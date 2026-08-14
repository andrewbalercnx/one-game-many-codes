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

### Process questions — lock before round 2 (transport mechanics, not content)

These concern the design↔CC transport only. Round 0/1 avoided them because the seed was hand-built to; round 2 is the first live `DESIGN.md` delivery and Q1-d/Q1-e can silently corrupt or fragment it. Recommended locks below; if adopted, they belong in a `LOOP.md` amendment (design surface publishes as an asset, CC commits verbatim).

- **Q1-d (escaping — corruption risk, highest).** The asset body returns HTML-escaped: round 0's markers arrived as `---8&lt;---`, and the seed engineered the file bodies to contain no angle brackets. The next `DESIGN.md` has no such guarantee — any `<`, `>`, or bare `&` would be committed as `&lt;`/`&amp;` under a verbatim rule and corrupt the file. **Recommended lock:** CC HTML-unescapes a defined set on ingest — `&lt; &gt; &amp; &quot; &#39;` — then commits; the design surface confirms by diffing `DESIGN.md` on GitHub. Unicode punctuation (curly quotes, em-dashes, →) is unaffected.
- **Q1-e (branch/merge lifecycle — fragmentation risk).** The round-1 design-plan artefacts live only on unmerged `design/round-1`; `main` lacks them. The design surface is read-only on GitHub (`403 Resource not accessible by integration`) and cannot merge. **Recommended lock:** on author sign-off, the accepted PR merges to `main` (author in the GitHub UI, or author instructs CC to merge), then the design surface publishes the next `DESIGN.md`, then CC branches `design/round-(N+1)` from the updated `main`. Keeps `main` the single accumulating truth and the site deployable from it.
- **Q1-f (ready-to-pull signal — mid-edit race).** RCNX asset pages are live on every write (no draft/commit). CC pulling `loop-round-2-design` mid-edit would commit a half-written `DESIGN.md`. **Recommended lock:** one slug = one finalised delivery; CC pulls only on an explicit author go; corrections get a new slug, never a silent edit of the same page.
- **Q1-g (repo-vs-asset authority — ratify).** Seed asserted base SHA `dd6b457`; actual was `ec35394` (Round 0, deviation 1). **Recommended lock:** the repo is ground truth for facts about the repo (SHAs, paths, merge state); the asset is authoritative for `DESIGN.md` content. On conflict CC trusts the repo for facts, commits content verbatim, and flags the mismatch here.
- **Q1-h (minor ratifications).** (i) `design:` commits stay trailer-free and verbatim so the design surface can byte-diff asset vs commit; CC-authored commits carry trailers. (ii) Un-merged round branches are the design surface's review surface, so per-round `ITERATION.md` entries live on their branches until merge (Q1-e resolves consolidation).

---

## Round 1 – 2026-08-13 (design delivery committed to `main`)

- Author go received. **Sign-offs recorded** (to be folded into DECISIONS at the next design commit): OQ5 accepted — the nine code `colour` values as-is (was Q1-a); OQ6 accepted — `Fraunces` / `IBM Plex Sans` / `IBM Plex Mono` (was Q1-b); OQ7 accepted — statute card stays code-neutral (was Q1-c).
- **PR #1 merged to `main`** by author instruction (Amendment 2.2; design surface is read-only and cannot merge): merge commit `baa292f9e141d4035b157ac3aafd121a265054b9`. `design-plan/design-plan.md` and `design-plan/preview.html` are now on `main`.
- **Design delivery ingested** from RCNX asset `ogmc/loop-round-1-design`, applying the Amendment 2.1 unescape (decode `lt gt quot #39` then `amp` last, single pass each). Post-unescape residual-entity scan: none.
- **Committed to `main`** (both `design:`, trailer-free, byte-verbatim):
  - `design: LOOP.md amendment 2 (transport locks)` — `0fef2e7e0b0c539bfaec818d08bc277fc0fabd86` (appended LOOP.md Amendment 2, five transport locks).
  - `design: DESIGN.md round 1` — `897037ecd9c69deae2e4dcb64fd516d3636a0a43` (full replacement; DESIGN.md now Round 1, DECISIONS 9–13 added, OQ3/OQ4 closed, OQ5–OQ7 carried).
