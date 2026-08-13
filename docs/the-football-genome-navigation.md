# One Game, Many Codes
## Navigation model – v1, post adversarial review

This describes how a visitor moves through the site, at experience level. It sits under the content brief (v2.1) and inherits its vocabulary; where this document and the brief use different words for the same thing, the brief's word is the internal name and this document's word is what the visitor sees.

---

# 1. Principles

**Deep entry is the primary case.** Most visitors will not arrive at the homepage. They arrive from a search for "why does rugby have scrums", from a shared episode, from a screenshotted genome card. Every page therefore orients a cold visitor in its first screen: which code or question it belongs to, where it sits in the wider story, and one obvious next step. The homepage is a front door, not the front door.

**Questions are the navigation primitive.** The site's links are phrased as the questions they answer, not as section names. A visitor moves by curiosity, and the interface speaks curiosity's language.

**The taxonomy is invisible.** Layers, lenses, evidence tiers, confidence markers – all of it is authoring machinery. The visitor never sees the words "Layer 4", "gameplay lens" or "tier 2". Rule pages carry two plainly titled sections – **On the pitch** and **In the stands** – which are the two lenses wearing normal clothes. Evidence tiering surfaces only as the natural register of the prose ("the record shows…" vs "arguably…") plus a single small source marker per claim cluster. One metadata system in the chrome, not three.

**Every page ends with a door.** The end-of-page prompts from the brief are the site's actual navigation. They are written specifically per page ("Why doesn't rugby just adopt downs?"), never from a generic template, because templated prompts become wallpaper within three pages.

---

# 2. Wayfinding

Two devices carry all orientation, and there is no conventional breadcrumb hierarchy because the site's journeys are lateral, not hierarchical.

**Code colours.** Each code has a fixed colour used everywhere it appears – Map nodes, page headers, genome cards, compare panels, episode chapters. After a few minutes a visitor reads "green page" as "I'm in rugby league territory" without thinking about it. Colour is never the *only* signal (each surface also names the code) so the system survives colour-blindness.

**The trail.** As a visitor follows question-prompts, the questions they've followed accumulate in a compact retraceable trail – their personal path across the genome, phrased as the chain of questions they asked. Tapping any point in the trail returns there. The trail is the answer to "how did I get here?", which lateral navigation otherwise makes unanswerable, and it doubles as a quiet record of how far across the codes they've travelled. Local state only; no account, no gamification, no badges.

---

# 3. The front door

The homepage leads with a single rotating question, full width, in plain language – "Why does American football stop after every play?", "Why can a soccer minnow beat a giant?", "Why are there four kinds of rugby?" – and tapping it drops the visitor straight into that chain. **For first-time visitors the default question is the canonical entry story: the 1925 offside change** ("How did one line in the law book change football forever?"), chosen in the brief's decisions log. The thesis appears as one line beneath it: *small rule changes create entirely different games.*

Below the question, three doors:

- **Start with your game** – pick the code you know. This sets the visitor's **anchor code** (see §5) and lands them on that code's page, from which every outward prompt leads somewhere less familiar.
- **Explore the family tree** – the Map, for visitors who want the overview.
- **Watch** – the episode hub, for lean-back visitors.

Nothing else competes for the first screen. Compare, search and the timeline are present but secondary.

---

# 4. The Map

The Map opens in **guided tree view**: the trunk (medieval football → the 1863 fork) rendered simply, with branches collapsed and each split annotated with its one-line cause. Progressive disclosure – a visitor expands what they're curious about rather than confronting thirty nodes at once. Tapping a node gives its four answers (came from / why split / what changed / what survived) in place, with the door into the full code page.

The **graph view** – multiple ancestry, dashed influence edges, confidence markers – is an explicit switch, labelled honestly ("The messier truth"). It is the expert view and the historiography lives there. First-time visitors are not shown contested-descent apparatus before they've met the tree.

The Map is a hub, not the homepage. It is always one tap away (persistent in the site chrome) but never forced.

---

# 5. The anchor code

On first meaningful interaction the site asks one optional question: **"Which football do you know best?"** The answer becomes the visitor's anchor code, and the site uses it to frame everything else relatively:

- Code pages for other codes open with a one-line bridge from the anchor ("You know this as a knock-on; here it's a legal fumble").
- Compare defaults its left panel to the anchor.
- Prompts prefer routes that cross from the anchor into unfamiliar territory, which is the traversal behaviour §10 of the brief measures.
- Glossary entries surface the anchor-code sibling of an action first (a rugby-anchored visitor reading "fair catch" is shown the mark relationship immediately).

Anchoring is skippable, changeable at any time, and stored locally. It is the single strongest engagement device in the model because it converts the site's neutrality between codes into a personal vantage point – the site stays neutral; the visitor doesn't have to.

---

# 6. Moving laterally

The standard page exit is two to four specific question-prompts, each colour-marked with the code it leads into so a visitor can *see* they're about to cross a boundary. Rule pages and experiment pages additionally carry a compact strip showing every code's position on that page's dimension – the visual invitation to hop sideways.

**Compare** is reachable from every code page, every genome card, and the Map (select any two nodes). It composes from existing content per the brief: cards side by side, shared ancestor, differing rule dimensions, each difference linking to the rule page that owns the why. The share unit is the compare view itself – it is designed to be screenshotted with attribution and the URL intact.

**Search** is always present and is glossary-first: searching "scrum" returns the glossary entry, then the rule pages and episodes that cite it. Search results are phrased as the questions the pages answer.

---

# 7. The lean-back mode

**The episode hub** is a proper series surface – episodes ordered as a season with a stated cadence, each titled as its question. It is also syndicated: an audio-only derivative of each episode feeds standard podcast platforms, because "podcast-style" viewing on the site and actual podcast listening off the site are different habits and both are cheap once the script exists.

**On pages**, any page with an episode shows a *Watch this instead* control at the top – the mode switch is per-question, not a site-wide toggle. The transcript is the page (or lives on it), so switching modes never loses content.

**Episode end-cards** do the same job as page prompts: the closing question, rendered as a tappable door into the site at exactly that question – or as the next episode for visitors staying leaned back. Off-site (YouTube, podcast apps), the end-card is spoken and the door is a short memorable URL.

---

# 8. Arriving cold and coming back

**Cold arrival** (search, shared link): the first screen of every page carries its code colour and name, its question as the title, and – for chain and experiment pages – one line of "this is part of a bigger story" with the door to the Map. A visitor who lands on the 1925 offside page from Google can read it standalone, and leaves knowing the site exists around it.

**Returning visitors** are served by the "still evolving" content: the homepage's rotating question gives priority to whatever most recently changed in the real world ("Why did the NFL just redesign the kickoff?"), and the episode hub badges new episodes. No accounts, no notification machinery – recency does the work.

**On phones**, the trail collapses to a single "how I got here" control, the Map defaults to the guided tree only (graph view remains available but is desktop-first), and episodes are assumed to be the dominant mode – the mobile front door leads with Watch.
