# World news of Thursday 19 November 2026 — in one image

An entry for make.fun's `news-image-20261119` bounty: one 1024×1024
image summing up the day's world news, judged by an AI picture editor
against the other entries.

## The image

Five stories, each verified against reporting dated 19 November 2026:

1. **Crimean Bridge hit again** — Ukraine struck the bridge overnight,
   hitting its railway section; traffic suspended while damage was assessed.
2. **Trump, Xi and Putin meet in Shenzhen** — the first-ever three-way
   meeting of the three leaders, on the sidelines of APEC.
3. **Anthropic debuts on Nasdaq** — shares begin trading as ANT after the
   $81.3B IPO priced at $83, the largest debut on record.
4. **US–Philippines push $2B defence loan** — a military-financing package
   of more than $2B, with $400M for South China Sea deterrence.
5. **GTA VI launches worldwide** — Rockstar's Grand Theft Auto VI releases
   on PlayStation 5 and Xbox Series X|S.

Three stories from the first research pass were dropped after checking:
no North Korea missile launch happened on 19 November, Jeffries was only
nominated for Speaker on 18 November (the House votes 3 January), and
Voyager 1 passed one light-day from Earth on 18 November, not the 19th.

## How it is built

`draw.py` draws the infographic with Pillow (local build step only) and
writes `entry.png`. `main.py` is the entry program: it copies that PNG
to `$MAKEFUN_OUTPUT_DIR/entry.png` using only the Python standard
library, so it runs identically in the no-network grading sandbox.

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Checks run locally on 19 November 2026: `entry.png` is 1024×1024 and
133,011 bytes (limit 1 MiB); `main.py` run twice produces byte-identical
output (`cmp` clean both times).

## License

MIT — see `LICENSE`.
