"""Recorta imágenes oficiales de producto (fondo claro) a PNG transparente sin sombra.
Uso: python3 recorte.py <entrada> <salida.png> [--hull|--mirror]
--hull: envases con etiqueta blanca (frascos, botellas): usa la silueta convexa del modelo u2net.
Sin opción: productos con forma irregular o elementos al lado (ej. Nitro Tech con helado, barras)."""
import sys
from rembg import remove, new_session
from PIL import Image, ImageFilter
import numpy as np
from scipy import ndimage

def recortar(path, out, mirror=False, sess=None, hull=False):
    src = Image.open(path).convert('RGBA')
    bg = Image.new('RGBA', src.size, (255, 255, 255, 255)); bg.alpha_composite(src); rgb = bg.convert('RGB')
    a = np.asarray(rgb).astype(int); H, W = a.shape[:2]
    bc = np.median(np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]]), 0)
    near = np.abs(a - bc).max(2) <= 6
    lab, _ = ndimage.label(near); edge = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    strict = ~np.isin(lab, list(edge))
    u2 = np.asarray(remove(rgb, session=sess or new_session('u2net'), only_mask=True).convert('L')) > 100
    if hull:
        from scipy.spatial import ConvexHull
        from PIL import ImageDraw
        u = ndimage.binary_opening(u2, iterations=2); l, n = ndimage.label(u); z = ndimage.sum(u, l, range(1, n + 1)); u = l == (np.argmax(z) + 1)
        ys, xs = np.nonzero(u); pts = np.c_[xs, ys]; h = ConvexHull(pts); S = 2
        m = Image.new('L', (W * S, H * S), 0); ImageDraw.Draw(m).polygon([tuple(p * S) for p in pts[h.vertices]], fill=255)
        m = m.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
        im = rgb.resize(m.size, Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=2, percent=70, threshold=2))
        im.putalpha(m); im = im.crop(m.getbbox()); im.save(out); return im
    fg = strict & ndimage.binary_dilation(u2, iterations=4)   # quita sombras que u2net no ve como producto
    fg = ndimage.binary_fill_holes(fg); fg = ndimage.binary_opening(fg, iterations=2)
    l2, nl = ndimage.label(fg); sz = ndimage.sum(fg, l2, range(1, nl + 1)); fg = l2 == (np.argmax(sz) + 1)
    if mirror:
        rows = range(int(H * .35), int(H * .65)); xs = [np.nonzero(fg[r])[0] for r in rows]; xs = [x for x in xs if len(x)]
        cx = np.median([(x[0] + x[-1]) / 2 for x in xs]); mx = np.clip(np.round(2 * cx - np.arange(W)).astype(int), 0, W - 1)
        fg = ndimage.binary_fill_holes(fg | (fg[:, mx] & strict))
    S = 2
    al = Image.fromarray((fg * 255).astype('uint8')).resize((W * S, H * S), Image.LANCZOS).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
    im = rgb.resize(al.size, Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=2, percent=70, threshold=2))
    im.putalpha(al); im = im.crop(al.getbbox()); im.save(out); return im

if __name__ == '__main__':
    recortar(sys.argv[1], sys.argv[2], '--mirror' in sys.argv, hull='--hull' in sys.argv)
