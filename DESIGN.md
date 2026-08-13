# DESIGN.md — One Game, Many Codes

Round 0. Owned by the design surface. Contract: `LOOP.md`.

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

## OPEN QUESTIONS

- OQ1 (author): episode 1 `video_url` is pending the author's recording — is a placeholder acceptable through MVP acceptance, or should acceptance wait for the real embed?
- OQ2 (author): deploy target within the Cloudflare estate — a subdomain of rcnx.io, a fresh zone, or *.pages.dev for the MVP?
- OQ3 (CC, round 1): present the design plan (palette incl. the nine code colours, type choices, the law-text signature treatment) as artefacts in the round-1 branch BEFORE building pages, for author sign-off. Confirm or push back.
- OQ4 (CC, round 1): confirm local history reconciled with origin/main and `docs/` pushed; note the commit SHAs in ITERATION.md.

## CURRENT SPEC

Operative spec: `docs/one-game-many-codes-mvp-design-brief.md`. Intent context: `docs/one-game-many-codes-content-brief-v3.md` (v3.1), `docs/the-football-genome-navigation.md`, `docs/the-football-genome-navigation-adversarial-review.md`, `docs/one-game-many-codes-production-model.md`. Where DESIGN.md and docs conflict, DECISIONS here win. Round 0: no implementation reviewed yet; first review follows `design/round-1`.
