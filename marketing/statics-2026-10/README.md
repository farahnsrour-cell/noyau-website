# Noyau · October statics

Ten Instagram statics (1080 × 1350) for 8 to 28 October, built from Farah's product and lifestyle photographs with the brand type (Cormorant Garamond with Hanken Grotesk) and the wordmark without the ® mark.

| File | Post |
|---|---|
| `final/S1` | A complete skincare ritual, in one place · 8 Oct |
| `final/S6` | 8. Eight pieces. One order. One bag · 11 Oct |
| `final/S7` | A ritual, shared · 13 Oct |
| `final/S4` | The mirror · 15 Oct |
| `final/S3` | A ritual that travels · 17 Oct |
| `final/S2` | Forest Green or Light Beige · 19 Oct |
| `final/S9` | Sold complete. One price, everywhere · 21 Oct |
| `final/S5` | A ritual, given · 23 Oct |
| `final/S8` | The details · 25 Oct |
| `final/S10` | A familiar ritual, wherever you stay · 28 Oct |

`final/noyau-statics-october.pdf` (also `-v3.pdf`, the copy Canva imported) holds all ten pages for a Canva import (Upload, then open the PDF as a design).

Rebuild: `python3 prep.py <photos dir> plates` (crops and the mirror cutout), `python3 build.py` (HTML in `html/`), `NODE_PATH=$(npm root -g) node render.cjs` (2x screenshots in `out2x/`), then downsample to 1080 × 1350.
