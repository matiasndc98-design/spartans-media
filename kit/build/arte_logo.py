import sys
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
SRC = sys.argv[1]; OUT = sys.argv[2]
im = Image.open(SRC).convert('RGB')
W, H = im.size; k = W / 1254  # escala por si la imagen viene en otro tamaño
logo = Image.open('/home/claude/spartans-media/Logo/logo_spartans_transparente.png').convert('RGBA')
logo = logo.crop(logo.getbbox())

def disco(cx, cy, r, color=(4, 3, 3), blur=3):
    m = Image.new('L', im.size, 0); ImageDraw.Draw(m).ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(blur))
    im.paste(Image.new('RGB', im.size, color), (0, 0), m)

def pegar(cx, cy, w, tint=None):
    L = logo.resize((int(w), int(w * logo.height / logo.width)), Image.LANCZOS)
    if tint:
        a = L.split()[3]; L = Image.new('RGBA', L.size, tint + (255,)); L.putalpha(a)
    # halo oscuro para separar del fondo
    sh = Image.new('RGBA', L.size, (0, 0, 0, 0)); sh.putalpha(L.split()[3].filter(ImageFilter.MaxFilter(9)))
    im.paste((0, 0, 0), (int(cx - L.width / 2), int(cy - L.height / 2)), sh.split()[3])
    im.paste(L, (int(cx - L.width / 2), int(cy - L.height / 2)), L)

# pecho: disco negro (como el original) + logo nuevo
disco(620 * k, 552 * k, 76 * k)
pegar(620 * k, 552 * k, 138 * k)
# bajo SPARTANS: fondo negro + logo nuevo
d = ImageDraw.Draw(im)
m = Image.new('L', im.size, 0); ImageDraw.Draw(m).ellipse([566 * k, 972 * k, 684 * k, 1104 * k], fill=255); m = m.filter(ImageFilter.GaussianBlur(3))
im.paste(Image.new('RGB', im.size, (3, 2, 2)), (0, 0), m)
pegar(625 * k, 1040 * k, 120 * k)
# medallas de los hombros: fondo oscuro dentro del anillo dorado + logo en tono bronce
for cx in (457, 774):
    disco(cx * k, 424 * k, 19 * k, (22, 18, 16), 1.5)
    pegar(cx * k, 424 * k, 34 * k, tint=(214, 150, 80))
im.save(OUT, quality=95)
