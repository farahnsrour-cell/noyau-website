# Prepare photo plates and the mirror cutout for the Noyau statics (all at 2x of layout size).
import sys
from PIL import Image, ImageFilter, ImageDraw
IMG = sys.argv[1]; OUT = sys.argv[2]
S = 2  # render scale

def crop_to(im, box, w, h, name):
    c = im.crop(box).resize((w*S, h*S), Image.LANCZOS)
    c.save(f"{OUT}/{name}.jpg", quality=94)
    print(name, c.size)

# S1 · image 4 portrait plate 780x1010
im = Image.open(f"{IMG}/4.jpg")            # 1333x2000
crop_to(im, (0, 215, 1333, 215+1726), 780, 1010, "s1")
# S2 · image 9 landscape plate 936x660
im = Image.open(f"{IMG}/9.jpg")            # 2000x1334
aw = int(1334*936/660); x0 = (2000-aw)//2
crop_to(im, (x0, 0, x0+aw, 1334), 936, 660, "s2")
# S3 · image 10 top (beige bag held) plate 936x820
im = Image.open(f"{IMG}/10.jpg")           # 1333x2000
h = int(1333*820/936); crop_to(im, (0, 150, 1333, 150+h), 936, 820, "s3")
# S5 · image 6 portrait plate 780x1010
im = Image.open(f"{IMG}/6.jpg")            # 1333x2000
crop_to(im, (0, 140, 1333, 140+1726), 780, 1010, "s5")
# S7 · image 5 full bleed 1080x1350
im = Image.open(f"{IMG}/5.jpg")            # 1333x2000
h = int(1333*1350/1080); crop_to(im, (0, 90, 1333, 90+h), 1080, 1350, "s7")
# S8 · image 1 editorial 820x1350
im = Image.open(f"{IMG}/1.webp")           # 1024x1536
w = int(1536*820/1350); x0 = 1024-w-20; crop_to(im, (x0, 0, x0+w, 1536), 820, 1350, "s8")
# S10 · diptych panels 456x1000. HOME from image 7 (green bag on wood), AWAY from image 10 bottom (green bag in hand)
im = Image.open(f"{IMG}/7.jpg")            # 2000x1334
w = int(1334*456/1000); x0 = 530 - w//2; crop_to(im, (x0, 0, x0+w, 1334), 456, 1000, "s10_home")
im = Image.open(f"{IMG}/10.jpg")
hh = 1171; ww = int(hh*456/1000); x0 = 635-ww//2; y0 = 2000-hh
crop_to(im, (x0, y0, x0+ww, y0+hh), 456, 1000, "s10_away")

# S4 · mirror cutout from image 2 (studio white): flood fill from the border, feathered alpha
im = Image.open(f"{IMG}/2.webp").convert("RGB")
W, H = im.size
mask = Image.new("L", (W, H), 255)          # 255 = keep
px = im.load(); seen = bytearray(W*H)
from collections import deque
q = deque()
def bg(p): return p[0] > 215 and p[1] > 215 and p[2] > 215 and max(p)-min(p) < 18
for x in range(W):
    for y in (0, H-1): q.append((x, y))
for y in range(H):
    for x in (0, W-1): q.append((x, y))
m = mask.load()
while q:
    x, y = q.popleft()
    i = y*W+x
    if seen[i]: continue
    seen[i] = 1
    if not bg(px[x, y]): continue
    m[x, y] = 0
    if x > 0: q.append((x-1, y))
    if x < W-1: q.append((x+1, y))
    if y > 0: q.append((x, y-1))
    if y < H-1: q.append((x, y+1))
mask = mask.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
rgba = im.convert("RGBA"); rgba.putalpha(mask)
bbox = mask.getbbox(); cut = rgba.crop(bbox)
cut.save(f"{OUT}/s4_mirror.png"); print("s4_mirror", cut.size, "bbox", bbox)
