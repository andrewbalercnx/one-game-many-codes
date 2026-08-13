# DESIGN.md — One Game, Many Codes

Round 1. Owned by the design surface. Contract: `LOOP.md`.

## GOAL

The MVP proves one journey end to end, on a phone: a first-time visitor lands cold on any URL, is oriented, meets the 1925 offside story, follows an authored question sideways into an unfamiliar code, picks up their anchor code along the way, sees where they've been (the trail), and can watch episode one instead of reading it. (`docs/one-game-many-codes-mvp-design-brief.md` §1.)

## CONSTRAINTS

- Static site generated from a typed content repository under `/content/`; entity schemas and field names per MVP brief §3 are normative.
- Pages render without JavaScript; anchor code, trail and search are `localStorage`/client enhancements.
- No accounts, no server-side state, no CMS. Deploy target: Cloudflare.
- Build-time content lint per MVP brief §7, blocking from day one.
- Rendered output never contains internal vocabulary: `tier`, `lens`, `Layer`, `gameplay lens`, `fan lens`.
- Rule-page lens headings, exact strings: `On the pitch`, `In the stands`.
- British English interface copy; code colour never the sole signal; WCAG AA; reduced-motion respected.
- Seed facts drafted by CC carry `verified: false` until the author's verification pass; the build reports the count.

## DECISIONS

1. Title: "One Game, Many Codes". The genome metaphor survives only as the Game DNA feature name.
2. Canonical entry: the 1925 offside change — homepage default question for first visits, episode 1, first page authored.
3. Episode cadence: weekly; scripts banked ahead; narration recorded in question-sized segments, batched.
4. Language: British English source, "from the UK, to the world", origin-is-not-ownership stance (content brief §7).
5. Two consequence lenses (pitch/stands), never conflated; enforced by lint; invisible to readers.
6. Architecture is repository-first: pages are views over `/content/` entities; the podcast is a traversal (production model).
7. MVP scope is the vertical slice per MVP brief §§1, 4, 8; explicitly out of scope per §9: Map graph view, genome cards/DNA data, Compare, audio syndication, localisation, full episode slate, gamification, accounts.
8. Loop write path: DESIGN.md updates travel design-surface → RCNX asset page (namespace `ogmc`, slug `loop-round-N-design`) → CC → verbatim commit prefixed `design:` (LOOP.md amendment, 2026-08-13).
9. Transport ingest unescape: CC decodes exactly five HTML entities — those for the characters < > " ' & — on ingest of each design page, amp decoded last, then commits; delivered files never contain literal entity strings; design surface verifies by GitHub diff. (Resolves Q1-d; LOOP.md Amendment 2.1.)
10. Branch/merge lifecycle: on author sign-off the accepted round PR merges to `main` (author merges or instructs CC; design surface cannot); next DESIGN.md publishes after merge; CC branches `design/round-(N+1)` from updated `main`. PR #1 merges on author sign-off of the round-1 design plan. (Resolves Q1-e; Amendment 2.2.)
11. Delivery finality: one slug = one finalised delivery; CC pulls only on explicit author go; corrections get a new slug. (Resolves Q1-f; Amendment 2.3.)
12. Authority split: repo is ground truth for repo facts; the asset page is authoritative for delivered content; conflicts flagged in ITERATION.md. The round-0 base-SHA discrepancy (seed `dd6b457` vs actual `ec35394`) is confirmed benign; no re-seed. (Resolves Q1-g and Q0-a; Amendment 2.4.)
13. Ratified: commit hygiene per Amendment 2.5 — `design:` commits trailer-free and byte-verbatim, CC commits carry trailers, per-round ITERATION.md entries live on their branch until merge (Q1-h). `the-football-genome-content-brief-v2.md` stays out of the repo per CURRENT SPEC (Q0-b). OQ3 and OQ4 are closed as answered in ITERATION.md round 1.

## OPEN QUESTIONS

- OQ1 (author, re-asked): episode 1 `video_url` is pending the author's recording — is a placeholder acceptable through MVP acceptance, or should acceptance wait for the real embed?
- OQ2 (author, re-asked): deploy target within the Cloudflare estate — a subdomain of rcnx.io, a fresh zone, or *.pages.dev for the MVP?
- OQ5 (author; was Q1-a): sign off the nine code `colour` values in `design-plan/design-plan.md` §1. Design-surface review: recommend accept as-is — all nine clear WCAG AA both as white-on-fill chips and as text on the light surface, and the wayfinding-not-flags rationale upholds DECISION 4. One taste note only: Gaelic `#1D6FB8` sits hue-adjacent to the rugby indigo–violet band despite not being rugby-family; the always-present name disambiguates — change only if it grates.
- OQ6 (author; was Q1-b): confirm the type system — display `Fraunces`, body `IBM Plex Sans`, apparatus `IBM Plex Mono`, all SIL OFL, self-hosted at build. Design-surface review: recommend accept.
- OQ7 (author; was Q1-c): statute card framing — code-neutral (ink on paper, code named by a small chip) versus tinted in the owning code's colour. Design-surface review: recommend code-neutral as delivered — the law is the shared origin; colour marks what the codes did with it. The unverified-quote discipline is required either way.

## CURRENT SPEC

Operative spec: `docs/one-game-many-codes-mvp-design-brief.md`. Intent context: `docs/one-game-many-codes-content-brief-v3.md` (v3.1), `docs/the-football-genome-navigation.md`, `docs/the-football-genome-navigation-adversarial-review.md`, `docs/one-game-many-codes-production-model.md`. On merge of PR #1, `design-plan/design-plan.md` and `design-plan/preview.html` join the operative spec as the visual system. Where DESIGN.md and docs conflict, DECISIONS here win. Round 1 reviewed; round-2 build scope on resolution of OQ5–OQ7: the deep-entry header, the 1925 experiment page (statute-card debut), and the possession-limits rule page.
