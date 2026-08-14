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

## Amendment 2 (2026-08-13) — transport locks

1. **Ingest unescape (lossless rule).** Asset-page bodies arrive HTML-escaped, and the store also normalises entity text, so literal entity strings do NOT round-trip — delivered files must never contain them (name the character instead). On ingest of any `loop-round-N-design` page, CC decodes exactly five entities — those encoding the characters < > " ' & (entity names: lt, gt, quot, #39, amp) — single pass each, with amp decoded LAST to prevent double-decoding. Then commit. The design surface verifies by diffing the committed file on GitHub.
2. **Branch/merge lifecycle.** On author sign-off, the accepted round PR merges to `main` (author merges in the GitHub UI, or explicitly instructs CC — the design surface is read-only and cannot merge). The next `DESIGN.md` publishes after merge; CC branches `design/round-(N+1)` from the updated `main`. `main` is the single accumulating truth and stays deployable.
3. **Delivery finality.** One slug = one finalised delivery. CC pulls a design page only on an explicit author go. Corrections are a new slug, never a silent edit of an existing page.
4. **Authority split.** The repo is ground truth for repo facts (SHAs, paths, merge state); the asset page is authoritative for delivered file content. On conflict, CC trusts the repo for facts, commits content verbatim, and flags the mismatch in `ITERATION.md`.
5. **Commit hygiene.** `design:` commits are trailer-free and byte-verbatim (post-unescape) so the design surface can diff asset against commit; CC-authored commits carry standard trailers. Per-round `ITERATION.md` entries live on their round branch until merge.

## Amendment 3 (2026-08-14) — the claims channel

1. **Claims ledger — location and queryability.** All causal claims live at `content/claims/`, one file per claim, schema per MVP brief §3 plus provenance fields: `proposed_by` (design | cc | author), `batch` (integer, present on design-proposed claims), `verified` (false until the author flips it — ONLY the author flips it). Sources live at `content/sources/` per §3, and every source body carries a **Ceiling** line: the strongest claim tier this source can support on its own (press-type sources cannot alone carry tier 1 or tier 2). The build regenerates `content/INDEX.md` — one line per claim (`id | lens | tier | verified | from -> to | source ids`) and one line per source (`id | type | ceiling | status`) — committed with every build, so the design surface can read the entire ledger in a single file on GitHub. Lint additions, blocking: a claim citing a missing source id; a tier-1 or tier-2 claim whose only sources are press-ceiling; a `verified: true` on any claim whose provenance is not author; a stale `INDEX.md`.
2. **Design → CC claims transport.** New claims and sources from the design surface arrive as RCNX asset pages, namespace `ogmc`, slug pattern `claims-batch-N`, N strictly sequential. One published page = one finalised batch (Amendment 2.3 finality applies; corrections are a new batch, never an edit of a published one). Each batch lists complete files — repo path plus full frontmatter and body — to be committed VERBATIM after the Amendment 2.1 unescape. Batches never set `verified: true`.
3. **Consumption.** CC consumes every unconsumed batch, in batch order: (a) at the start of each round, and (b) on any author go that mentions claims. Commit message per batch: `design: claims batch N (…)`. Run the lint; log the consumed batch numbers and the file ids in `ITERATION.md`. The design surface reads `content/INDEX.md` and the files directly on GitHub; no return channel is needed.
4. **Verification stays the author's.** The author's sourcing pass is the only mechanism that sets `verified: true`; design batches propose, the lint enforces, the author confirms.
