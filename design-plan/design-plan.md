# Design plan — One Game, Many Codes (round 1)

Status: **for author sign-off, before any pages are built.** This is the OQ3
deliverable. It fixes the three things every page will depend on — the code
palette, the type system, and the law-text signature treatment — so those
decisions are made once and not relitigated per page.

Companion artefact: `design-plan/preview.html` — a self-contained visual of
everything below (swatches with live contrast numbers, a type specimen, and
the statute-card mock). Open that to judge; read this for the rules.

Constraints honoured (MVP brief §6): code colour is the identity system and is
never the sole signal; the rendered law text is the signature element; a
characterful display face is used sparingly for questions and law quotes, a
highly readable face for body; British English; WCAG AA; reduced-motion; and a
deliberate swerve away from the current AI-default looks (cream + serif +
terracotta; near-black + acid accent; broadsheet hairlines).

---

## 1. Palette — the nine code colours

One fixed colour per code, doing wayfinding everywhere the code appears (Map
node, page spine, prompt chip, timeline dot, episode chapter). These are the
values for each Code entity's `colour` field (MVP brief §3).

**These are wayfinding colours, not flags.** They are chosen for mutual
distinguishability and contrast, not to echo national or club colours —
choosing by nationality would fight DECISION 4 (origin-is-not-ownership) and
collide badly (three codes would all want red). Two family relationships are
deliberately encoded in hue adjacency, which is a *bonus* cue on top of the
always-present name: the soccer family sits in green–teal (soccer, futsal), and
the rugby family sits in indigo–violet (union, sevens).

| Code | `colour` | Chip: white text on fill | As text on light surface |
|---|---|---|---|
| Association football (soccer) | `#157F4C` | 5.03:1 | 4.68:1 |
| Futsal | `#0F766E` | 5.47:1 | 5.09:1 |
| Canadian football | `#0E7490` | 5.36:1 | 4.99:1 |
| Gaelic football | `#1D6FB8` | 5.23:1 | 4.86:1 |
| Rugby union | `#3B4AA0` | 7.86:1 | 7.31:1 |
| Rugby sevens | `#6D28D9` | 7.10:1 | 6.61:1 |
| Australian rules football | `#A21F6E` | 7.10:1 | 6.61:1 |
| Rugby league | `#C0223B` | 5.94:1 | 5.53:1 |
| American football | `#97590F` | 5.60:1 | 5.21:1 |

All nine clear WCAG AA for normal text (≥ 4.5:1) **both** as a solid chip with a
white label **and** as coloured text on the light surface. Ratios are computed
with the WCAG 2.x formula; the numbers above are reproduced by
`design-plan/preview.html`, which recomputes them in-page from the hexes so the
claim is self-checking.

### Usage rules

- **Never colour alone.** A code's colour always travels with its name — chip
  = fill + white name; spine = coloured rule directly above/below the named
  page title. A colour-blind or greyscale reader loses nothing.
- **Colour lives in fills and rules, not in body text.** Long-form prose is ink
  on the light surface; the code colour appears as the page spine, prompt
  chips, and small markers. (Coloured *text* also passes AA per the table, and
  is available for short labels, but body copy stays ink for calm long reads.)
- **Prompts are chips.** Each end-of-page prompt renders as a pill in the
  destination code's colour with the code named on it, so the reader can see
  they are about to cross a boundary (navigation model §6).

### Surfaces and neutrals (the quiet palette)

The rest of the palette stays quiet so nine accents can shout.

- Light surface (default page): `#F6F7F5` — a cool chalk white. **Not cream.**
- Ink (body text): `#1A1E1C` — 15.68:1 on the light surface.
- Chalkboard (accent surface for the law card and episode hub): `#17211E`;
  white text on it is 16.50:1.
- Statute paper (the law card, §3): `#F2F3EF` — a faint cool grey, not parchment.

