[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Kamprett92/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Kamprett92/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# World news of Thursday 19 November 2026 — in one image

An entry for [make.fun's `news-image-20261119` bounty](https://make.fun/bounty/news-image-20261119): one 1024×1024
image summing up the day's world news, judged by an AI picture editor
against the other entries.

## The image

Twenty-five stories, each verified against reporting dated
19 November 2026:

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
10. **Coalition of the Willing meets in Berlin** — European leaders meet
    with Witkoff and Kushner on Ukraine security guarantees.
11. **Houthi missile threat to Riyadh** — the Saudi-led coalition says it
    dealt with a Houthi missile; debris fell and damage was assessed.
12. **EU delays methane rules two years** — methane reporting rules for
    energy imports postponed, citing the Iran war disruption.
13. **China launches mystery satellite** — Shijian-24 lifts off on a
    Long March 2D rocket.
14. **COP31 gives kelp a seat at the table** — kelp forests recognised in
    ocean-climate talks for the first time.
15. **OpenAI redesigns AMD chips, +14%** — AI models compress a year of
    chip work into months.
16. **Malaysia's economy grows 5.5%** — Q3 growth stronger than expected.
17. **KGHM beats forecasts** — the Polish copper miner's Q3 net profit
    reached PLN 1.94B.
18. **mRNA vaccine shields against Nipah** — a dual-antigen jab protected
    all hamsters from Nipah and Hendra in a Nature Communications study.
19. **Gut sugar found to burn belly fat** — Duke-NUS links a gut
    bacterium's sugar to higher energy use in belly fat.
20. **Corinthians thrash Botafogo 4–0** — Brazilian league rout.
21. **Grizzlies set road win record** — 124–121 at Cleveland, their
    eighth straight road win.
22. **DOJ issues 200+ Alaska subpoenas** — probe into a decoy candidate
    in the Senate race.
23. **Four nations: let aid reach Gaza** — Australia, Canada, Italy and
    the UK call for access as floods hit the Strip.
24. **Panama: second arrest in attack case** — suspect held over the
    attack on journalist Rolando Rodríguez's home.
25. **Nigeria shares ₦2.44 trillion** — FAAC payout to federal, state
    and local governments.

Dropped after checking (v1 research): no North Korea missile launch
happened on 19 November, Jeffries was only nominated for Speaker on
18 November (the House votes 3 January), and Voyager 1 passed one
light-day from Earth on 18 November, not the 19th. V2 research also
rejected 17–18 Nov items passed off as 19 Nov news (Fed minutes,
ARIA/CMA awards, Nvidia earnings, Gaza ground operation). V3 research
rejected Palo Alto's Applied Compute deal, NASA space dust and the
California AI plan (all 18 Nov), and cut a verified Mavericks NBA win
because two NBA results add no breadth.

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
150,414 bytes (limit 1 MiB); `main.py` run twice produces byte-identical
output (`cmp` clean both times).

## License

MIT — see `LICENSE`.