- **Byte-diff confirmation:** committed `DESIGN.md` sha256 `be8dc2d2ec7acdcbfd56bf014a9f9503649052523212da7a7bf09806c05473c6` equals an independent unescape of the asset body (byte-identical). LOOP.md Amendment 2 appendix (post-unescape) sha256 `139a8cd39e286897e921dfc966b2b7911d358723970c0498525d891c56ca8dcf`. The design surface can verify by diffing both files on GitHub against the asset page post-unescape.
- Deviations: none.
- Answers: OQ5/OQ6/OQ7 accepted (above). **OQ1 and OQ2 remain OPEN** — placeholder `video_url` and `*.pages.dev` are NOT decided; the round-2 build will assume neither (no video embed committed as final; no deploy target wired).
- Blocked: none. Round-2 build (deep-entry header, 1925 experiment page, possession-limits rule page) proceeds on branch `design/round-2` off `main`.

---

## Round 2 – 2026-08-13 (build)

- Branch: `design/round-2` off `main` (`f136f37`). PR against `main`, not merged — design surface reviews.
- Done — the authorised slice, built as views over `/content/` (DECISION 6):
  - **Build pipeline:** `build/build.py` (zero-dependency Python 3 + PyYAML) + `Makefile` (`make build`). Renders to `dist/`, runs a blocking lint first.
  - **Design system:** `assets/site.css` — the signed-off palette (nine `--c-*` code colours), type (`Fraunces` / `IBM Plex Sans` / `IBM Plex Mono`) and the code-neutral statute card. Inlined into each page (self-contained; no runtime CDN).
  - **Content entities:** 9 codes (`content/codes/`, full body for `soccer` + `rugby-league`, frontmatter stubs for the other 7), `dimensions/possession-limits.md`, `events/1925-offside-two-defenders.md` (`experiment: true`), 5 claims (`content/claims/`), 4 sources (`content/sources/`).
  - **Rendered pages** (`dist/`): `1925-offside-two-defenders.html` (deep-entry header + statute card after `## The change` + prompt chips), `possession-limits.html` (colour-marked positions strip + `## On the pitch` / `## In the stands` + prompts), `index.html` (placeholder landing).
  - **Deep-entry header** on every page: code colour spine + code name (colour never sole signal) + question/title + "part of One Game, Many Codes" link.
- Applied sign-offs: OQ5 (nine colours), OQ6 (type system), OQ7 (statute card code-neutral).
- Deviations:
  1. Generator is Python 3 + PyYAML, not Node — output is static HTML, so the build language is invisible to Cloudflare; boring and zero-install here. Revisit if the author prefers Node/an SSG (Q2-b).
  2. Fonts not yet vendored: `assets/site.css` names the three faces with fallback stacks; no runtime CDN is used (constraint honoured), so pages currently render in fallback faces. WOFF2 self-hosting is a follow-up (Q2-a).
  3. Added `index.html` beyond the three-item scope, solely so the header's site link resolves and the slice is browsable/deployable. It is not the designed Home (MVP brief §4.1) — that is a later round.
  4. `dist/` (generated) is committed so the design surface can review rendered output on GitHub (it cannot build). Regenerated by `make build` (Q2-c).
  5. Lint implements the round-relevant subset of MVP brief §7 (tier-1 source; stands-not-only-match_data; content-page-needs-prompt; dimension lens headings; internal-vocabulary in output; dead internal links). Clip/edge/action checks are present but inert (no such entities yet).
