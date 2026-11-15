"""Lunes 16 nov 2026 · semana de la proteína (2ª vuelta) · estilo SOBRIO.
Carrusel 4:5 "Se suma." con idea nueva TEXTO DETRÁS DEL PRODUCTO (efecto de profundidad de portada de revista /
campaña de marca grande: una palabra gigante de fondo y el envase parado delante, tapando la parte baja de las letras).
Tono "consistency compounds" de Gymshark: scoop a scoop, se suma (sin prometer cambios físicos).
Historias 9:16: "Lunes." Whey USN (texto detrás) + encuesta "¿Agua o leche?".
Sin precios. Uso (desde kit/build): python3 lunes_se_suma.py <carpeta_feed> <carpeta_historias>
"""
import sys
FEED = sys.argv[1] if len(sys.argv) > 1 else 'feed'
HIST = sys.argv[2] if len(sys.argv) > 2 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

W, H, N = 1080, 1350, 6

# ajusta cada palabra gigante al ancho disponible (antes de marcar la página como lista)
FIT = """<script>document.fonts.ready.then(()=>{document.querySelectorAll('.big').forEach(e=>{
const max=+e.dataset.w;let s=+e.dataset.s;e.style.fontSize=s+'px';
while(e.scrollWidth>max&&s>60){s-=4;e.style.fontSize=s+'px';}});});</script>"""


def big(word, top, maxw, size, color='#f4f1ec', cx=None, w=W):
    return (f'<div class="h big" data-w="{maxw}" data-s="{size}" style="position:absolute;left:{w // 2}px;transform:translateX(-50%);'
            f'top:{top}px;display:inline-block;white-space:nowrap;color:{color};line-height:.8">{word}</div>')


def num(i):
    return f'<div class="foot" style="right:70px;top:74px">{i:02d} / 0{N}</div>'


def lamina(i, word, img, alto, lab, dato, glow, color='#f4f1ec'):
    b = (FIT + P.marca(70, 64) + num(i)
         + big(word, 270, 960, 460, color)
         + P.heroe(img, 540, 1120, alto)
         + f'<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center"><div class="lab">{lab}</div>'
           f'<div class="h" style="font-size:64px;margin-top:12px">{dato}</div></div>')
    return P.page(W, H, b, glow)


def portada():
    b = (FIT + P.marca(70, 64) + num(1)
         + '<div class="lab" style="position:absolute;left:0;right:0;top:200px;text-align:center">Semana de la proteína</div>'
         + big('Proteína', 290, 980, 400)
         + P.heroe('p_whey.png', 540, 1120, 760)
         + '<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center">'
           '<div class="h" style="font-size:84px">Scoop a scoop. <span class="o">Se suma.</span></div>'
           '<div class="foot" style="position:static;margin-top:16px">Desliza</div></div>')
    return P.page(W, H, b, 'rgba(242,106,27,.12)')


def barra():
    b = (FIT + P.marca(70, 64) + num(5)
         + big('Al paso', 270, 960, 460)
         + f'<img class="prod" src="{P.I("p_barra.png")}" style="left:540px;top:690px;width:860px;transform:translate(-50%,-50%) rotate(-14deg)">'
         + '<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center"><div class="lab">Space Protein XXL · 80 g · Coco</div>'
           '<div class="h" style="font-size:64px;margin-top:12px">36% proteína. <span class="o">3 g de azúcar.</span></div></div>')
    return P.page(W, H, b, 'rgba(120,170,220,.12)')


def cierre():
    b = (P.marca(70, 64) + num(6)
         + '<div style="position:absolute;left:0;right:0;top:170px;text-align:center"><div class="lab">Spartans</div>'
           '<div class="h" style="font-size:170px;margin-top:16px">Se suma.</div>'
           '<div class="h o" style="font-size:84px;margin-top:10px">¿Cuál va en tu shaker?</div>'
           '<div class="h" style="font-size:64px;margin-top:14px;color:#cfcac2">1, 2, 3 o 4.</div></div>'
         + P.heroe('p_iso100.png', 300, 1130, 430) + P.heroe('p_whey.png', 540, 1150, 480) + P.heroe('p_nitro.png', 780, 1130, 430)
         + '<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center;font-weight:600;font-size:26px;letter-spacing:6px;text-transform:uppercase">'
           'Pídela por DM <span class="o">·</span> Con creatina, shaker de regalo</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.10)')


FEED_P = [
    ('1_proteina_se_suma', portada()),
    ('2_whey_clasico', lamina(2, 'Clásico', 'p_whey.png', 780, 'Whey USN · 5 lb · Chocolate', '22 g <span class="o">por scoop.</span>', 'rgba(242,106,27,.12)')),
    ('3_iso100_isolate', lamina(3, 'Isolate', 'p_iso100.png', 800, 'Dymatize ISO 100 · 5 lb · Cocoa Pebbles', '25 g. <span class="o">71 porciones.</span>', 'rgba(60,110,170,.16)')),
    ('4_nitro_30g', lamina(4, '30 g', 'p_nitro.png', 780, 'MuscleTech Nitro Tech · 4 lb · Vainilla', '30 g <span class="o">+ 3 g de creatina.</span>', 'rgba(200,30,30,.12)')),
    ('5_barra_al_paso', barra()),
    ('6_se_suma', cierre()),
]

SW, SH = P.SW, P.SH


def h_lunes():
    b = (FIT + P.marca(70, 150)
         + '<div class="lab" style="position:absolute;left:0;right:0;top:330px;text-align:center">Semana de la proteína</div>'
         + big('Lunes', 440, 980, 520, w=SW)
         + P.heroe('p_whey.png', 540, 1430, 820)
         + '<div style="position:absolute;left:0;right:0;bottom:290px;text-align:center">'
           '<div class="h" style="font-size:84px">Se empieza <span class="o">hoy.</span></div>'
           '<div class="foot" style="position:static;margin-top:14px">Whey USN · 22 g por scoop · Pídelo por DM</div></div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.12)')


def h_encuesta():
    # espacio libre ~720–1080 para el sticker de encuesta
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Tu batido</div>'
           '<div class="h" style="font-size:180px;margin-top:26px">¿Agua</div><div class="h o" style="font-size:180px">o leche?</div></div>'
         + P.heroe('p_shaker.png', 400, 1580, 420) + P.heroe('p_whey.png', 660, 1580, 400)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Proteína + creatina · Shaker de regalo</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.07)')


if __name__ == '__main__':
    P.render(FEED_P, FEED, W, H)
    P.render([('1_lunes_se_empieza', h_lunes()), ('2_agua_o_leche', h_encuesta())], HIST, SW, SH)
