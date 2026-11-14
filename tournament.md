# ai-joke-03 — local pairwise tournament

Method: single-elimination bracket judged in the persona of the sealed judge from RULES.txt —
an AI comedy judge picking, for a room of developers who work beside coding agents, by the rubric
in its fixed order: (1) on-topic joke about AI coding agents, (2) the laugh — a surprise punchline
that still makes sense, (3) truth a dev recognises at once, (4) economy — every word earning its
place, (5) freshness. The first criterion where a pair differs decides, unless a later one differs
by much more. Margins are the judge's 1 (by a hair) to 5 (overwhelming).

## Qualifying cut (28 → 24)

- C13 ("committed both as 'fix error'") — cut: plausible-behaviour gag with no real surprise turn.
- C17 ("// adds the numbers") — cut: recognition chuckle for a narrow slice; the laugh never springs.
- C20 (agent reviews the agent's PRs) — cut: workflow satire that states its gag instead of springing it.
- C23 (900-line fix for a typo) — cut: same over-engineering territory as C16/C24, wordier than both.

Seeds: 1 C1 · 2 C2 · 3 C5 · 4 C3 · 5 C6 · 6 C4 · 7 C11 · 8 C8 · 9 C9 · 10 C25 · 11 C10 · 12 C15 ·
13 C16 · 14 C7 · 15 C12 · 16 C28 · 17 C26 · 18 C14 · 19 C27 · 20 C18 · 21 C21 · 22 C22 · 23 C24 · 24 C19

## Round 1 (seed vs seed)

- C1 def. C19 (margin 3): the machine twist detonates in five words; the autocomplete list is a smile, not a snap.
- C2 def. C24 (margin 2): "exactly what I said, never what I meant" is the bigger laugh; C24's scaffolding list is truth without a turn.
- C5 def. C22 (margin 2): "but at least it's original" is a real punchline; the landlord metaphor amuses but never snaps.
- C3 def. C21 (margin 3): C21 explains itself and runs long — economy decides after an even laugh.
- C6 def. C18 (margin 2): escalating misbehaviour with a deletion at the end beats a straight, if accurate, observation.
- C4 def. C27 (margin 2): the read-everything/remembers-nothing image is fresher than the well-worn "AI takes my job" frame.
- C11 def. C14 (margin 3): the counting gag lands instantly; the standup scene needs its setting explained by familiarity.
- C8 def. C26 (margin 2): the toddler hiding broken pieces is vivid and visual; C26's second half meanders.
- C9 def. C28 (margin 2): the unreliable-witness metaphor is the fresher angle; the smoke alarm is a familiar comparison shape.
- C25 def. C12 (margin 2): "a younger, faster bug" is a genuine surprise; the duck's different bug is a turn you can see coming.
- C10 def. C7 (margin 2): a clean paradox that reads at a glance; C7 is clever but abstract, the judge has to work for it.
- C16 def. C15 (margin 1): final_v2 is a concrete, screenshot-true laugh; the goldfish line is warm but softer. Closest match of the round.

## Round 2

- C1 def. C16 (margin 2): both run on recognition, but C1 needs no setup at all — one borrowed excuse, one twist.
- C2 def. C10 (margin 2): the genie frame converts the daily spec-gaming frustration into a mechanism; C10's paradox is neat but slighter.
- C25 def. C5 (margin 1): laugh is even, truth is even; economy (18 words vs 30) and the novel phrase "younger, faster bug" decide it.
- C3 def. C8 (margin 1): the toddler image delights, but C3's joke performs itself — it *says* "I don't know" in a code block — and is tighter.
- C6 def. C9 (margin 2): devs have literally watched an agent delete a failing test; the witness metaphor laughs a beat slower.
- C11 def. C4 (margin 2): the arithmetic spring ("fixed a sixth") is a joke mechanism with a snap; C4 lands as a knowing smile.

## Semifinals

- SF1 — C1 def. C11 (margin 2): C11 is the best pure gag in the field, but C1 hijacks the oldest excuse in
  development and the five-word reveal ("It is the machine.") is the biggest surprise per word in the bracket.
  It also lands for any dev, even one who has never debugged agent output.
- SF2 — C2 def. C6 (margin 2): C6's deleted test is the round's strongest truth, yet its middle clause
  ("graded every test") pads the line. C2 is one clean mechanism — wish, wording, instant delivery — and
  freshness favours the fairy-tale frame over the test-suite frame.
- SF3 — C3 def. C25 (margin 1): the hardest call before the final. "A younger, faster bug" is a superb
  phrase, but C3 names the single most recognisable agent trait — it never admits ignorance — and the
  punchline re-reads the entire first clause. Truth differs enough, late, to overturn C25's economy edge.

## Final — round robin among C1, C2, C3

- C1 def. C2 (margin 2): C2's laugh is a slow-burn nod of recognition; C1's is instant. Economy is not
  close (15 words against 22), and both are equally true.
- C3 def. C2 (margin 1): C2's "never what I meant" is a fine reframe, but C3's self-performing structure —
  the denial delivered as a confident code block — gets the sharper laugh.
- C1 def. C3 (margin 2) — the championship game: C3 captures hallucinated confidence perfectly, but C1's
  surprise is bigger precisely because the setup is the most familiar sentence in software. Criterion 2
  (the laugh) differs first and settles it; criterion 4 (economy) confirms it.

## Result

- **Winner: C1** — "My coding agent told me "it works on my machine." It is the machine."
- **Runner-up: C3** — "My coding agent never says "I don't know." It says it in a code block, with complete confidence."
- Third: C2 (the genie joke, my pre-tournament favourite — the bracket overruled it).

Why C1 is the pick against a strong field, not a personal favourite: it is the shortest serious
contender, its setup is borrowed from the most universal dev experience there is, and its punchline is
a single twist that needs no agent-specific knowledge to detonate — the profile that survives the most
pairwise matchups against unknown opposition.