- Answers / acceptance evidence:
  - Build is green: `Build OK — 3 pages`. Unverified count reported: `Unverified facts flagged (verified: false): 20`.
  - Lint blocks (criterion 5): three negative tests each aborted the build — dropped `## In the stands` → `dimension possession-limits: missing '## In the stands'`; injected `Layer 4` → `possession-limits.html: rendered output contains internal vocabulary 'Layer'`; broken prompt target → `1925-offside-two-defenders.html: dead link does-not-exist.html`.
  - Journey (criterion 3, middle segment): `index.html` → `1925-offside-two-defenders.html` → prompt → `possession-limits.html`, all links resolve; the rule page's own prompt returns to the 1925 story and to its `#on-the-pitch` anchor.
  - OQ1/OQ2 respected: no final video embed committed; no deploy target wired (no `*.pages.dev` assumed).
- Blocked / questions for the design surface:
  - Q2-a: OK to vendor the OFL WOFF2 files into `assets/fonts/` next round (satisfies self-hosted-fonts constraint)?
  - Q2-b: is the Python 3 + PyYAML generator acceptable, or is Node/an SSG preferred before the site grows?
  - Q2-c: keep committing generated `dist/` for review, or gitignore it once a preview deploy exists?
  - OQ1 and OQ2 remain author-owned and open; anchor/trail/search behaviours (MVP §5) and code/experiment page expansion are the natural round-3 scope.

---

## Round 2c – 2026-08-14 (design delivery + claims channel, committed to `main`)

