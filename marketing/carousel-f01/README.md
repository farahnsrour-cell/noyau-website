# F01 · Carousel · What's inside The Ritual Kit

Ten slides, 1080 × 1350, built to the markers of the published posts: forest ground, Sackers Gothic caps eyebrow top-left, wordmark with ® top-right, Montserrat bold headline with a light subline, slide counter at the foot, the "n" emblem watermark on the closing slide. Item slides follow Farah's reference: serif caps H1 (Cormorant Garamond), italic subline, the piece cut out on the forest ground with three hairline callouts.

| Slide | Content | State |
|---|---|---|
| 01 | Cover: the open kit photograph above a forest panel with the title | Final |
| 02 | 01 · The bag: Saffiano leather bag, three callouts | Final |
| 03–09 | The brush, headband set, towels, pads, jade roller, gua sha, mask: layout and drafted copy, photo placeholder | Need each piece's photo and copy sign-off |
| 10 | Closing: Eight pieces. One order. One bag. Price and link | Final |

Rebuild: `python3 build_f01.py` writes `html/`, `NODE_PATH=$(npm root -g) node render.cjs` renders `out2x/`, downsample to 1080 × 1350 into `final/`, `node pdf.cjs` prints the PDF. Drop each piece's cutout into `plates/` as a PNG with transparency and pass its path in `build_f01.py`.

The bag cutout in `plates/f01_bag.png` was made from `src/bags-wood.jpg` with a colour mask; product pixels are untouched.
