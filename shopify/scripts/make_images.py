"""Retouche les photos produit et crée les visuels marketing (bracelet trèfle)."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

BASE = Path(sys.argv[1])
SRC, OUT = BASE / "img/orig", BASE / "img/out"
OUT.mkdir(parents=True, exist_ok=True)

CREAM, CREAM2 = (247, 242, 235), (239, 231, 220)
INK, GOLD, MUTED = (43, 38, 32), (166, 129, 74), (120, 108, 95)
G = "/usr/share/fonts/opentype/ebgaramond/"
SERIF, SERIF_IT = G + "EBGaramond12-Regular.otf", G + "EBGaramond12-Italic.otf"
SANS = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
SANS_MED = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.truetype("DejaVuSans.ttf", size)


def load(name):
    return Image.open(SRC / name).convert("RGB")


def enhance(im, size=1600):
    """Retouche douce : recadrage carré, agrandissement, lumière, contraste, netteté."""
    im = ImageOps.fit(im, (min(im.size),) * 2, method=Image.LANCZOS)
    im = im.resize((size, size), Image.LANCZOS)
    im = ImageEnhance.Brightness(im).enhance(1.04)
    im = ImageEnhance.Contrast(im).enhance(1.05)
    im = ImageEnhance.Color(im).enhance(1.06)
    return im.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=3))


def save(im, name):
    im.save(OUT / name, "JPEG", quality=88, optimize=True, progressive=True)


def center_text(d, y, text, f, fill, w):
    tw = d.textlength(text, font=f)
    d.text(((w - tw) / 2, y), text, font=f, fill=fill)


def rounded(im, r):
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, *im.size], r, fill=255)
    return im, mask


# 1. Photos retouchées (variantes + lifestyle)
photos = {
    "08.webp": "rose", "09.webp": "blanc", "10.webp": "noir", "11.webp": "rouge",
    "12.webp": "bleu", "13.webp": "vert", "03.webp": "dore", "04.webp": "porte",
}
for src, key in photos.items():
    save(enhance(load(src)), f"bracelet-trefle-{key}.jpg")

# Photo de groupe sans le texte anglais "Lucky Bracelet" (recadrage sous le texte)
grp = load("01.webp")
w, h = grp.size
side = int(h * 0.86)
x0 = (w - side) // 2
save(enhance(grp.crop((x0, h - side, x0 + side, h))), "bracelet-trefle-toutes-couleurs.jpg")

# 2. Visuel « 7 couleurs »
W = 2000
cv = Image.new("RGB", (W, W), CREAM)
d = ImageDraw.Draw(cv)
center_text(d, 200, "BRACELET TRÈFLE", font(SANS_MED, 40), GOLD, W)
center_text(d, 260, "Une couleur pour chaque style", font(SERIF_IT, 104), INK, W)
order = ["dore", "noir", "blanc", "rose", "rouge", "bleu", "vert"]
labels = {"dore": "Doré", "noir": "Noir", "blanc": "Blanc", "rose": "Rose",
          "rouge": "Rouge", "bleu": "Bleu", "vert": "Vert"}
tile, gap = 420, 40
rows = [order[:4], order[4:]]
y = 540
for row in rows:
    x = (W - (len(row) * tile + (len(row) - 1) * gap)) // 2
    for key in row:
        src = Image.open(OUT / f"bracelet-trefle-{key}.jpg")
        s = src.size[0]
        t = src.crop((int(s * .12), int(s * .14), int(s * .88), int(s * .90))).resize((tile, tile), Image.LANCZOS)
        img, mask = rounded(t, 28)
        cv.paste(img, (x, y), mask)
        center_label = labels[key]
        f = font(SANS, 34)
        tw = d.textlength(center_label, font=f)
        d.text((x + (tile - tw) / 2, y + tile + 18), center_label, font=f, fill=MUTED)
        x += tile + gap
    y += tile + 110
center_text(d, 1700, "Acier inoxydable couleur or  ·  Taille réglable", font(SANS, 38), MUTED, W)
save(cv, "bracelet-trefle-7-couleurs.jpg")

# 3. Visuel « Détails & dimensions »
cv = Image.new("RGB", (W, W), CREAM)
d = ImageDraw.Draw(cv)
center_text(d, 110, "LES DÉTAILS", font(SANS_MED, 40), GOLD, W)
center_text(d, 170, "Pensé pour être porté tous les jours", font(SERIF_IT, 96), INK, W)
ph = enhance(load("03.webp"), 1240)
ph = ph.crop((0, 90, 1240, 1150))
img, mask = rounded(ph, 36)
cv.paste(img, ((W - 1240) // 2, 360), mask)
specs = [("16,5 cm", "+ 5 cm de rallonge"), ("1,3 cm", "par trèfle"),
         ("9,9 g", "léger au poignet"), ("Acier", "inoxydable doré")]
colw = W // 4
for i, (big, small) in enumerate(specs):
    cx = i * colw
    fb, fs = font(SERIF, 84), font(SANS, 32)
    d.text((cx + (colw - d.textlength(big, font=fb)) / 2, 1500), big, font=fb, fill=INK)
    d.text((cx + (colw - d.textlength(small, font=fs)) / 2, 1610), small, font=fs, fill=MUTED)
    if i:
        d.line([(cx, 1510), (cx, 1650)], fill=CREAM2, width=3)
center_text(d, 1790, "Fermoir mousqueton  ·  chaînette de réglage", font(SANS, 36), MUTED, W)
save(cv, "bracelet-trefle-details.jpg")

# 4. Visuel « Pourquoi vous allez l'adorer »
cv = Image.new("RGB", (W, W), CREAM)
d = ImageDraw.Draw(cv)
ph = enhance(load("04.webp"), 1000)
img, mask = rounded(ph.resize((900, 1500), Image.LANCZOS) if False else ImageOps.fit(ph, (900, 1500)), 40)
cv.paste(img, (100, 250), mask)
d.text((1100, 260), "POURQUOI", font=font(SANS_MED, 40), fill=GOLD)
d.text((1100, 310), "vous allez", font=font(SERIF_IT, 110), fill=INK)
d.text((1100, 420), "l’adorer", font=font(SERIF_IT, 110), fill=INK)
points = [
    ("Élégant au quotidien", "Du jean à la robe de soirée,\nil s’accorde à tout."),
    ("Taille réglable", "Chaînette de rallonge pour\nun ajustement parfait."),
    ("Acier inoxydable", "Une base solide et durable,\nfinition couleur or."),
    ("L’idée cadeau", "Anniversaire, fête des mères,\nou juste pour se faire plaisir."),
]
y = 640
for title, body in points:
    d.ellipse([1100, y + 18, 1124, y + 42], fill=GOLD)
    d.text((1150, y), title, font=font(SERIF, 64), fill=INK)
    d.multiline_text((1150, y + 82), body, font=font(SANS, 34), fill=MUTED, spacing=10)
    y += 270
save(cv, "bracelet-trefle-avantages.jpg")

for p in sorted(OUT.iterdir()):
    print(p.name, Image.open(p).size, f"{p.stat().st_size // 1024} Ko")
