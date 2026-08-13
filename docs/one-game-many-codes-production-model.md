# One Game, Many Codes
## Content production model – building the repository, deriving the podcast

This sits under the content brief (v3.1). The brief says what the site contains and why; this document says how that content gets made, and how the same material then generates the weekly series. It stays at content level – the entity model below is an editorial structure, not a database design, though it will map onto one naturally when the build side picks it up.

---

# 1. The reframe: pages are views, the repository is the product

The brief describes the site as pages – rule pages, code pages, experiment pages. But almost everything on those pages is assembled from a small set of underlying units that each appear in many places. The 1966 limited-tackle rule appears on the possession-limits rule page, the league code page, its own experiment page, the timeline, two consequence chains and an episode. Written six times as prose, it will drift into six slightly different versions with six sourcing standards. Written once as a repository entry and assembled six times, it can't.

So the production model inverts the intuitive order: **the repository is what gets built; the pages are views over it; the podcast is a traversal of it.** This isn't an engineering nicety – it's what makes the editorial disciplines in the brief enforceable. Lens separation, evidence tiers, source citation and confidence markers all become fields on entries rather than conventions authors must remember, which means they can be audited mechanically instead of hoped for.

It also makes the podcast nearly free at the margin. Every episode fact already exists as a sourced entry; the marginal cost of an episode is script, recording and edit – never research.

---

# 2. The units

Eight entity types cover the whole site. Fields listed are editorial, not exhaustive.

**Codes** (9 + ancestors + satellites). Name, colour, one-sentence genome, bridge lines to each other first-class code, status (first-class / second-class / satellite / ancestor).

**Rule dimensions** (12 at launch). The question it answers, and a **position per code** – each position being the rule as that code states it, with the law citation. The rule page is this entity plus its claims.

**Events** (~80–120). Dated rule changes and splits. Date, code, what changed (quoted where short), why introduced, source. The timeline is the event set; each Natural Experiment page is one event promoted to a full story.

**Claims** – the heart of the repository, and the site's real asset. One causal assertion per entry:

> *statement* · *from* (rule position or event) · *to* (phenomenon) · **lens** (pitch / stands) · **tier** (1 / 2 / 3) · *sources* · *confounds, if any*

Example entry: "Limited tackles made possession finite, which made tactical kicking rational" · from: possession-limits/league · to: kick-on-the-last · lens: pitch · tier: 2 · sources: [law text 1966; match-data refs] · confounds: none stated. A consequence chain is an ordered sequence of claim entries. A rule page's two lens sections are its claims filtered by lens. The three-points experiment page is its event plus the claims that *failed*, tiered and sourced like any others.

**Actions** (40–50). The glossary: definition, the rule position that makes it exist, misconception, sibling links (shared inheritance, with the ancestor rule named), clip reference, closing door.

**Edges**. Descent and influence links between codes, each carrying confidence (established / probable / contested) and its evidence note. The Map is the edge set rendered.

**Sources**. Law texts, papers, match-data sets, each entered once and cited by ID from claims, events and DNA scores – so when a source is superseded, every dependent entry is findable in one query.

**Clips**. The media inventory: concept illustrated, rights status, annotation text ("which rule made this happen"), paired fallback diagram, last-checked date. The annotation text is deliberately double-duty – it is also narration script (§6).

Everything else on the site is composition. Compare was already defined as a view in the brief; under this model, *every* page is.

---

# 3. Build sequence

Five stages, ordered so that each one makes the next cheaper. This refines the brief's §11 ordering rather than replacing it.

**Stage 1 – the skeleton (fast, forcing).** Enter the codes, the twelve dimensions with their per-code positions, the event list, and the edge list with confidence markers. This is mostly transcription from the historical record and can be drafted quickly – but it forces every canon and historiography decision early, while changing them is cheap. The Map and timeline become viewable from this stage alone.

**Stage 2 – the claims ledger (slow, valuable).** The real work. Every causal assertion the site will ever make, entered with lens, tier, sources and confounds – starting with the seven Natural Experiments' claims, since they carry the boldest assertions and need the best sourcing, then the launch chains, then the per-rule consequences. The ledger is where the fan-lens literature gets read properly and where the site's credibility is actually earned; a weak ledger cannot be rescued by good prose. Expect this stage to surface claims the brief assumed that the evidence won't support – deleting those here costs nothing, discovering them post-publication costs outcome 2.

**Stage 3 – the prose.** Pages written over the ledger: the "what changed" narratives, citing ledger entries rather than re-asserting facts. Order per the brief: 1925 first, experiments and Map annotations, then rule pages, then code pages (which by now are mostly assembly), glossary continuously. Every page passes the tellability test on completion – if it can't be read aloud as cause and effect, it goes back.

