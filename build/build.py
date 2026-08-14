#!/usr/bin/env python3
"""One Game, Many Codes — static build.

Round 3 (increment 1 — the OQ10 template-first checkpoint + the Amendment 3 claims
channel storage). This build:
  - reads the single base-URL config (DECISION 19);
  - keeps the round-2 pages buildable but UNLINKED from the launch surface (DECISION 17e);
  - renders the manifesto home with the author-copy placeholder (OQ9) and the episode-1
    teaser (DECISION 20);
  - renders ONE example stub for OQ10 review (the 22-stub skeleton is stamped out only
    after the template is signed off);
  - regenerates content/INDEX.md (the claims ledger, Amendment 3.1) and runs the claims
    lint additions.
A blocking content lint runs before anything is written.
"""
import os, re, sys, html, glob, json
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
DIST = os.path.join(ROOT, "dist")
CSS = open(os.path.join(ROOT, "assets", "site.css"), encoding="utf-8").read()
CONFIG = json.load(open(os.path.join(ROOT, "site.config.json"), encoding="utf-8"))
BASE_URL = CONFIG.get("base_url", "")   # single source; empty => relative links
INK = "#1A1E1C"

LINT_ERRORS = []
def fail(msg): LINT_ERRORS.append(msg)

# ---------- load ----------
def load(kind):
    out = {}
    for path in glob.glob(os.path.join(CONTENT, kind, "*.md")):
        raw = open(path, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", raw, re.S)
        if not m: fail(f"{os.path.relpath(path, ROOT)}: missing YAML frontmatter"); continue
        meta = yaml.safe_load(m.group(1)) or {}
        meta["_body"] = m.group(2).strip("\n")
        out[meta.get("id")] = meta
    return out

# ---------- markdown ----------
def slugify(t): return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    return t
def body_sections(body):
    sections, cur_head, cur_lvl, buf = [], None, 0, []
    def flush():
        htmlp = "\n".join(f"<p>{inline(p.strip())}</p>" for p in re.split(r"\n\s*\n", "\n".join(buf).strip()) if p.strip())
        sections.append((cur_lvl, cur_head, slugify(cur_head) if cur_head else None, htmlp))
    for line in body.split("\n"):
        h = re.match(r"^(#{2,3})\s+(.*)$", line)
        if h: flush(); buf=[]; cur_lvl, cur_head = len(h.group(1)), h.group(2).strip()
        else: buf.append(line)
    flush()
    return sections

# ---------- chrome ----------
def code_colour(cid): return codes.get(cid, {}).get("colour", INK)

def deep_header(label, colour, title_html):
    return (f'<header class="deep-header"><div class="spine" style="background:{colour}"></div>'
            f'<div class="code-line"><span class="code-name">{html.escape(label)}</span></div>'
            f'<h1>{title_html}</h1>'
            f'<div class="site-link">part of <a href="index.html">One Game, Many Codes</a></div></header>')

def render_prompts(prompts):
    if not prompts: return ""
    items = []
    for p in prompts:
        t = p["target"]; href = t if t.startswith("#") else t.split("/")[-1] + ".html"
        slug = None if t.startswith("#") else t.split("/")[-1]
        code = events.get(slug, {}).get("code") if slug in events else (slug if slug in codes else None)
        colour = code_colour(code) if code else INK
        items.append(f'<a class="prompt" href="{html.escape(href)}" style="border-left-color:{colour}">'
                     f'<span>{html.escape(p["question"])}</span><span class="arrow">&rarr;</span></a>')
    return '<nav class="prompts"><h2>Where next</h2>\n' + "\n".join(items) + "</nav>"

def page(title, inner):
    return (f'<!doctype html>\n<html lang="en-GB">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{html.escape(title)} — One Game, Many Codes</title>\n<style>\n{CSS}\n</style>\n</head>\n'
            f'<body>\n<div class="wrap">\n{inner}\n'
            f'<footer class="pagefoot">One Game, Many Codes — a work in progress. British English throughout.</footer>\n'
            f'</div>\n</body>\n</html>\n')

# ---------- pages ----------
def statute_card(ev):
    colour = code_colour(ev.get("code")); cname = codes.get(ev.get("code"), {}).get("name", ev.get("code") or "")
    src_ref = ""
    for sid in ev.get("sources", []):
        s = sources.get(sid)
        if s and s.get("type") == "law_text": src_ref = s.get("citation", ""); break
    ref = " · ".join(x for x in [src_ref or "law text", str(ev.get("date",""))] if x)
    badge = "" if ev.get("verified") else '<span class="unverified">unverified · paraphrase</span>'
    return (f'<figure class="statute"><div class="cite"><span class="code-chip" style="background:{colour}">'
            f'{html.escape(cname)}</span><span class="ref">{html.escape(ref)}</span></div>'
            f'<blockquote class="line">{html.escape(ev.get("law_quote",""))}</blockquote>'
            f'<figcaption class="foot"><span>{html.escape(ev.get("change_summary",""))}</span>{badge}</figcaption></figure>')

def build_event(ev):
    colour = code_colour(ev.get("code")); cname = codes.get(ev.get("code"), {}).get("name","")
    parts = [deep_header(cname, colour, html.escape(ev["title"]))]
    anchors = set()
    for lvl, head, anchor, htmlp in body_sections(ev["_body"]):
        if head: anchors.add(anchor); parts.append(f'<h{lvl} id="{anchor}">{html.escape(head)}</h{lvl}>')
        parts.append(htmlp)
        if head and head.strip().lower() == "the change": parts.append(statute_card(ev))
    parts.append(render_prompts(ev.get("prompts")))
    return page(ev["title"], "\n".join(p for p in parts if p)), anchors

def build_dimension(dim):
    parts = [deep_header("A rule across the codes", INK, html.escape(dim["question"]))]
    strip = ['<ul class="positions">']
    for pos in dim.get("positions", []):
        c = pos["code"]; strip.append(
            f'<li><div class="head" style="background:{code_colour(c)}"><span class="code-name">'
            f'{html.escape(codes.get(c,{}).get("name",c))}</span></div>'
            f'<div class="rule-text">{html.escape(pos["rule_text"])}</div>'
            f'<div class="law-ref">{html.escape(pos.get("law_ref",""))}</div></li>')
    strip.append("</ul>")
    parts.append("\n".join(strip))
    anchors = set()
    for lvl, head, anchor, htmlp in body_sections(dim["_body"]):
        if head: anchors.add(anchor); parts.append(f'<h{lvl} id="{anchor}">{html.escape(head)}</h{lvl}>')
        parts.append(htmlp)
    parts.append(render_prompts(dim.get("prompts")))
    return page(dim["question"], "\n".join(p for p in parts if p)), anchors

def build_stub(kind, ent, question, promise):
    """OQ10 stub template: question + one-paragraph promise + honest 'coming' state + onward prompt."""
    colour = ent.get("colour", INK) if kind == "code" else INK
    label = "Coming — " + kind
    inner = (deep_header(label, colour, html.escape(question))
             + f'<p class="lede">{html.escape(promise)}</p>'
             + (f'<p><em>{html.escape(ent.get("one_line_genome",""))}</em></p>' if ent.get("one_line_genome") else "")
             + '<p class="pagefoot" style="margin-top:1.5rem">This page is a stub in the launch skeleton: '
               'its question and place are fixed; the full content arrives with its layer.</p>'
             + render_prompts([{"question": "See what the whole site is aiming for", "target": "index"}]))
    return page(question, inner), set()

def build_manifesto_home():
    man = pages_.get("manifesto", {})
    body = man.get("_body", "")
    m = re.search(r"BEGIN-AUTHOR-COPY\n(.*?)\nEND-AUTHOR-COPY", body, re.S)
    author_copy = (m.group(1).strip() if m else "")
    if author_copy:
        manifesto_html = "\n".join(f"<p>{inline(p.strip())}</p>" for p in re.split(r"\n\s*\n", author_copy) if p.strip())
    else:
        manifesto_html = ('<div class="statute"><div class="cite"><span class="ref">Manifesto</span>'
                          '<span class="unverified">author copy pending</span></div>'
                          '<blockquote class="line">The manifesto is written by the author and committed here verbatim (OQ9).</blockquote>'
                          '<figcaption class="foot"><span>This placeholder is replaced, not drafted over.</span></figcaption></div>')
    teaser = ('<nav class="prompts"><h2>The podcast</h2>'
              '<a class="prompt" href="index.html" style="border-left-color:' + code_colour("soccer") + '">'
              '<span>Episode 1, coming: Why did one football conquer the world?</span>'
              '<span class="arrow">weekly</span></a></nav>')
    skeleton = ('<nav class="prompts"><h2>The frame</h2>'
                '<a class="prompt" href="stub-example.html" style="border-left-color:' + INK + '">'
                '<span>See the skeleton — an example of a page waiting to be filled</span><span class="arrow">&rarr;</span></a></nav>')
    inner = (f'<header class="deep-header"><div class="spine" style="background:{INK}"></div>'
             f'<div class="code-line"><span class="code-name">One Game, Many Codes</span></div>'
             f'<h1>{html.escape(man.get("title","One Game, Many Codes"))}</h1>'
             f'<div class="site-link">a framing site — the frame is here; the content is coming</div></header>'
             f'{manifesto_html}\n{teaser}\n{skeleton}')
    return page(man.get("title","One Game, Many Codes"), inner), set()

# ---------- claims ledger + lint (Amendment 3) ----------
def source_ceiling(s):
    m = re.search(r"Ceiling:\s*tier\s*(\d)", s.get("_body",""))
    if m: return int(m.group(1))
    return 3 if s.get("type") == "press" else 1   # default: press weakest, others can carry tier 1

def source_status(s):
    m = re.search(r"Status:\s*(.+?)(?:\.\s|\.$|$)", s.get("_body",""))
    return (m.group(1).strip() if m else "—")

def generate_index():
    lines = ["# Content ledger — generated by build (do not edit)", "",
             "## Claims", "id | lens | tier | verified | from -> to | source ids"]
    for cid in sorted(claims):
        c = claims[cid]
        lines.append(f"{cid} | {c.get('lens','')} | {c.get('tier','')} | {c.get('verified')} | "
                     f"{c.get('from','')} -> {c.get('to','')} | {','.join(c.get('sources',[]) or [])}")
    lines += ["", "## Sources", "id | type | ceiling | status"]
    for sid in sorted(sources):
        s = sources[sid]
        lines.append(f"{sid} | {s.get('type','')} | {source_ceiling(s)} | {source_status(s)}")
    return "\n".join(lines) + "\n"

def lint_claims():
    src_types = {sid: s.get("type") for sid, s in sources.items()}
    ceil = {sid: source_ceiling(s) for sid, s in sources.items()}
    for cid, c in claims.items():
        srcs = c.get("sources", []) or []
        for s in srcs:
            if s not in sources: fail(f"claim {cid}: cites missing source id '{s}'")
        if c.get("tier") == 1 and not any(src_types.get(s) in ("law_text","match_data","paper") for s in srcs):
            fail(f"claim {cid}: tier-1 claim needs a law_text/match_data/paper source")
        if c.get("lens") == "stands" and srcs and all(src_types.get(s) == "match_data" for s in srcs):
            fail(f"claim {cid}: stands claim may not cite only match_data (laundering)")
        if c.get("tier") in (1,2) and srcs and all(ceil.get(s, 3) > c["tier"] for s in srcs):
            fail(f"claim {cid}: tier-{c['tier']} claim whose only sources are press-ceiling")
        if c.get("verified") is True and c.get("proposed_by") != "author":
            fail(f"claim {cid}: verified:true requires proposed_by author (only the author flips it)")

BANNED = [(re.compile(r"\btier\b", re.I), "tier"), (re.compile(r"\blens(es)?\b", re.I), "lens"),
          (re.compile(r"\bgameplay lens\b", re.I), "gameplay lens"), (re.compile(r"\bfan lens\b", re.I), "fan lens"),
          (re.compile(r"\bLayer\b"), "Layer")]
def lint_output(fname, doc, all_files, anchors):
    for rx, label in BANNED:
        if rx.search(doc): fail(f"{fname}: rendered output contains internal vocabulary '{label}'")
    for href in re.findall(r'href="([^"]+)"', doc):
        if href.startswith("#"):
            if href[1:] not in anchors: fail(f"{fname}: dead in-page anchor {href}")
        elif href.endswith(".html") and href not in all_files: fail(f"{fname}: dead link {href}")

def lint_content_pages():
    for kind, coll in (("code", codes), ("dimension", dimensions)):
        for i, ent in coll.items():
            if not ent.get("prompts") and not ent.get("door"): fail(f"{kind} {i}: no authored prompt/door")
    for did, d in dimensions.items():
        if "## On the pitch" not in d.get("_body",""): fail(f"dimension {did}: missing '## On the pitch'")
        if "## In the stands" not in d.get("_body",""): fail(f"dimension {did}: missing '## In the stands'")

# ---------- run ----------
codes = load("codes"); dimensions = load("dimensions"); events = load("events")
claims = load("claims"); sources = load("sources"); pages_ = load("pages")

lint_claims(); lint_content_pages()

# regenerate the ledger (Amendment 3.1) — committed with every build
index_md = generate_index()
index_path = os.path.join(CONTENT, "INDEX.md")
prev = open(index_path, encoding="utf-8").read() if os.path.exists(index_path) else None
index_changed = (prev != index_md)

built = {}
d, a = build_manifesto_home();                       built["index.html"] = (d, a)
ev = events["1925-offside-two-defenders"];  d,a = build_event(ev);       built["1925-offside-two-defenders.html"] = (d,a)
dim = dimensions["possession-limits"];      d,a = build_dimension(dim);  built["possession-limits.html"] = (d,a)
# OQ10: ONE example stub (code stub). The 22-stub skeleton is stamped only after sign-off.
d,a = build_stub("code", codes["rugby-union"], "What kind of game is rugby union — and why?",
                 "A full code page will live here: its one-sentence genome, the four to six rules that shape it, "
                 "its signature actions, and where it sits in the family tree.")
built["stub-example.html"] = (d,a)

all_files = set(built)
for fname,(doc,anchors) in built.items(): lint_output(fname, doc, all_files, anchors)

unverified = sum(1 for coll in (codes,dimensions,events,claims,sources,pages_) for e in coll.values() if e.get("verified") is False)

if LINT_ERRORS:
    print("LINT FAILED:")
    for e in LINT_ERRORS: print("  - " + e)
    sys.exit(1)

open(index_path, "w", encoding="utf-8").write(index_md)   # ledger committed with every build
os.makedirs(os.path.join(DIST,"assets"), exist_ok=True)
for fname,(doc,_) in built.items(): open(os.path.join(DIST,fname),"w",encoding="utf-8").write(doc)
open(os.path.join(DIST,"assets","site.css"),"w",encoding="utf-8").write(CSS)

print(f"Build OK — {len(built)} pages: {', '.join(sorted(built))}")
print(f"content/INDEX.md {'regenerated' if index_changed else 'unchanged'} "
      f"({len(claims)} claims, {len(sources)} sources).")
print(f"base_url = {BASE_URL!r} (empty = relative links until the Pages preview).")
print(f"Unverified facts flagged (verified: false): {unverified}.")
