# ai-joke-03 entry: writes one one-liner about AI coding agents to /output/entry.txt.
# Python 3.13, standard library only. The program runs twice and must write the
# same bytes both times, so the joke is a fixed constant with no trailing newline
# (the judge reads exactly the bytes in the file).
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

JOKE = "My coding agent told me \"it works on my machine.\" It is the machine."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
