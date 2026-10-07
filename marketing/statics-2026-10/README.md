# Noyau · October statics

Eight Instagram statics and two statistic cards (1080 × 1350) for 8 to 28 October, built from Farah's product and lifestyle photographs with the brand type (Cormorant Garamond with Hanken Grotesk) and the wordmark without the ® mark.

| Date | File | Post | Serves |
|---|---|---|---|
| Thu 8 Oct | `final/S1` | A complete skincare ritual, in one place | Sales |
| Sat 10 Oct | `final/I1` | 22.4 minutes a day on skincare routines | Growth |
| Tue 13 Oct | `final/S2` | A ritual, shared (lifestyle photo, text overlay) | Growth, awareness |
| Thu 15 Oct | `final/S4` | The mirror | Sales |
| Sat 17 Oct | `final/S6` | A ritual that travels | Awareness |
| Sun 18 Oct | `final/I2` | A recent UK study: 60%, 69%, 21% | Growth |
| Mon 19 Oct | `final/S3` | Forest Green or Light Beige | Sales |
| Sat 24 Oct | `final/S8` | Built to a standard, not to a season | Awareness |
| Sun 25 Oct | `final/S5` | The details (photography-led editorial) | Sales |
| Wed 28 Oct | `final/S7` | A familiar ritual, wherever you stay (home / away diptych) | Awareness |

`final/noyau-statics-october.pdf` holds all ten pages for Canva (`-v4.pdf` is the copy Canva imported).

`archive-v1/` keeps the first set, including three finished pages not in the current plan: A ritual, given (gifting, old S5), the 8 statistic card (old S6, now a carousel idea) and Sold complete. One price, everywhere (old S9).

The two statistic cards carry the figures as supplied; add the study name and year to each caption, and to the card if wanted, before posting.

Rebuild: `python3 prep.py <photos dir> plates` (crops and the mirror cutout), `python3 build.py` (HTML in `html/`), `NODE_PATH=$(npm root -g) node render.cjs` (2x screenshots in `out2x/`), then downsample to 1080 × 1350. `node pdf.cjs` prints the ten pages to one PDF.
