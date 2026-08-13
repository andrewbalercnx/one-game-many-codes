# One Game, Many Codes
## MVP design brief – for implementation by Claude Code

This brief is self-contained but assumes three companion documents are placed in the repo before work starts: the content brief (v3.1), the navigation model, and the production model. Where this brief and those documents conflict, this brief wins for the MVP; the companions win for intent.

---

# 1. What the MVP proves

One deployed vertical slice demonstrating the whole concept end to end:

> A first-time visitor lands (from any URL), is oriented, meets the 1925 offside story, follows an authored question sideways into an unfamiliar code, picks up their anchor code along the way, sees where they've been, and can watch episode one instead of reading it.

If that journey works on a phone, the MVP has succeeded. Everything below serves it; anything that doesn't is out of scope (§9).

---

# 2. Architecture in one paragraph

A static site generated from a structured content repository. Content lives as version-controlled files with typed frontmatter (the entity model in §3); pages are build-time views assembled from those files; the only client-side state is `localStorage` for the anchor code and the trail. No accounts, no server-side state, no CMS. Deploy to Cloudflare (Pages or a Worker serving static assets – implementer's choice). Framework choice is the implementer's, with a strong preference for boring: a static site generator or a light build script beats a SPA; ship HTML that works without JavaScript, then enhance (anchor, trail, search are enhancements – reading and navigating must not depend on them).

---

# 3. The content repository

Entities are files under `/content/`, one file per entity, YAML frontmatter + markdown body. IDs are slugs, stable, referenced across files. This is the production model's §2 made concrete; keep field names exactly as below so the lint (§7) and future tooling agree.

```
/content/
  codes/          soccer.md, rugby-league.md, ...
  dimensions/     possession-limits.md, offside.md, ...
  events/         1925-offside-two-defenders.md, ...
  claims/         limited-tackles-made-kicking-rational.md, ...
  actions/        mark.md, fair-catch.md, play-the-ball.md, ...
  edges/          union-to-league-1895.md, ...
  sources/        vicente-2025.md, fa-minutes-1925.md, ...
  clips/          wm-formation-diagram.md, ...
  episodes/       ep1-1925-offside.md, ...
```

**Code** – `id, name, colour (hex), status (first|second|satellite|ancestor), one_line_genome, bridges: {code_id: sentence}` – body: the code page prose sections.

**Dimension** – `id, question, positions: [{code, rule_text, law_ref}]` – body: the rule page prose, with `## On the pitch` and `## In the stands` as required headings.

**Event** – `id, date, code, title, change_summary, law_quote (optional), why_introduced, sources: [source_id], experiment: true|false` – body: experiment-page prose when `experiment: true`.

**Claim** – `id, statement, from (dimension_id#code or event_id), to (short phenomenon label), lens (pitch|stands), tier (1|2|3), sources: [source_id], confounds (optional)` – body optional (elaboration).

**Action** – `id, name, code, definition, rule_basis (dimension_id#code), misconception, sibling (action_id, optional), ancestor_rule (text, required if sibling), clip (clip_id), door (any entity/page id, required)`.

**Edge** – `id, from (code_id), to (code_id), kind (descent|influence), confidence (established|probable|contested), note`.

**Source** – `id, citation, url (optional), type (law_text|paper|match_data|press)`.

**Clip** – `id, concept, url, rights_note, annotation (the "which rule made this happen" sentence), fallback_image (path, required), last_checked (date)`.

**Episode** – `id, number, title_question, source_page (entity id), video_url, audio_url (optional), transcript (body), closing_question, closing_door (entity/page id)`.

Prompts are part of page prose, authored per page, expressed as markdown links with a `?prompt` marker or a small frontmatter list `prompts: [{question, target}]` – implementer's choice, but they must be machine-identifiable (the trail and lint depend on it).

---

# 4. Pages to render

Every page shares a **deep-entry header**: the code's colour and name (colour never the sole signal), the page's question as its title, and one line – "part of One Game, Many Codes" – linking to the Map. Cold arrival from any URL must self-orient; assume the homepage is never seen.

1. **Home** – one full-width question (default for new visitors: the 1925 story; rotate for returning ones), the thesis line beneath, three doors: *Start with your game* (anchor picker), *Explore the family tree* (Map), *Watch* (episode hub). Nothing else above the fold.
2. **The Map (tree view only)** – the descent tree from the edge set, progressively disclosed (trunk visible, branches expand), each split annotated with its one-line cause, each node opening its four answers in place with a door to the code page. Graph view is out of MVP scope; contested edges render in the tree with their confidence note where they appear.
3. **Code pages** (all 9, but only soccer and rugby league fully written for MVP) – one-sentence genome, bridge line for the visitor's anchor, descent summary, rules that matter (links into dimensions), signature actions, "still evolving" section. Genome cards: out of scope (§9); leave a designed placeholder slot.
4. **Rule page** (one for MVP: possession limits) – rendered from the dimension entity on the brief's template: the rule per code (positions table/strip), why introduced, *On the pitch*, *In the stands*, adoption and rejection. A compact all-codes strip showing each code's position, colour-marked.
5. **Experiment page** (one for MVP: 1925 offside) – before / the change (law quote styled as an artefact) / what happened next (the goals number given room) / what it demonstrates. This is the flagship page; it gets the design attention.
6. **Glossary entries** (MVP set: mark, fair catch, play-the-ball, offside trap, kick-chase, WM formation) – definition, rule basis, misconception, clip with fallback, sibling reveal (anchor-first), closing door. No entry ends without a door.
7. **Timeline** – simple vertical/horizontal list of events by date, colour-marked, each linking to its page. An index, not a feature.
8. **Episode hub + episode page** – hub lists the season with stated weekly cadence and question-titles; the episode page embeds the video (external host URL from the entity), shows the transcript, ends with the closing question as a door. Audio feed: out of scope.
9. **Search** – client-side, glossary-first ordering, results phrased as the questions pages answer. A prebuilt JSON index is fine.

---

# 5. Navigation behaviours

- **Prompts** – every content page ends with its authored prompts (2–4), each rendered with the destination code's colour. These are the primary navigation; style them as the page's most inviting element, not a footer.
- **Anchor code** – optional picker ("Which football do you know best?") offered on first meaningful interaction and available in the header; stored in `localStorage`; drives the bridge line shown on code pages and sibling-first ordering in glossary entries. Skippable, changeable, no nagging.
- **The trail** – the sequence of question-prompts followed this session (and persisted locally), rendered as a compact retraceable strip; collapses to a single "how I got here" control on mobile. Following browser navigation without a prompt does not pollute the trail.
- **Mobile** – design mobile-first; the front door's *Watch* leads on small screens per the navigation model.

---

# 6. Design direction

The subject supplies the aesthetic: law books, club colours, chalkboards and formation diagrams – the visual world of rulemaking and the games it produced. Direction, not prescription; the implementer runs the full design process (plan, critique, build) within these constraints:

- **Code colours are the identity system.** Nine fixed colours doing wayfinding work everywhere; the rest of the palette stays quiet so they can. Never colour alone – always paired with the code's name.
- **The signature element is the rendered law text.** Rule quotations (the 1925 line, the 1863 fork) set as typographic artefacts – the site's thesis is that these small texts changed everything, and the design should make a single quoted line feel consequential.
- Typography: a characterful display face used sparingly for questions and law quotes, a highly readable body face for long-form causal prose; long reads are the core activity, so body settings win any conflict.
- British English in all interface copy; questions in sentence case; controls say what they do.
- Quality floor: responsive to small phones, visible keyboard focus, reduced-motion respected, WCAG AA contrast, alt text on every clip fallback image.
- Avoid the current AI-default looks (cream + serif + terracotta; near-black + acid accent; broadsheet hairlines) unless a deliberate case is made from this subject.

---

# 7. Content lint (build-time, blocking)

A script run in the build that fails on:

- any tier-1 claim without at least one source of type `law_text` or `match_data` or `paper`
- any `lens: stands` claim whose only sources are match_data (the lens-laundering check)
- any action without a `door`, or with a `sibling` but no `ancestor_rule`
- any clip without `fallback_image` or with `last_checked` older than 120 days (warning, not failure, for the age check)
- any contested edge without a `note`
- any content page (code, dimension, event-experiment, action) without at least one authored prompt/door
- any dimension body missing the two lens headings
- reader-facing output containing internal vocabulary: "tier", "lens", "gameplay lens", "fan lens", "Layer" (check rendered pages, not source files)

The lint is the brief's editorial policy made mechanical; keep it strict from day one.

---

# 8. Seed content

Claude Code drafts the seed entries from the companion documents; the author verifies before launch. Mark every unverified fact `verified: false` in frontmatter (lint warns, doesn't fail, on unverified – but the count is reported).

- All 9 codes (frontmatter complete; full prose for soccer and rugby league only, stubs elsewhere)
- All 12 dimensions as frontmatter with positions; full body for possession-limits only
- ~25 events including all seven experiments; full body for 1925 only
- The claims for the 1925 page and the possession-limits page (expect ~10–15 entries), with sources entered as far as the companion documents support and `verified: false` where sourcing is a placeholder
- The 6 glossary entries in §4.6
- The edge set for the tree (~15 edges)
- Episode 1 entity with a placeholder `video_url` and the transcript drafted from the production model's §5 beat structure
- Clip entities may use placeholder URLs but must have real fallback diagrams (simple SVG formation/rule diagrams are acceptable and preferred over nothing)

---

# 9. Out of scope for MVP

Graph view of the Map; genome cards and all DNA data; Compare; audio syndication; localisation; the full episode slate; search beyond the client-side index; any gamification; accounts or server-side state; comment or feedback machinery. Leave clean seams (the placeholder card slot, the entity fields already defined) rather than partial implementations.

---

# 10. Acceptance criteria

1. Deployed and reachable on Cloudflare; all pages render without JavaScript; enhancements degrade gracefully.
2. Cold-arrival test: landing directly on the possession-limits page, a visitor can identify the code context, the site, and a next step within the first screen – on a phone.
3. The proving journey (§1) is walkable: home → 1925 story → authored prompt → possession-limits → prompt → rugby league code page, with the trail showing the path and the anchor (if set) changing the bridge line and glossary ordering.
4. Episode 1 page plays an embedded video, shows its transcript, and its closing question links into the site.
5. The content lint runs in the build and passes; deliberately breaking a rule (e.g. removing a glossary door) fails the build.
6. Lighthouse (or equivalent): accessibility ≥ 95 on the experiment page and a code page; no reader-facing internal vocabulary anywhere.
7. The unverified-fact count is reported at build time and listed in the README for the author's verification pass.

---

# 11. Suggested milestones

1. Repo scaffold: content directories, entity schemas, build pipeline, deploy to Cloudflare with a placeholder page.
2. Seed content drafted (§8) and lint implemented (§7) – content and its enforcement land together.
3. Views: deep-entry header, home, Map tree, the four fully-written pages, glossary, timeline.
4. Behaviours: prompts styling, anchor, trail, search.
5. Episode hub and episode 1; design pass on the experiment page (the flagship); acceptance run (§10).

Small, reviewable increments; the author reviews content accuracy at milestone 2 and design at milestone 5.