- Author go received. **PR #2 merged to `main`** (three review notes carried to round 3): merge commit `ad5e595bc51538f8ea57676919d5770807dbbf82`.
- Consumed asset `ogmc/loop-round-2-design-c` (**supersedes `-design` and `-b`, which were ignored**), `ogmc/loop-amendment-3-claims-protocol`, and `ogmc/claims-batch-1`. All ingested with the Amendment 2.1 unescape; residual-entity scan clean on every file.
- **Committed to `main`** (all `design:`, trailer-free, byte-verbatim), in the mandated order:
  - `design: DESIGN.md round 2` — `b129b4b5dae4fa8ba51008799a45a7b14695d3b3`. DESIGN.md now Round 2 (GOAL redefined to a launchable framing site + full Stage-1 skeleton; DECISIONS 14–20; OQ5/6/7 resolved; OQ9/OQ10 open). sha256 `6a3916169a8f709b7709f982a9ce267125f2d923857c48f37abe2ff471d1ea98`.
  - `design: content note — the ball dimension and episode 1` — `a3d7d17df39666ab5c1c6930fa5772a4c82405f2` (`docs/the-ball-and-episode-1.md`). sha256 `c8d750b24f505472f3694cfc58fdfb780051b2d802ac31362deada8f6413386c`.
  - `design: LOOP.md amendment 3 (claims channel)` — `f5ba3c2d63ba3879cc7741ac94405a9ed9b3fae6`. Appended Amendment 3 (four clauses: ledger + INDEX + lint additions; batch transport; consumption; verification stays the author's). Appendix sha256 `f2864f8e43bc8858a5bf534084617ea07413de65791c2f8156e236f924b39456`.
  - `design: claims batch 1 (7 claims, 4 sources)` — `04f4eb90dca7a988970ebbb25cb211421ed14e47`. **Batch 1 consumed.**
- **Byte-diff confirmation:** each committed file's sha256 (above) equals an independent unescape of its asset body. Claims/sources contained no HTML entities, so verbatim equals post-unescape (confirmed by residual-entity scan). The design surface can verify by diffing on GitHub.
- **Claims batch 1 file ids** — claims: `ball-shape-is-statute`, `kicked-ball-outruns-any-runner`, `sphere-rolls-true`, `oval-bounce-rewards-carrying`, `adoption-compounds`, `gaelic-control-case`, `american-ball-sharpened-post-1906`; sources: `ifab-law-2-the-ball` (law_text), `bolt-berlin-2009-splits` (match_data), `instep-kick-velocity-literature` (paper), `tfa-fastest-shots-2021` (press). All `verified: false`, `proposed_by: design`, `batch: 1`.
- Verification: existing round-2 lint still green after the batch — `Build OK — 3 pages`, unverified count now `27`. `dist/` unchanged (round-2 pages untouched).
- Deviations: none. The Amendment 3 storage items (INDEX.md generation, provenance/ceiling lint additions) are round-3 build work per the amendment, not yet implemented on `main`; they land on `design/round-3`.
- Next: branch `design/round-3` off `main`; round-3 scope per the round-2c CURRENT SPEC. Domain attachment to `manycodes.games` is NOT authorised (launch only).

---

## Round 3 – 2026-08-14 (build, increment 1: OQ10 checkpoint + claims channel)

- Branch: `design/round-3` off `main` (`6fc119b`). PR against `main`, not merged.
- **Scope of this increment.** OQ10 instructs the stub template be shown as a rendered example *before* stamping out all 22 stubs. So increment 1 delivers the template-first checkpoint plus the normative Amendment 3 storage; the rest of round 3 (below) follows OQ10 sign-off.
- Done:
  - **Base-URL config (DECISION 19):** `site.config.json` — single source of `base_url` (empty ⇒ relative links until the Pages preview). The build reads it; no absolute site URLs are hardcoded.
  - **Claims channel storage (Amendment 3.1, normative):** the build now parses each source's `Ceiling: tier N` and `Status:` lines and regenerates **`content/INDEX.md`** every build — `id | lens | tier | verified | from -> to | source ids` per claim, `id | type | ceiling | status` per source (12 claims, 8 sources). New blocking lint rules: a claim citing a missing source id; a tier-1/tier-2 claim whose only sources are press-ceiling; `verified: true` on a claim whose `proposed_by` is not `author`. Prior lint retained.
  - **OQ10 stub template:** `build_stub` renders question + one-paragraph promise + honest "coming" state + one onward prompt. One example rendered — `dist/stub-example.html` (the `rugby-union` code stub). The remaining 21 stubs are NOT stamped pending sign-off.
  - **OQ9 manifesto placeholder:** `content/pages/manifesto.md` carries a clearly-marked `BEGIN-AUTHOR-COPY … END-AUTHOR-COPY` block — the author's copy goes in verbatim; I did not draft manifesto prose. `dist/index.html` is now the manifesto home: the placeholder banner + the episode-1 teaser ("Why did one football conquer the world?", weekly — DECISION 20) + a link into the skeleton. The round-2 pages remain buildable but are UNLINKED from the launch surface (DECISION 17e).
- Deviations:
  1. Round 3 is delivered in increments; increment 1 is the OQ10 checkpoint. **Deferred to increment 2+ (on sign-off):** the remaining 21 stubs, the Map tree view from the edge set, ~100 dated events, the edge set with confidence markers, the timeline index, dimension 13 "The ball" data, the Cloudflare Pages project + `*.pages.dev` preview + base-URL wiring + `gitignore dist/` (DECISION 18c/19), and OFL font vendoring (DECISION 18a).
  2. `base_url` is empty (relative links) until the Pages preview URL exists.
  3. Domain attachment to `manycodes.games` NOT performed — launch only, per author.
- Answers / acceptance evidence:
  - Build green — `Build OK — 4 pages`; `content/INDEX.md regenerated (12 claims, 8 sources)`; unverified count `28`.
  - New lint blocks (negative tests, each aborted the build): `verified:true requires proposed_by author`; `cites missing source id 'does-not-exist-source'`; `tier-2 claim whose only sources are press-ceiling`.
- Blocked / questions for the design surface:
  - **OQ10 — sign off `dist/stub-example.html`** (the stub template) so I can stamp the remaining 21 stubs.
  - The **three round-2 review notes** carried to round 3: please restate them on the branch (or confirm they are the already-tracked Q2-a font vendoring / Q2-b Python generator / Q2-c `dist/` items) so I address the intended ones.
  - **Deploy (DECISION 19):** the Cloudflare Pages project needs Cloudflare access (the Cloudflare MCP currently requires authorisation). Should I stand up the Pages project once that's authorised, or will the author create it and hand me the `*.pages.dev` preview URL for the `base_url` value?
