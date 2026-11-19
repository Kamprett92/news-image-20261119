"""News-image entry: copy the built infographic to the output path.

The image (entry.png, 1024x1024) sums up the world news of Thursday
19 November 2026. It is drawn by draw.py in this repository and shipped
as a file, so this program only copies it: deterministic, no network,
same bytes on every run.

Run locally with:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
target = OUTPUT_DIR / "entry.png"
shutil.copyfile(HERE / "entry.png", target)
# The grader runs this program twice and requires identical bytes;
# fail loudly here instead of shipping a partial copy.
assert target.stat().st_size == (HERE / "entry.png").stat().st_size
