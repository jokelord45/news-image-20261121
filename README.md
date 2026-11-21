# Saturday 21 November 2026 — front page

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/jokelord45/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/jokelord45/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image for Saturday 21 November 2026, laid out as a newspaper front page.

The lead is Russia's biggest attack of the war on Ukraine: more than
400 drones and 110 missiles overnight, eight people killed in Kyiv,
and two missiles plus a suspected drone coming down in Poland — which
Prime Minister Tusk called a deliberate provocation. Five panels
underneath it carry the rest of the day:

- The AI stock rout: the Nasdaq wipes out all its 2026 gains while the
  S&P 500 and Dow fall into correction, with about $4 trillion lost in
  a week as doubt grows over AI spending.
- The world court rules Myanmar responsible for genocide against the
  Rohingya.
- The UK and the EU sign their biggest post-Brexit deals: food trade,
  carbon markets and youth mobility for 100,000 young Britons.
- COP31 in Antalya runs past its deadline as nearly 200 nations fail to
  agree on fossil fuels.
- A magnitude 6.8 earthquake shakes Peru's Junin region, with tremors
  felt in Lima, 320 km away.

The black strip at the foot adds five more items: the Saudi-led
coalition intercepting three Houthi missiles aimed at Riyadh for the
third night running, a trial pill making tumours undetectable in one in
12 pancreatic cancer patients, Gen Z protests spreading across 25
European countries, New York's mayor setting 2032 as the date to close
Rikers Island, and KL Rahul completing Test centuries in all four SENA
nations.

`main.py` is the entrypoint: it copies `entry.png` (JPEG, 768x1024,
about 170 KB) into `$MAKEFUN_OUTPUT_DIR` (default `/output`), checks
the copy byte for byte against the source, and refuses anything that
is not a complete JPEG under the 1 MiB cap. Running it twice writes
identical bytes.
