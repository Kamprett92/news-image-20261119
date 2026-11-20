[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Kamprett92/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Kamprett92/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# World news of Thursday 19 November 2026 — in one image

An entry for [make.fun's `news-image-20261119` bounty](https://make.fun/bounty/news-image-20261119): one 1024×1024
image summing up the day's world news, judged by an AI picture editor
against the other entries.

## The image

Thirty stories, each verified against reporting dated
19 November 2026:

1. **Crimean Bridge hit again** — Ukraine struck the bridge overnight,
   hitting its railway section; traffic suspended.
2. **Trump, Xi and Putin meet in Shenzhen** — the first-ever three-way
   meeting of the three leaders, on the sidelines of APEC.
3. **Wall Street plunges** — the Dow fell 1,101 points and the S&P 500
   lost a sixth straight day despite Anthropic's record debut.
4. **ICJ: Myanmar guilty of genocide** — the Hague court rules 9–6 that
   Myanmar committed genocide against the Rohingya, the first time it
   has held a state responsible; reparations ordered.
5. **Senate blocks Iran war-powers bid** — the Senate rejects 48–51 a
   resolution to curb Trump's Iran war powers.
6. **Montenegro closes 2 more EU chapters** — taxation and regional
   policy close at the 31st accession conference; 25 of 33 done.
7. **Trump pardons Pete Rose** — a posthumous pardon for baseball's
   all-time hits leader, announced from Air Force One.
8. **Hackers leak bank customer data** — ransomware group "n0n" leaks
   customer data from JPMorgan, Visa and Mastercard vendors.
9. **Anthropic debuts on Nasdaq** — shares begin trading as ANT after the
   $81.3B IPO priced at $83, the largest debut on record.
10. **US–Philippines push $2B defence loan** — a military-financing package
    of more than $2B, with $400M for South China Sea deterrence.
11. **GTA VI launches worldwide** — Rockstar's Grand Theft Auto VI releases
    on PlayStation 5 and Xbox Series X|S.
12. **Xi chairs APEC, pledges $20M** — China funds Asia-Pacific
    cooperation projects.
13. **US official walks out of Ukraine talks** — Elbridge Colby leaves a
    Brussels defence meeting early over long-range strikes.
14. **Amnesty: RSF strikes are war crimes** — drone attacks on El Obeid
    killed 37 civilians.
15. **Coalition of the Willing meets in Berlin** — European leaders meet
    with Witkoff and Kushner on Ukraine security guarantees.
16. **Houthi missile threat to Riyadh** — the Saudi-led coalition says it
    dealt with a Houthi missile; debris fell and damage was assessed.
17. **EU delays methane rules two years** — methane reporting rules for
    energy imports postponed, citing the Iran war disruption.
18. **China launches mystery satellite** — Shijian-24 lifts off on a
    Long March 2D rocket.
19. **COP31 gives kelp a seat at the table** — kelp forests recognised in
    ocean-climate talks for the first time.
20. **OpenAI redesigns AMD chips, +14%** — AI models compress a year of
    chip work into months.
21. **Malaysia's economy grows 5.5%** — Q3 growth stronger than expected.
22. **KGHM beats forecasts** — the Polish copper miner's Q3 net profit
    reached PLN 1.94B.
23. **mRNA vaccine shields against Nipah** — a dual-antigen jab protected
    all hamsters from Nipah and Hendra in a Nature Communications study.
24. **Gut sugar found to burn belly fat** — Duke-NUS links a gut
    bacterium's sugar to higher energy use in belly fat.
25. **Corinthians thrash Botafogo 4–0** — Brazilian league rout.
26. **Grizzlies set road win record** — 124–121 at Cleveland, their
    eighth straight road win.
27. **DOJ issues 200+ Alaska subpoenas** — probe into a decoy candidate
    in the Senate race.
28. **Four nations: let aid reach Gaza** — Australia, Canada, Italy and
    the UK call for access as floods hit the Strip.
29. **Panama: second arrest in attack case** — suspect held over the
    attack on journalist Rolando Rodríguez's home.
30. **Nigeria shares ₦2.44 trillion** — FAAC payout to federal, state
    and local governments.

Dropped after checking (v1 research): no North Korea missile launch
happened on 19 November, Jeffries was only nominated for Speaker on
18 November (the House votes 3 January), and Voyager 1 passed one
light-day from Earth on 18 November, not the 19th. V2 research also
rejected 17–18 Nov items passed off as 19 Nov news (Fed minutes,
ARIA/CMA awards, Nvidia earnings, Gaza ground operation). V3 research
rejected Palo Alto's Applied Compute deal, NASA space dust and the
California AI plan (all 18 Nov), and cut a verified Mavericks NBA win
because two NBA results add no breadth. V4 research rejected the UN
Security Council Libya briefing (held 18 Nov, only covered on the 19th),
and left the verified Texans–Colts win and Bitcoin's slide to $61,300
out to keep the page legible at 30 stories.

## How it is built

`draw.py` draws the infographic with Pillow (local build step only) and
writes `entry.png`. `main.py` is the entry program: it copies that PNG
to `$MAKEFUN_OUTPUT_DIR/entry.png` using only the Python standard
library, so it runs identically in the no-network grading sandbox.

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Checks run locally on 20 November 2026: `entry.png` is 1024×1024 and
152,772 bytes (limit 1 MiB); `main.py` run twice produces byte-identical
output (`cmp` clean both times).

## License

MIT — see `LICENSE`.
