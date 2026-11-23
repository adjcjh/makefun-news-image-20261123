# 23 November 2026 — World News in One Image

Entry for the make.fun bounty
["Sum up 23 November's world news in one image"](https://make.fun/bounty/news-image-20261123)
($100 USDC, 50 places paid; deadline Wed 2026-11-25 08:00 CST).

## The image

`entry.png` — 1024×1024, 273 KB. A title banner plus 8 numbered panels,
each with a scene and a short legible caption:

1. **COP31 ends with no deal** — nearly 200 nations fail to agree a climate declaration
2. **Hormuz tankers on fire** — Iran navy says tankers blazed in a restricted area; oil falls
3. **AI sell-off hits Asia** — tech rout spreads; Trump blames Democrats for $6tn wipeout
4. **Democrats win House** — largest House majority since 1992; at least 258 seats
5. **Nvidia spy scandal** — US probes alleged spy tied to ex-CEO Jensen Huang
6. **BepiColombo at Mercury** — ESA/JAXA probe enters Mercury orbit after 8 years
7. **Indonesia fire toll 24** — Cikande candy-factory fire; dozens still missing
8. **Drones hit Khartoum** — strikes hit homes and a UN building in Sudan's capital

The panel scenes were AI-generated illustrations (no real photographs of
identifiable people); the collage, captions and layout were composed with
Python/PIL (`compose.py`, kept in the repo for reference).

## The program

`main.py` (Python 3.13, standard library only) deterministically copies
`entry.png` to `/output/entry.png`. No network, no randomness — two runs
produce byte-identical output. Verified: 1024×1024 PNG, 279,546 bytes,
identical SHA-256 across runs.

## License

MIT — see `LICENSE`.
