# ITERATION.md — implementation log

Owned by the implementation surface (Claude Code). Append-only. Contract: `LOOP.md`.

---

## Round 0 – 2026-08-13

- Branch: `main` (bootstrap round; seed instructs direct commit to `main`, no `design/round-N` branch).
- Done:
  - Repointed `origin` from `andrewbalercnx/one-game-many-codes-` (old, trailing-dash) to `andrewbalercnx/one-game-many-codes`, fetched, and reconciled local history onto `origin/main`.
  - Committed the five operative/context documents under `docs/`: `one-game-many-codes-mvp-design-brief.md`, `one-game-many-codes-content-brief-v3.md`, `the-football-genome-navigation.md`, `the-football-genome-navigation-adversarial-review.md`, `one-game-many-codes-production-model.md`.
  - Committed `LOOP.md` verbatim from asset `ogmc/loop-round-0-seed`, message `Add LOOP.md: design↔implementation contract`.
  - Committed `DESIGN.md` verbatim from the same asset, message `design: seed DESIGN.md (round 0)`.
  - Commit SHAs (on `main`, atop `ec35394`):
    - docs/ — `dc07ea58956aab55adaba73325dc912e0c6d8139`
    - LOOP.md — `8e21ff336666b9eaff0fa200bdc6fefd4c2ce46b`
    - DESIGN.md — `704cd69ba93f86a1e27b8867c0014f5ed426455f`
    - ITERATION.md (this entry) — recorded on push below.
- Deviations:
  1. **Base SHA differs from the seed.** The seed states `origin/main` is README-only at SHA `dd6b457`. The actual `origin/main` is README-only at SHA `ec35394` (`Initial commit`; `README.md` = `# one-game-many-codes`). Content matches the seed's description; only the SHA differs — consistent with the repo having been recreated during the rename. Built on the real `ec35394`.
  2. **Reconcile method.** Used `git checkout -b main origin/main` rather than `git pull --rebase origin main`, because the local branch (`claude/file-review-comments-0zjj7r`) had no commits — there was nothing to rebase; the result is identical (local `main` = `origin/main` + my commits on top).
  3. **No trailers on the two seed-specified commits.** `LOOP.md` and `DESIGN.md` were committed with exactly the seed-specified messages and no co-author/session trailers, to keep them byte-verifiable by the design surface against the asset. The `docs/` and `ITERATION.md` commits carry the standard trailers.
  4. **v2 content brief excluded.** The source archive contained six documents; `the-football-genome-content-brief-v2.md` (superseded *The Football Genome* v2.1) was not committed, matching `DESIGN.md` CURRENT SPEC, which enumerates exactly the five above.
  5. **Verbatim scope.** Transcription is lossless on identifiers, error strings, numbers and file paths (verified by grep before commit); prose apostrophes/dashes reproduce the asset's Unicode as-is. Per LOOP.md, prose is allowed to be lossy.
- Answers: none due this round (OQ3/OQ4 are answered on `design/round-1`).
- Blocked / questions for the design surface (to fold into OPEN QUESTIONS next round):
  - Q0-a: Confirm the base-SHA discrepancy (`dd6b457` in the seed vs actual `ec35394`) is benign and needs no re-seed.
  - Q0-b: Confirm `the-football-genome-content-brief-v2.md` should stay out of the repo (assumed yes, per CURRENT SPEC).

---

## Round 1 – 2026-08-13

- Branch: `design/round-1` (PR against `main`, not merged — design surface reviews).
- Done:
  - Produced the design-plan artefacts for OQ3, **before building any pages**:
    - `design-plan/design-plan.md` — the written plan (palette, type, statute card, sign-off scope).
    - `design-plan/preview.html` — self-contained visual; recomputes the palette contrast ratios in-page from the hexes.
  - Fixed the nine code `colour` values (WCAG AA verified, chip white-on-fill and colour-as-text on the light surface both ≥ 4.5:1): soccer `#157F4C` (5.03/4.68), futsal `#0F766E` (5.47/5.09), Canadian `#0E7490` (5.36/4.99), Gaelic `#1D6FB8` (5.23/4.86), rugby union `#3B4AA0` (7.86/7.31), rugby sevens `#6D28D9` (7.10/6.61), Australian rules `#A21F6E` (7.10/6.61), rugby league `#C0223B` (5.94/5.53), American football `#97590F` (5.60/5.21).
  - Fixed the type system: display `Fraunces` (questions, law quotes); body `IBM Plex Sans`; apparatus `IBM Plex Mono` — all SIL OFL, self-hosted at build.
  - Specified the law-text signature treatment (the "statute card") with a code-neutral frame and a `verified: false` / `unverified` discipline so no fabricated quote ships.
- Deviations:
  1. No pages built this round — intentional, per OQ3 ("BEFORE building any pages"). Round 1 is design-plan only.
  2. `preview.html` loads the three fonts from Google Fonts **for the preview only**, with full fallback stacks; the shipped site self-hosts them (no runtime CDN, per CONSTRAINTS). Marked in-file.
- Answers:
  1. **OQ4 — confirmed.** Local history reconciled onto `origin/main`; `docs/` pushed. `main` now at `8e9c1e06d9baba3c441ac97b927bb08f87707542`, atop `Initial commit ec35394`. Round-0 SHAs: docs `dc07ea58956aab55adaba73325dc912e0c6d8139`, LOOP.md `8e21ff336666b9eaff0fa200bdc6fefd4c2ce46b`, DESIGN.md `704cd69ba93f86a1e27b8867c0014f5ed426455f`, ITERATION.md `8e9c1e06d9baba3c441ac97b927bb08f87707542`. Note: actual base SHA is `ec35394`, not the seed's `dd6b457` (see Round 0, deviation 1).
  2. **OQ3 — confirmed, no push-back.** Design-first is correct: the palette, type and statute card are cross-page dependencies; settling them once avoids per-page drift and re-work. Delivered as the two artefacts above for author sign-off. On sign-off, round 2 can build the deep-entry header, the 1925 experiment page (statute-card debut) and the possession-limits rule page against a settled system.
- Blocked / questions for the design surface (to fold into OPEN QUESTIONS next round):
  - Q1-a: Sign off the nine `colour` values as-is, or request adjustments? These become the `colour` field on each Code entity.
  - Q1-b: Confirm the `Fraunces` / `IBM Plex Sans` / `IBM Plex Mono` type system.
  - Q1-c: The statute card is code-neutral (ink on paper, code named only by a small chip). Confirm that reading, versus tinting the card in the owning code's colour.
