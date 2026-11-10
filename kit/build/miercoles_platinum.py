"""Miércoles 11 nov 2026 · producto de la semana (creatina, estilo SOBRIO).
Idea nueva: LOOK DE FLASH DIRECTO (tendencia de foto de producto 2025-26: flash frontal duro que deja una
sombra nítida del envase en la pared de atrás, como foto editorial de campaña).
Feed (4:5, Metricool 10 AM): MuscleTech Platinum sin sabor "Sin sabor. Sin excusas." · 80 porciones.
Historias 9:16: 1 macro con flash "Pura. Micronizada." · 2 encuesta "¿Con qué la tomas?" (espacio libre 760–1080).
Sin precios, sin numeración. Uso (desde kit/build): python3 miercoles_platinum.py <feed_dir> <hist_dir>
"""
import sys
FEED_OUT = sys.argv[1] if len(sys.argv) > 1 else 'feed'
HIST_OUT = sys.argv[2] if len(sys.argv) > 2 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

OR = P.OR
IMG = 'p_mt_sin.png'


def flash(cx, base_y, height, dx=46, dy=-30, rot=0):
    """Producto con flash duro: sombra nítida corrida hacia la pared, piso brillante y reflejo."""
    src = P.I(IMG)
    t = f'left:{cx}px;top:{base_y}px;height:{height}px;transform:translate(-50%,-100%) rotate({rot}deg)'
    sh = (f'<img src="{src}" style="position:absolute;left:{cx + dx}px;top:{base_y + dy}px;height:{height}px;'
          f'transform:translate(-50%,-100%) rotate({rot}deg);filter:brightness(0) blur(2px);opacity:.78">')
    prod = (f'<img src="{src}" style="position:absolute;{t};'
            'filter:contrast(1.08) brightness(1.06) drop-shadow(0 18px 14px rgba(0,0,0,.7))">')
    refl = (f'<img src="{src}" style="position:absolute;left:{cx}px;top:{base_y}px;height:{height}px;'
            'transform:translate(-50%,0) scaleY(-1);opacity:.16;'
            '-webkit-mask-image:linear-gradient(to bottom,rgba(0,0,0,.9),transparent 40%)">')
    return sh + prod + refl


def fondo(w, h, floor_y, cx, cy):
    """Pared gris carbón iluminada por el flash (centro claro, bordes negros) y piso."""
    return (f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse 60% 48% at {cx}px {cy}px,'
            '#4a453f 0%,#2a2622 40%,#0d0c0b 78%,#060504 100%)"></div>'
            f'<div style="position:absolute;left:0;right:0;top:{floor_y}px;bottom:0;'
            f'background:radial-gradient(ellipse 55% 60% at {cx}px 0,#2c2925 0%,#121110 55%,#060504 100%)"></div>'
            f'<div style="position:absolute;left:0;right:0;top:{floor_y}px;height:2px;background:rgba(255,255,255,.05)"></div>')


def feed():
    W, H = 1080, 1350
    b = (fondo(W, H, 1110, 600, 760)
         + flash(600, 1110, 620)
         + P.marca(70, 64) + '<div class="foot" style="right:70px;top:74px">Producto de la semana</div>'
         + '<div style="position:absolute;left:70px;top:150px"><div class="h" style="font-size:150px;line-height:.9">Sin sabor.</div>'
           f'<div class="h" style="font-size:150px;line-height:.9;color:{OR}">Sin excusas.</div></div>'
         + '<div style="position:absolute;left:70px;right:70px;bottom:70px;display:flex;justify-content:space-between;align-items:flex-end">'
           '<div><div class="lab" style="color:#d8d3cb">MuscleTech Platinum · 400 g</div>'
           '<div style="font-size:34px;color:#c9c4bc;margin-top:10px;font-weight:500">Micronizada. 5 g al día. 80 porciones.</div></div>'
           f'<div style="width:90px;height:2px;background:{OR};margin-bottom:18px"></div></div>')
    return P.page(W, H, b, 'rgba(0,0,0,0)')


def h_macro():
    SW, SH = 1080, 1920
    b = (fondo(SW, SH, 1560, 560, 1150)
         + flash(560, 1560, 780, dx=56, dy=-36)
         + P.marca(70, 150)
         + '<div style="position:absolute;left:70px;top:290px"><div class="lab">Producto de la semana</div>'
           '<div class="h" style="font-size:170px;line-height:.9;margin-top:20px">Pura.</div>'
           f'<div class="h" style="font-size:170px;line-height:.9;color:{OR}">Micronizada.</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">5 g al día · 80 porciones · Sin sabor</div>')
    return P.page(SW, SH, b, 'rgba(0,0,0,0)')


def h_encuesta():
    SW, SH = 1080, 1920
    b = (fondo(SW, SH, 1560, 540, 1300)
         + flash(540, 1560, 480, dx=34, dy=-22)
         + P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:300px;text-align:center"><div class="lab">Sin sabor · 5 g</div>'
           '<div class="h" style="font-size:180px;line-height:.92;margin-top:22px">¿Con qué</div>'
           f'<div class="h" style="font-size:180px;line-height:.92;color:{OR}">la tomas?</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">MuscleTech Platinum 400 g · 80 porciones · Pídela por DM</div>')
    return P.page(SW, SH, b, 'rgba(0,0,0,0)')


if __name__ == '__main__':
    P.render([('1_platinum_sin_sabor', feed())], FEED_OUT, 1080, 1350)
    P.render([('1_pura_micronizada', h_macro()), ('2_con_que_la_tomas', h_encuesta())], HIST_OUT, 1080, 1920)
