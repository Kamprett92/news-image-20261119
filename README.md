[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Kamprett92/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Kamprett92/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# World news of Thursday 19 November 2026 — in one image

An entry for [make.fun's `news-image-20261119` bounty](https://make.fun/bounty/news-image-20261119): one 1024×1024
image summing up the day's world news, judged by an AI picture editor
against the other entries.

## The image

Sixteen stories, each verified against reporting dated 19 November 2026:

1. **Crimean Bridge hit again** — Ukraine struck the bridge overnight,
   hitting its railway section; traffic suspended.
2. **Trump, Xi and Putin meet in Shenzhen** — the first-ever three-way
   meeting of the three leaders, on the sidelines of APEC.
3. **Anthropic debuts on Nasdaq** — shares begin trading as ANT after the
   $81.3B IPO priced at $83, the largest debut on record.
4. **US–Philippines push $2B defence loan** — a military-financing package
   of more than $2B, with $400M for South China Sea deterrence.
5. **GTA VI launches worldwide** — Rockstar's Grand Theft Auto VI releases
   on PlayStation 5 and Xbox Series X|S.
6. **ICJ rules in Rohingya genocide case** — the Hague court delivers its
   judgment on whether Myanmar committed genocide against the Rohingya.
7. **Xi chairs APEC, pledges $20M** — China funds Asia-Pacific
   cooperation projects.
8. **US official walks out of Ukraine talks** — Elbridge Colby leaves a
   Brussels defence meeting early over long-range strikes.
9. **Amnesty: RSF strikes are war crimes** — drone attacks on El Obeid
   killed 37 civilians.
10. **China launches mystery satellite** — Shijian-24 lifts off on a
    Long March 2D rocket.
11. **COP31 gives kelp a seat at the table** — kelp forests recognised in
    ocean-climate talks for the first time.
12. **OpenAI redesigns AMD chips, +14%** — AI models compress a year of
    chip work into months.
13. **Corinthians thrash Botafogo 4–0** — Brazilian league rout.
14. **DOJ issues 200+ Alaska subpoenas** — probe into a decoy candidate
    in the Senate race.
15. **Four nations: let aid reach Gaza** — Australia, Canada, Italy and
    the UK call for access as floods hit the Strip.
16. **Panama: second arrest in attack case** — suspect held over the
    attack on journalist Rolando Rodríguez's home.

Dropped after checking (v1 research): no North Korea missile launch
happened on 19 November, Jeffries was only nominated for Speaker on
18 November (the House votes 3 January), and Voyager 1 passed one
light-day from Earth on 18 November, not the 19th. V2 research also
rejected 17–18 Nov items passed off as 19 Nov news (Fed minutes,
ARIA/CMA awards, Nvidia earnings, Gaza ground operation).

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
137,081 bytes (limit 1 MiB); `main.py` run twice produces byte-identical
output (`cmp` clean both times).

## License

MIT — see `LICENSE`.
