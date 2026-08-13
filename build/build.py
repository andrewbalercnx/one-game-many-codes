#!/usr/bin/env python3
"""One Game, Many Codes — static build (round 2).

Pages are views over /content entities (DECISION 6). This round renders the
deep-entry header, the 1925 experiment page (statute-card debut) and the
possession-limits rule page, plus a placeholder landing so the slice is
browsable. A blocking content lint (MVP brief §7, the relevant subset for this
round) runs before anything is written; a failing check aborts the build.
"""
import os, re, sys, html, glob
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
DIST = os.path.join(ROOT, "dist")
CSS = open(os.path.join(ROOT, "assets", "site.css"), encoding="utf-8").read()

INK = "#1A1E1C"

# ---------- load entities ----------
def load(kind):
    out = {}
    for path in glob.glob(os.path.join(CONTENT, kind, "*.md")):
        raw = open(path, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", raw, re.S)
        if not m:
            fail(f"{os.path.relpath(path, ROOT)}: missing YAML frontmatter")
        meta = yaml.safe_load(m.group(1)) or {}
        meta["_body"] = m.group(2).strip("\n")
        meta["_path"] = os.path.relpath(path, ROOT)
        out[meta.get("id")] = meta
    return out

LINT_ERRORS = []
def fail(msg): LINT_ERRORS.append(msg)

# ---------- tiny markdown ----------
def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    return t

def body_sections(body):
    """Yield (level, heading, anchor, html) sections; heading None for the intro."""
    sections, cur_head, cur_lvl, buf = [], None, 0, []
    def flush():
        htmlp = "\n".join(f"<p>{inline(p.strip())}</p>" for p in re.split(r"\n\s*\n", "\n".join(buf).strip()) if p.strip())
        anchor = slugify(cur_head) if cur_head else None
        sections.append((cur_lvl, cur_head, anchor, htmlp))
    for line in body.split("\n"):
        h = re.match(r"^(#{2,3})\s+(.*)$", line)
        if h:
            flush(); buf = []
            cur_lvl, cur_head = len(h.group(1)), h.group(2).strip()
        else:
            buf.append(line)
    flush()
    return sections

# ---------- shared chrome ----------
def code_colour(code_id):
    return codes.get(code_id, {}).get("colour", INK)

def deep_header(code_name, colour, title_html, question=False):
    return f"""<header class="deep-header">
  <div class="spine" style="background:{colour}"></div>
  <div class="code-line"><span class="code-name">{html.escape(code_name)}</span></div>
  <h1>{title_html}</h1>
  <div class="site-link">part of <a href="index.html">One Game, Many Codes</a></div>
</header>"""

def render_prompts(prompts):
    if not prompts: return ""
    items = []
    for p in prompts:
        t = p["target"]
        href = t if t.startswith("#") else t.split("/")[-1] + ".html"
        slug = None if t.startswith("#") else t.split("/")[-1]
        code = events.get(slug, {}).get("code") if slug in events else (slug if slug in codes else None)
        colour = code_colour(code) if code else INK
        items.append(
            f'<a class="prompt" href="{html.escape(href)}" style="border-left-color:{colour}">'
            f'<span>{html.escape(p["question"])}</span><span class="arrow">&rarr;</span></a>'
        )
    return '<nav class="prompts"><h2>Where next</h2>\n' + "\n".join(items) + "</nav>"

def statute_card(ev):
    code = ev.get("code")
    colour = code_colour(code)
    cname = codes.get(code, {}).get("name", code or "")
    src_ref = ""
    for sid in ev.get("sources", []):
        s = sources.get(sid)
        if s and s.get("type") == "law_text":
            src_ref = s.get("citation", ""); break
    ref = " · ".join(x for x in [src_ref or "law text", str(ev.get("date", ""))] if x)
    badge = "" if ev.get("verified") else '<span class="unverified">unverified · paraphrase</span>'
    return f"""<figure class="statute">
  <div class="cite"><span class="code-chip" style="background:{colour}">{html.escape(cname)}</span><span class="ref">{html.escape(ref)}</span></div>
  <blockquote class="line">{html.escape(ev.get("law_quote",""))}</blockquote>
  <figcaption class="foot"><span>{html.escape(ev.get("change_summary",""))}</span>{badge}</figcaption>
</figure>"""

def page(title, inner, anchors):
    doc = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — One Game, Many Codes</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="wrap">
{inner}
<footer class="pagefoot">One Game, Many Codes — a work in progress. British English throughout.</footer>
</div>
</body>
</html>
"""
    return doc, anchors

# ---------- page builders ----------
def build_event(ev):
    colour = code_colour(ev.get("code"))
    cname = codes.get(ev.get("code"), {}).get("name", "")
    parts = [deep_header(cname, colour, html.escape(ev["title"]))]
    anchors = set()
    for lvl, head, anchor, htmlp in body_sections(ev["_body"]):
        if head:
            anchors.add(anchor)
            parts.append(f'<h{lvl} id="{anchor}">{html.escape(head)}</h{lvl}>')
        parts.append(htmlp)
        if head and head.strip().lower() == "the change":
            parts.append(statute_card(ev))
    parts.append(render_prompts(ev.get("prompts")))
    return page(ev["title"], "\n".join(p for p in parts if p), anchors)

def build_dimension(dim):
    parts = [deep_header("A rule across the codes", INK, html.escape(dim["question"]), question=True)]
    # positions strip (colour-marked, name always shown)
    strip = ['<ul class="positions">']
    for pos in dim.get("positions", []):
        c = pos["code"]; colour = code_colour(c); cname = codes.get(c, {}).get("name", c)
        strip.append(
            f'<li><div class="head" style="background:{colour}"><span class="code-name">{html.escape(cname)}</span></div>'
            f'<div class="rule-text">{html.escape(pos["rule_text"])}</div>'
            f'<div class="law-ref">{html.escape(pos.get("law_ref",""))}</div></li>'
        )
    strip.append("</ul>")
    parts.append("\n".join(strip))
    anchors = set()
    for lvl, head, anchor, htmlp in body_sections(dim["_body"]):
        if head:
            anchors.add(anchor)
            parts.append(f'<h{lvl} id="{anchor}">{html.escape(head)}</h{lvl}>')
        parts.append(htmlp)
    parts.append(render_prompts(dim.get("prompts")))
    return page(dim["question"], "\n".join(p for p in parts if p), anchors)

def build_index():
    inner = f"""<header class="deep-header">
  <div class="spine" style="background:{INK}"></div>
  <div class="code-line"><span class="code-name">Placeholder landing</span></div>
  <h1>One Game, Many Codes</h1>
  <div class="site-link">Small rule changes create entirely different games.</div>
</header>
<p class="lede">A vertical slice. The full front door, the Map and the code pages come in later rounds; for now, two pages carry the idea end to end.</p>
<nav class="prompts"><h2>Start here</h2>
<a class="prompt" href="1925-offside-two-defenders.html" style="border-left-color:{code_colour('soccer')}"><span>How did one line in the law book change football?</span><span class="arrow">&rarr;</span></a>
<a class="prompt" href="possession-limits.html" style="border-left-color:{INK}"><span>How long do you get to keep the ball?</span><span class="arrow">&rarr;</span></a>
</nav>"""
    return page("One Game, Many Codes", inner, set())

# ---------- lint (blocking; MVP brief §7 subset for this round) ----------
BANNED = [(re.compile(r"\btier\b", re.I), "tier"),
          (re.compile(r"\blens(es)?\b", re.I), "lens"),
          (re.compile(r"\bgameplay lens\b", re.I), "gameplay lens"),
          (re.compile(r"\bfan lens\b", re.I), "fan lens"),
          (re.compile(r"\bLayer\b"), "Layer")]

def lint_entities():
    src_types = {sid: s.get("type") for sid, s in sources.items()}
    for cid, c in claims.items():
        srcs = c.get("sources", []) or []
        if c.get("tier") == 1:
            if not any(src_types.get(s) in ("law_text", "match_data", "paper") for s in srcs):
                fail(f"claim {cid}: tier-1 claim needs a law_text/match_data/paper source")
        if c.get("lens") == "stands" and srcs and all(src_types.get(s) == "match_data" for s in srcs):
            fail(f"claim {cid}: stands claim may not cite only match_data (laundering)")
    for aid, a in actions.items():
        if not a.get("door"): fail(f"action {aid}: missing door")
        if a.get("sibling") and not a.get("ancestor_rule"): fail(f"action {aid}: sibling without ancestor_rule")
    for eid, e in edges.items():
        if e.get("confidence") == "contested" and not e.get("note"): fail(f"edge {eid}: contested without note")
    # content pages need at least one prompt/door
    for kind, coll in (("code", codes), ("dimension", dimensions), ("action", actions)):
        for i, ent in coll.items():
            if not ent.get("prompts") and not ent.get("door"):
                fail(f"{kind} {i}: no authored prompt/door")
    for eid, e in events.items():
        if e.get("experiment") and not e.get("prompts"):
            fail(f"event {eid}: experiment page needs a prompt")
    for did, d in dimensions.items():
        b = d.get("_body", "")
        if "## On the pitch" not in b: fail(f"dimension {did}: missing '## On the pitch'")
        if "## In the stands" not in b: fail(f"dimension {did}: missing '## In the stands'")

def lint_output(fname, htmldoc, all_files, anchors):
    for rx, label in BANNED:
        if rx.search(htmldoc):
            fail(f"{fname}: rendered output contains internal vocabulary '{label}'")
    for href in re.findall(r'href="([^"]+)"', htmldoc):
        if href.startswith("#"):
            if href[1:] not in anchors: fail(f"{fname}: dead in-page anchor {href}")
        elif href.endswith(".html"):
            if href not in all_files: fail(f"{fname}: dead link {href}")

# ---------- run ----------
codes = load("codes"); dimensions = load("dimensions"); events = load("events")
claims = load("claims"); sources = load("sources")
actions = load("actions") if os.path.isdir(os.path.join(CONTENT, "actions")) else {}
edges = load("edges") if os.path.isdir(os.path.join(CONTENT, "edges")) else {}

lint_entities()

pages = {}
d, a = build_index();                                  pages["index.html"] = (d, a)
ev = events["1925-offside-two-defenders"]; d, a = build_event(ev);     pages["1925-offside-two-defenders.html"] = (d, a)
dim = dimensions["possession-limits"];    d, a = build_dimension(dim); pages["possession-limits.html"] = (d, a)

all_files = set(pages.keys())
for fname, (doc, anchors) in pages.items():
    lint_output(fname, doc, all_files, anchors)

# unverified count (informational)
unverified = sum(1 for coll in (codes, dimensions, events, claims, sources)
                 for e in coll.values() if e.get("verified") is False)

if LINT_ERRORS:
    print("LINT FAILED:")
    for e in LINT_ERRORS: print("  - " + e)
    sys.exit(1)

os.makedirs(DIST, exist_ok=True)
os.makedirs(os.path.join(DIST, "assets"), exist_ok=True)
for fname, (doc, _) in pages.items():
    open(os.path.join(DIST, fname), "w", encoding="utf-8").write(doc)
open(os.path.join(DIST, "assets", "site.css"), "w", encoding="utf-8").write(CSS)

print(f"Build OK — {len(pages)} pages: {', '.join(sorted(pages))}")
print(f"Unverified facts flagged (verified: false): {unverified} — for the author's verification pass.")
