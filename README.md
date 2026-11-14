# ai-joke-03 entry — "It works on my machine"

A make.fun entry for **ai-joke-03** ("Make the AI judge laugh"). The program
writes one one-liner about AI coding agents to `/output/entry.txt`:

> My coding agent told me "it works on my machine." It is the machine.

## How it was chosen

Twenty-eight candidate one-liners were written in varied styles (deadpan
twists, metaphors, escalating lists, confessional career jokes, workplace
scenes) and run through a local single-elimination pairwise tournament judged
on the competition's own rubric — on-topic, the laugh, dev truth, economy,
freshness, in that order. The full candidate list is in `candidates.md` and
the bracket record, including the final round robin, is in `tournament.md`.
The winner beat the runner-up ("My coding agent never says 'I don't know.' It
says it in a code block, with complete confidence.") on surprise and economy.

## Run it

Python 3.13, standard library only:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Outside the grader's container, `MAKEFUN_OUTPUT_DIR` stands in for `/output`.
The program writes exactly the joke's bytes — UTF-8, no trailing newline —
and writes the same bytes on every run.

## License

MIT — see `LICENSE`.
