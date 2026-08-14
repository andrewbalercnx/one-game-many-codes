# DESIGN.md — One Game, Many Codes

Round 2. Owned by the design surface. Contract: `LOOP.md`.

## GOAL

The MVP is a launchable FRAMING SITE plus the complete data skeleton beneath it. The site states what One Game, Many Codes is aiming for (the manifesto: complex systems emerge from simple rules; football is the demonstration), shows the visible frame all later content will fill — the Map, the nine codes, the thirteen rule dimensions, the timeline, each present as a browsable stub with its question and a stated "coming" promise — and trails the podcast: episode 1 coming ("Why did one football conquer the world?"), weekly thereafter. Beneath the surface, `/content/` holds the full Stage-1 skeleton so everything that follows is rendering, not restructuring. The original proving journey (superseded DECISION 7) becomes post-launch milestone 1, not the launch bar.

## CONSTRAINTS

- Static site generated from a typed content repository under `/content/`; entity schemas and field names per MVP brief §3 are normative.
- Pages render without JavaScript; anchor code, trail and search are `localStorage`/client enhancements.
- No accounts, no server-side state, no CMS. Deploy target: Cloudflare.
- Build-time content lint per MVP brief §7, blocking from day one.
- Rendered output never contains internal vocabulary: `tier`, `lens`, `Layer`, `gameplay lens`, `fan lens`.
- Rule-page lens headings, exact strings: `On the pitch`, `In the stands`.
- British English interface copy; code colour never the sole signal; WCAG AA; reduced-motion respected.
- Seed facts drafted by CC carry `verified: false` until the author's verification pass; the build reports the count.
- The site base URL is a single build-config value; no absolute site URLs are hardcoded in content, templates or generated output (canonical tags, sitemap and prompt links all derive from it).

## DECISIONS

