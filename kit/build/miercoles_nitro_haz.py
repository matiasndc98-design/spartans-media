"""Miércoles 18 nov 2026 · producto de la semana (proteína, estilo SOBRIO).
Idea nueva: HAZ DE LUZ EN SET OSCURO (tendencia de renders/fotos de suplementos 2026: un solo haz de luz
diagonal que cae sobre el envase en un set negro con algo de bruma; aquí el haz es cálido, acento Spartans).
Feed (4:5, Metricool 10 AM): MuscleTech Nitro Tech 4 lb vainilla "Todo en un scoop." · 30 g + 3 g de creatina.
Historias 9:16: 1 haz "Proteína. + Creatina." · 2 encuesta "¿Ya la probaste?" (espacio libre ~700–1050).
Sin precios, sin numeración. Uso (desde kit/build): python3 miercoles_nitro_haz.py <feed_dir> <hist_dir>
"""
import sys
FEED_OUT = sys.argv[1] if len(sys.argv) > 1 else 'feed'
HIST_OUT = sys.argv[2] if len(sys.argv) > 2 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

OR = P.OR
IMG = 'p_nitro.png'


def set_haz(w, h, floor_y, cx, top_x=None, ang=18, ancho=360):
    """Set negro con un haz de luz cálido que baja en diagonal hasta el producto, bruma y piso."""
    import math
    top_x = cx - (floor_y + 200) * math.tan(math.radians(ang))  # el haz cae justo sobre el producto
    top_x = int(top_x)
    return (
        '<div style="position:absolute;inset:0;background:#060504"></div>'
        # haz: trapecio difuminado desde arriba hasta el piso
        f'<div style="position:absolute;left:{top_x - ancho // 2}px;top:-200px;width:{ancho}px;height:{floor_y + 200}px;'
        f'transform-origin:50% 0;transform:rotate({-ang}deg);filter:blur(20px)">'
        '<div style="position:absolute;inset:0;clip-path:polygon(40% 0,60% 0,92% 100%,8% 100%);'
        'background:linear-gradient(to bottom,rgba(255,214,170,.02),rgba(255,190,130,.26) 55%,rgba(242,140,70,.36))"></div></div>'
        # núcleo más brillante del haz
        f'<div style="position:absolute;left:{top_x - ancho // 4}px;top:-200px;width:{ancho // 2}px;height:{floor_y + 200}px;'
        f'transform-origin:50% 0;transform:rotate({-ang}deg);filter:blur(10px)">'
        '<div style="position:absolute;inset:0;clip-path:polygon(44% 0,56% 0,90% 100%,10% 100%);'
        'background:linear-gradient(to bottom,rgba(255,230,200,0),rgba(255,220,180,.18) 60%,rgba(255,200,150,.26))"></div></div>'
        # bruma baja
        f'<div style="position:absolute;left:0;right:0;top:{floor_y - 260}px;height:420px;'
        f'background:radial-gradient(ellipse 45% 50% at {cx}px 65%,rgba(255,170,110,.10),transparent 70%)"></div>'
        # piso con charco de luz
        f'<div style="position:absolute;left:0;right:0;top:{floor_y}px;bottom:0;'
        f'background:radial-gradient(ellipse 38% 45% at {cx}px 0,#3a2a1f 0%,#17110d 50%,#060504 100%)"></div>'
        f'<div style="position:absolute;left:0;right:0;top:{floor_y}px;height:2px;background:rgba(255,220,190,.06)"></div>'
    )


def producto(cx, base_y, height):
    src = P.I(IMG)
    prod = (f'<img src="{src}" style="position:absolute;left:{cx}px;top:{base_y}px;height:{height}px;'
            'transform:translate(-50%,-100%);'
            'filter:contrast(1.06) brightness(1.02) drop-shadow(18px 22px 22px rgba(0,0,0,.75))">')
    # brillo cálido del haz sobre el lado izquierdo del envase
    luz = (f'<img src="{src}" style="position:absolute;left:{cx}px;top:{base_y}px;height:{height}px;'
           'transform:translate(-50%,-100%);mix-blend-mode:screen;opacity:.35;'
           'filter:sepia(1) saturate(3) hue-rotate(-12deg) brightness(.9);'
           '-webkit-mask-image:linear-gradient(100deg,#000 0%,transparent 55%)">')
    refl = (f'<img src="{src}" style="position:absolute;left:{cx}px;top:{base_y}px;height:{height}px;'
            'transform:translate(-50%,0) scaleY(-1);opacity:.14;'
            '-webkit-mask-image:linear-gradient(to bottom,rgba(0,0,0,.9),transparent 38%)">')
    return prod + luz + refl


def feed():
    W, H = 1080, 1350
    b = (set_haz(W, H, 1120, 640, 470)
         + producto(640, 1120, 640)
         + P.marca(70, 64) + '<div class="foot" style="right:70px;top:74px">Producto de la semana</div>'
         + '<div style="position:absolute;left:70px;top:150px"><div class="h" style="font-size:150px;line-height:.9">Todo en</div>'
           f'<div class="h" style="font-size:150px;line-height:.9;color:{OR}">un scoop.</div></div>'
         + '<div style="position:absolute;left:70px;right:70px;bottom:70px;display:flex;justify-content:space-between;align-items:flex-end">'
           '<div><div class="lab" style="color:#d8d3cb">MuscleTech Nitro Tech · 4 lb · Vainilla</div>'
           '<div style="font-size:34px;color:#c9c4bc;margin-top:10px;font-weight:500">30 g de proteína + 3 g de creatina por porción.</div></div>'
           f'<div style="width:90px;height:2px;background:{OR};margin-bottom:18px"></div></div>')
    return P.page(W, H, b, 'rgba(0,0,0,0)')


def h_haz():
    SW, SH = 1080, 1920
    b = (set_haz(SW, SH, 1580, 600, 420, ang=16, ancho=440)
         + producto(600, 1580, 860)
         + P.marca(70, 150)
         + '<div style="position:absolute;left:70px;top:290px"><div class="lab">Producto de la semana</div>'
           '<div class="h" style="font-size:170px;line-height:.9;margin-top:20px">Proteína.</div>'
           f'<div class="h" style="font-size:170px;line-height:.9;color:{OR}">+ Creatina.</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Nitro Tech 4 lb · 30 g + 3 g por scoop · Pídela por DM</div>')
    return P.page(SW, SH, b, 'rgba(0,0,0,0)')


def h_encuesta():
    SW, SH = 1080, 1920
    # producto abajo a la derecha, recortado por el borde; espacio libre para el sticker ~700–1050 al centro
    b = (set_haz(SW, SH, 1560, 830, ang=12, ancho=420)
         + producto(830, 1560, 560)
         + P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:300px;text-align:center"><div class="lab">Nitro Tech · Vainilla</div>'
           '<div class="h" style="font-size:180px;line-height:.92;margin-top:22px">¿Ya la</div>'
           f'<div class="h" style="font-size:180px;line-height:.92;color:{OR}">probaste?</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">30 g + 3 g de creatina · Pídela por DM</div>')
    return P.page(SW, SH, b, 'rgba(0,0,0,0)')


if __name__ == '__main__':
    P.render([('1_nitro_tech_todo_en_un_scoop', feed())], FEED_OUT, 1080, 1350)
    P.render([('1_proteina_mas_creatina', h_haz()), ('2_ya_la_probaste', h_encuesta())], HIST_OUT, 1080, 1920)