**Stage 4 – the media.** One clip per concept sourced and annotated, fallback diagram made, rights and region status recorded. This can overlap stage 3 and should trail it slightly, because the prose determines which concepts actually need illustrating.

**Stage 5 – the numbers.** DNA scores computed from sourced match data, methodology page written, cards switched on. Last, as the brief orders, so data sourcing never blocks prose.

**Quality gates.** Two, both cheap because of the fields: a mechanical audit (every tier-1 claim has a primary source; no stands-lens claim cites only pitch-lens evidence; every contested edge has its note; every clip has a live fallback) and a hostile read of each experiment page by someone who knows that code's history – the same adversarial method that produced the navigation model, applied per page.

---

# 4. From repository to podcast

An episode is a **traversal**: one question, a path through claims, events and clips, one payoff, one closing question. Because the repository stores the links, candidate traversals can be enumerated rather than invented – any chain of claims from a rule to a phenomenon that crosses a payoff (a sibling-action reveal, a before/after number) is a potential episode, and the strongest ones are exactly the pages the brief already promoted to the slate.

**The script pipeline**, per episode:

1. The finished page is beaten out into question-sized segments – typically four to six beats: the hook question, the world before, the change, what happened next, the payoff, the closing question.
2. Each beat's facts come verbatim-in-substance from ledger entries (so every spoken claim inherits its tier and sources – the transcript can carry the citations even though the voice doesn't).
3. The script is written for the author's spoken register per the brief's voice rules, one idea per beat, and read aloud once before it's considered done.
4. Beats are recorded as separate segments in batched sessions – several episodes' segments per session – per the brief's §9 survival conditions for weekly cadence.
5. The edit assembles narration + clips + fallback diagrams + simple on-screen text; the audio derivative is cut from the same edit; the transcript publishes onto the source page.

A correction anywhere in the ledger flags every dependent beat, which is what makes a weekly show maintainable by one presenter: fixes are re-recorded as single segments, not episodes.

**Season design.** The repository's prompt-links let the season be sequenced as a literal path: each episode's closing question is the next episode's title. Season one is the entry arc –

1. *How did one line in the law book change football forever?* (1925 offside – the canonical entry)
2. → *Could a rule ever make players give the ball away on purpose?* (1966 limited tackles)
3. → *What happens when a rule is meant to fix boring football and fails?* (three points for a win – the counter-case, placed early to establish honesty)
4. → *Can a safety rule invent a whole new sport?* (1906 forward pass)
5. → *Why did goalkeepers suddenly have to learn to play?* (1992 back-pass)
6. → *What if you just halved the players?* (sevens)
7. → *Who decided footballers should only play offence or defence?* (free substitution)

– then into the flagship chains, with the fossil reveal (mark/fair catch) held back as a mid-season payoff episode. The exact question phrasings are drafting; the structural point is that the season order is a walk through the question graph, so a viewer who binges experiences the same lateral journey the site's browse mode is designed to produce.

**Recurring segments**, each mapping to a repository type so they never need bespoke research: *the fossil* (a sibling-action reveal from the glossary), *the counter-case* (claims where evidence beat intention), and *what just changed* (a short beat from the evolution updates – the weekly cadence's renewable fuel, since the real world supplies new events on its own schedule).

---

# 5. Worked example: episode one from the repository

*How did one line in the law book change football forever?*

- **Hook** (script only): a First Division fan in 1924 watches a 0–0 grind; the same fan in 1926 watches goals rain. Nothing about the players changed.
- **The world before** ← event entry: the three-defender offside law; claims about the offside-trap strangle, tier 1, sourced.
- **The change** ← event entry: 1925, three becomes two; the law text quoted on screen.
- **What happened next** ← claims: goals up roughly a third in a season (tier 1, the season data on screen); the trap collapses.
- **The payoff** ← claim: Chapman invents the WM as the *defensive counter-move* – the reveal that rule changes trigger arms races, which is the thesis of the entire site delivered inside one story.
- **The closing question** → "so could a rule ever make teams give the ball away on purpose?" – the door to episode two, and on-site, the door into the possession-limits rule page.

Six beats, five repository entries, two clips, one diagram, under ten minutes. Everything spoken is cited in the transcript; nothing was researched for the episode itself.

---

# 6. What the model buys

Consistency: every fact lives once, so six appearances can't drift into six versions. Auditability: the brief's editorial disciplines become checkable fields. Localisation: translating the repository translates the site, and the from-the-UK-outward policy applies to entries, not to page-by-page rework. Corrections: one fix propagates to every page and flags every recorded segment it touches. And the economics that make a weekly, single-presenter series plausible at all: by the time episode one is recorded, its research cost is already sunk in the repository – the show spends its budget on telling, not finding out.
