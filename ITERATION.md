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
