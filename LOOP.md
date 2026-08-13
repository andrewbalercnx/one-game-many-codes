# LOOP.md — the design↔implementation contract

This repo mediates a two-surface loop:

- **Design surface** (Claude web, with the author): owns `DESIGN.md` on `main`.
- **Implementation surface** (Claude Code): owns `ITERATION.md` (append-only log of rounds) and implements on branches named `design/round-N`.

## DESIGN.md structure (fixed sections)

1. **GOAL**
2. **CONSTRAINTS**
3. **DECISIONS** — numbered, append-only
4. **OPEN QUESTIONS**
5. **CURRENT SPEC**

## Each round

1. Design surface reads `ITERATION.md`'s latest entry and the diff of the newest `design/round-N` branch or PR.
2. Design surface discusses with the author, then updates `DESIGN.md`: agreed items are folded into DECISIONS with a number; nothing in OPEN QUESTIONS is answered by the design surface itself — each is resolved (by the author or by a numbered decision) or re-asked.
3. Deltas stay small. Sections that didn't change aren't rewritten.

## Rules

- Designs are never carried between surfaces via chat; both surfaces work through this repo and the `ogmc` asset namespace (write-path amendment below).
- **Lossless on identifiers, error strings, numbers, and file paths. Lossy is fine on prose.**
- DECISIONS is append-only: superseding a decision means a new numbered decision that names the one it replaces, never an edit.
- `ITERATION.md` is append-only; each round's entry records what was built, what deviated from `DESIGN.md` and why, and questions for the design surface.

## Write-path amendment (2026-08-13)

The design surface's GitHub connector is read-only on repo contents (`403 Resource not accessible by integration` on writes; reads work). Therefore:

- The design surface authors `DESIGN.md` updates and publishes each one as an RCNX asset page: namespace `ogmc`, slug pattern `loop-round-N-design` (this seed: `loop-round-0-seed`).
- CC reads the page (RCNX MCP `list_asset_blocks` + `get_asset_block` on namespace `ogmc`, or the public page at rcnx.io/assets/ogmc/{slug}) and commits the contained `DESIGN.md` to `main` **verbatim**, commit message prefixed `design:`.
- Authorship and ownership of `DESIGN.md` remain with the design surface; CC's commit is a mechanical act.
- CC → design surface travels through the repo itself: `ITERATION.md` and `design/round-N` branches, which the design surface reads directly via GitHub. No return objects needed.

## Repo facts

- Remote: `andrewbalercnx/one-game-many-codes` (private).
- Operative spec docs live under `docs/`.
- Design-delivery surface: RCNX asset pages, namespace `ogmc`, slug prefix `loop-`.