1. Title: "One Game, Many Codes". The genome metaphor survives only as the Game DNA feature name.
2. Canonical entry: the 1925 offside change — homepage default question for first visits, episode 1, first page authored. SUPERSEDED BY DECISION 20.
3. Episode cadence: weekly; scripts banked ahead; narration recorded in question-sized segments, batched.
4. Language: British English source, "from the UK, to the world", origin-is-not-ownership stance (content brief §7).
5. Two consequence lenses (pitch/stands), never conflated; enforced by lint; invisible to readers.
6. Architecture is repository-first: pages are views over `/content/` entities; the podcast is a traversal (production model).
7. MVP scope is the vertical slice per MVP brief §§1, 4, 8; explicitly out of scope per §9. SUPERSEDED BY DECISION 17.
8. Loop write path: DESIGN.md updates travel design-surface → RCNX asset page (namespace `ogmc`, slug `loop-round-N-design`) → CC → verbatim commit prefixed `design:` (LOOP.md amendment, 2026-08-13).
9. Transport ingest unescape: CC decodes exactly five HTML entities — those for the characters < > " ' & — on ingest of each design page, amp decoded last, then commits; delivered files never contain literal entity strings; design surface verifies by GitHub diff. (Resolves Q1-d; LOOP.md Amendment 2.1.)
10. Branch/merge lifecycle: on author sign-off the accepted round PR merges to `main`; next DESIGN.md publishes after merge; CC branches `design/round-(N+1)` from updated `main`. (Resolves Q1-e; Amendment 2.2.)
11. Delivery finality: one slug = one finalised delivery; CC pulls only on explicit author go; corrections get a new slug. (Resolves Q1-f; Amendment 2.3.)
12. Authority split: repo is ground truth for repo facts; the asset page is authoritative for delivered content; conflicts flagged in ITERATION.md. Round-0 base-SHA discrepancy confirmed benign. (Resolves Q1-g and Q0-a; Amendment 2.4.)
13. Ratified: commit hygiene per Amendment 2.5; `the-football-genome-content-brief-v2.md` stays out of the repo; OQ3/OQ4 closed. (Resolves Q1-h and Q0-b.)
14. OQ5 resolved: the nine code `colour` values accepted as-is per `design-plan/design-plan.md` §1 (author sign-off, 2026-08-13).
15. OQ6 resolved: type system confirmed — display `Fraunces`, body `IBM Plex Sans`, apparatus `IBM Plex Mono`, SIL OFL, self-hosted (author sign-off, 2026-08-13).
16. OQ7 resolved: the statute card stays code-neutral — ink on paper, code named by chip only (author sign-off, 2026-08-13).
17. MVP redefined (supersedes DECISION 7). Launch scope: (a) manifesto home — the thesis and what the site is aiming for, assembled in site voice from content brief §§1–3; (b) the visible skeleton as browsable stubs — Map tree view from the full edge set, nine code stub pages, dimension stub pages, timeline index — every stub carrying its question, a one-paragraph promise of what will live there, and an honest "coming" state; (c) podcast teaser — episode 1 named by its question, weekly cadence stated; no player, no embed. (d) The full Stage-1 data skeleton enters `/content/` now: all 9 codes, all rule dimensions with per-code positions, ~100 dated events, the edge set with confidence markers — drafted `verified: false` where sourcing is pending. (e) The round-2 pages (1925 experiment, possession-limits) are retained in `/content/` and buildable but NOT linked from the launch surface; they open with their layer post-launch. (f) OQ1 is resolved for launch by (c): a teaser, not an embed; the episode-1 video question moves to the podcast layer's opening round. Prior out-of-scope items from DECISION 7 remain out of scope except as amended here.
18. Round-2 ratifications: (a) vendor the OFL WOFF2 files into `assets/fonts/` (resolves Q2-a); (b) the Python 3 + PyYAML generator is accepted (resolves Q2-b); (c) `dist/` stays committed until a preview deploy exists, then is gitignored — couples to DECISION 19 (resolves Q2-c).
19. OQ2 resolved — deploy target. Domain `manycodes.games` is purchased and on the author's Cloudflare account (2026-08-14) as a fresh zone. Round 3 stands up a Cloudflare Pages project serving `dist/` with its *.pages.dev preview URL; review moves to the preview and `dist/` is then gitignored per 18(c). The production custom-domain attachment of `manycodes.games` is the LAUNCH act, performed only on explicit author go — the preview must not be publicly announced. Redirect domains at the author's discretion, not assumed. The base-URL config value is the preview URL until launch, then https://manycodes.games.
20. Episode 1 and canonical entry re-anchored (supersedes DECISION 2). The opening story is the ball: "Why did one football conquer the world?" — the deepest rule in the family is the ball's shape (sphere vs prolate spheroid; ball specs are law text in every code), told from a rugby fan's vantage. On the pitch: what a true-rolling ball allows (biomechanics; kicked-ball speed and power; ground passing without hands) versus what a chaotic-bouncing carriable ball rewards (the handling family's radiation of codes). In the stands: compounding adoption — standard ball, any ground, FA→FIFA→World Cup — with the confounds stated (simplicity, trade networks, first-mover standardisation) and Gaelic football as the in-canon control case (round ball, hands, regional): the ball enables, it does not decree. Consequences: (i) new rule dimension 13 "The ball" joins the launch set — 13 dimension stubs, 22 stubs total; skeleton counts in 17(b)/(d) read accordingly; (ii) the homepage default question and the 17(c) teaser follow episode 1's question; (iii) the 1925 offside change becomes episode 2, remains the flagship natural experiment and the first fully-authored page (already built); (iv) a new second-wave consequence chain "Why one code rules the world" is registered, stands-side with its economics evidence base, biomechanics kept strictly on the pitch side; (v) the American ball's post-1906 evolution toward the pointed spiral-throwing form is recorded as a rules-reshape-equipment exhibit linking dimension 13 to the natural-experiments layer. Content note: `docs/the-ball-and-episode-1.md`.

## OPEN QUESTIONS

- OQ9 (author, round 3): the manifesto copy will be drafted by CC from content brief §§1–3 in the site voice and flagged for author review on the round-3 branch — confirm this route, or supply/commission the copy directly?
- OQ10 (CC, round 3): propose the stub-page template (question + promise + coming state + onward prompts within the skeleton) as a rendered example early in the branch, before stamping out all 22 stubs.

## CURRENT SPEC

Operative spec: `docs/one-game-many-codes-mvp-design-brief.md` — EXCEPT §§1, 4, 8, 9 (MVP scope), which DECISION 17 supersedes; entity schemas (§3), lint (§7), design direction (§6) and the navigation model remain in force for the frame's chrome. Intent context: content brief v3.1, navigation model, adversarial review, production model, `design-plan/` (visual system), and `docs/the-ball-and-episode-1.md` (dimension 13 and episode 1). Round-3 scope: the framing site per DECISIONS 17 and 20 — manifesto home with teaser (episode-1 question per DECISION 20), Map tree, 22 stub pages via the OQ10 template-first approach, timeline index, Stage-1 data entry including dimension 13 — plus DECISION 19's deploy work (Pages project, *.pages.dev preview, base-URL config, then gitignore `dist/`), DECISION 18(a) font vendoring, and the three carried round-2 notes. Round-2 pages stay unlinked per 17(e). Domain attachment to `manycodes.games` is NOT in round 3 — launch only, on author go.