**Dark-surface caveat (documented, not a blocker):** on the chalkboard surface a
few code colours fall below the 3:1 graphical minimum as a hairline drawn
directly on the dark (union 2.10:1, sevens/Aussie 2.32:1). The MVP is
light-surface-first, and on the chalkboard the code identity is carried by
chips (white-on-fill, which all pass), not by hairlines — so this does not
affect the MVP. If a full dark theme is added later it needs lightened tint
variants of these five for hairline use; flagged for a future round, out of MVP
scope.

---

## 2. Typography

Three open-licence (SIL OFL) families, self-hosted at build (no third-party CDN
at runtime, per the static-site constraint). Roles:

- **Display — questions and law quotes: `Fraunces`.** A characterful variable
  serif with high optical-size contrast. Used sparingly and large: the rotating
  homepage question, page-title questions, and the quoted law line. This is the
  face that must make a single quoted sentence feel consequential.
- **Body — long-form causal prose: `IBM Plex Sans`.** A humanist sans with a
  faint engineered character that suits a site about rules and mechanisms;
  highly legible at small sizes on a phone, where the long reads actually
  happen. Body settings win any conflict with display (MVP brief §6).
- **Apparatus — source markers, law citations, data numerals: `IBM Plex Mono`.**
  Small, letterspaced, uppercase for the citation eyebrow; the "this is
  machinery / this is a reference" register. Pairs with Plex Sans by design.

Rationale against the AI-default looks: the swerve is (a) a cool chalk surface,
never cream; (b) an expressive display serif paired with an *engineered sans*
body rather than serif-on-serif broadsheet; (c) the accent system is nine coded
hues, never a single terracotta; (d) rules are deliberate single hairlines with
air around them, not a broadsheet grid of hairlines.

Sizing is fluid (`clamp()`), mobile-first: the question display scales roughly
1.6rem→2.6rem, body holds ~1.0–1.125rem with a generous measure cap for reading.

---

## 3. The law-text signature treatment — the "statute card"

The site's thesis is that small texts changed everything; the design must make
one quoted line feel like the hinge of a story. Every Natural Experiment and
every rule-fork moment renders its law text as a **statute card**:

**Anatomy (top to bottom):**

1. **Citation eyebrow** — IBM Plex Mono, uppercase, letterspaced, muted ink,
   e.g. `LAW 6 · THE FOOTBALL ASSOCIATION · 1925`, with a small code chip at
   the left so the owning code is named without colouring the law itself.
2. **The line** — the quoted law text set large in Fraunces, ink on statute
   paper (`#F2F3EF`), tight leading, generous padding. Air is the point: one
   line, lots of space, so it reads as consequential rather than as a caption.
3. **Before → after emphasis** — where a change turns on a single word, the
   changed value is shown as the swap it was: e.g. *three* → *two* defenders,
   the old value struck and the new value carried in a heavier weight. This is
   the "what changed, not what is" voice (brief §8) made typographic.
4. **Source marker** — a small mono tag linking to the `sources/` entity that
   backs the quote.

**Framing:** the card is **code-neutral** — ink on paper, not tinted — because
the law is the shared origin; the colour (divergence) is what the codes *did*
with it. The only colour on the card is the small chip in the eyebrow.

**Evidence discipline (non-negotiable, per CONSTRAINTS and the lint):** the card
never shows a fabricated verbatim quote. Until the author's verification pass,
the quoted line carries `verified: false` and the card shows a discreet
`unverified` state; the exact wording of the 1925 change must come from
`sources/fa-minutes-1925.md`. The mock in `preview.html` therefore uses a
clearly-marked *paraphrase*, not an invented statute, and labels itself
unverified — so the sign-off is on the *treatment*, not on unsourced words.

---

## 4. What sign-off covers, and what it unblocks

Signing off this plan fixes: the nine `colour` values, the three typefaces and
their roles, and the statute-card anatomy. With those fixed, the next round can
build the deep-entry header, the 1925 experiment page (the flagship, where the
statute card debuts), and the possession-limits rule page against a settled
visual system rather than inventing it per page.

Open items that ride alongside (not blocking sign-off):

- The dark-theme tint variants (§1 caveat) — deferred, out of MVP scope.
- Real law wording for the 1925 card depends on the author's sourcing pass
  (relates to OQ1's verification theme).
