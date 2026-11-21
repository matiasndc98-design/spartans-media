"""Reel 9:16 (15 s, estilo SOBRIO) · sábado 21 nov 2026: "Lo básico no descansa."
Tipo nuevo: FORMATO CINE + CORTE POR FORMA (tendencia "skinny cinematic reels" 2026: la imagen vive en una franja
panorámica con negro arriba y abajo; cada producto entra con un corte duro al MISMO punto del encuadre, con un
obturador que cierra y abre la franja, y un acercamiento lento continuo que no se corta entre tomas).
Gancho completo desde el cuadro 0 (fila de 4 en la franja + titular). Cada producto 2,5 s con un solo dato.
Cierre: la misma fila del gancho (empalma al repetirse). Llamado de una palabra, 2 opciones (SÍ o NO).
Sin precios, sin numeración, sin chistes. Sonido original: solo efectos (sonido.py), la música la pone el dueño.
Uso (desde kit/build): python3 reel_cine_base.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

STEP = 2.5
R.DUR = STEP * 6  # 15 s
TOP, ALTO = 680, 720          # franja de cine
BASE = 600                    # piso dentro de la franja

PRODS = [  # img, alto, etiqueta, titular, dato, glow
    ('p_multi.png', 500, 'Multivitamínico USN', 'Vitaminas.', '2 tabletas por porción · 30 porciones', 'rgba(242,106,27,.14)'),
    ('p_omega.png', 520, 'Omega 3 USN', 'Omega 3.', '1000 mg · 90 cápsulas blandas', 'rgba(230,170,40,.14)'),
    ('p_mt_uva.png', 500, 'Creatina MuscleTech Platinum', 'Creatina.', 'Uva · 5 g · 60 porciones', 'rgba(120,60,170,.18)'),
    ('p_barra.png', 0, 'Barra Space Protein XXL', 'Proteína.', 'Coco · 36% proteína · 3 g de azúcar', 'rgba(60,120,200,.16)'),
]
FILA = [('p_multi.png', 150, 340), ('p_omega.png', 370, 400), ('p_mt_uva.png', 620, 380)]


def scene_css():
    return P.CSS + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden;background:#060504}}
.sc{{position:absolute;inset:0;opacity:0;background:#060504}}
@keyframes win{{0%{{opacity:1}}100%{{opacity:1}}}}
@keyframes slam{{0%{{transform:scale(1.14);opacity:.25}}35%{{transform:scale(.99);opacity:1}}60%,100%{{transform:scale(1);opacity:1}}}}
@keyframes rise{{0%{{height:{ALTO // 2}px}}100%{{height:0}}}}
@keyframes push{{0%{{transform:scale(var(--a))}}100%{{transform:scale(var(--b))}}}}
.band{{position:absolute;left:0;right:0;top:{TOP}px;height:{ALTO}px;overflow:hidden}}
.lid{{position:absolute;left:0;right:0;height:0;background:#060504;z-index:5}}
.tit{{position:absolute;left:0;right:0;top:300px;text-align:center}}
.pie{{position:absolute;top:{TOP + ALTO + 70}px;left:0;right:0;text-align:center}}
.dato{{font-weight:600;font-size:28px;letter-spacing:4px;text-transform:uppercase;color:#d8d3cc}}
"""


def escena(t0, dur, contenido, ultima=False):
    return f'<div class="sc" style="animation:win {dur}s linear {t0}s {"forwards" if ultima else "none"}">{contenido}</div>'


def estudio(glow):
    return ('<div style="position:absolute;inset:0;background:radial-gradient(ellipse 45% 70% at 50% 55%,#2c2622 0%,#15110e 55%,#0a0807 100%)"></div>'
            f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse 40% 45% at 50% 60%,{glow},transparent 70%)"></div>'
            f'<div style="position:absolute;left:0;right:0;top:{BASE}px;bottom:0;background:linear-gradient(180deg,rgba(255,255,255,.035),rgba(0,0,0,.55))"></div>')


def band(t, i, glow, contenido, obturador=True):
    """Franja de cine con acercamiento continuo (escala sigue de una toma a la otra) y obturador en el corte."""
    a, b = (1 + .025 * i, 1 + .025 * (i + 1)) if 0 < i < 5 else (1, 1.03)
    lids = ''
    if obturador:
        lids = (f'<div class="lid" style="top:0;animation:rise .32s cubic-bezier(.2,.8,.2,1) {t}s both"></div>'
                f'<div class="lid" style="bottom:0;animation:rise .32s cubic-bezier(.2,.8,.2,1) {t}s both"></div>')
    return (f'<div class="band">{estudio(glow)}'
            f'<div style="position:absolute;inset:0;transform-origin:50% 75%;--a:{a};--b:{b};animation:push {STEP}s linear {t}s both">{contenido}</div>'
            f'{lids}</div>'
            f'<div style="position:absolute;left:0;right:0;top:{TOP}px;height:1px;background:rgba(255,230,210,.10)"></div>'
            f'<div style="position:absolute;left:0;right:0;top:{TOP + ALTO}px;height:1px;background:rgba(255,230,210,.10)"></div>')


def barra(cx, base, w, rot=-8):
    src = P.I('p_barra.png')
    return (f'<img class="prod" src="{src}" style="left:{cx}px;top:{base}px;width:{w}px;transform:translate(-50%,-100%) rotate({rot}deg)">')


def fila():
    h = ''.join(P.heroe(img, cx, BASE, alto) for img, cx, alto in FILA)
    return h + barra(880, BASE - 10, 250, -10)


def body():
    b = ''
    # Gancho: la fila completa en la franja + titular, legible desde el cuadro 0 (sin animación de entrada)
    b += escena(0, STEP, band(0, 0, 'rgba(242,106,27,.10)', fila(), obturador=False)
                + '''<div class="tit"><div class="lab" style="color:#d8d3cc">Sábado</div>
 <div class="h" style="font-size:150px;margin-top:20px">Lo básico</div>
 <div class="h o" style="font-size:150px">no descansa.</div></div>
<div class="pie"><div class="dato">Cuatro básicos <span class="o">·</span> Todos los días</div></div>''')
    for i, (img, alto, lab, tit, dato, glow) in enumerate(PRODS):
        t = STEP * (i + 1)
        prod = barra(540, BASE - 40, 760) if img == 'p_barra.png' else P.heroe(img, 540, BASE, alto)
        b += escena(t, STEP, band(t, i + 1, glow, prod)
                    + f'<div class="tit" style="top:330px"><div class="lab">{lab}</div>'
                      f'<div class="h o" style="font-size:190px;margin-top:22px;animation:slam .45s ease-out {t + .25}s both">{tit}</div></div>'
                    + f'<div class="pie"><div class="dato">{dato}</div></div>')
    t = STEP * 5
    b += escena(t, STEP, band(t, 5, 'rgba(242,106,27,.12)', fila())
                + f'''<div class="tit"><div class="lab" style="color:#d8d3cc">Responde SÍ o NO</div>
 <div class="h" style="font-size:150px;margin-top:20px;animation:slam .45s ease-out {t + .2}s both">¿Tienes</div>
 <div class="h o" style="font-size:150px">tu base?</div></div>
<div class="pie"><div style="font-weight:600;font-size:28px;letter-spacing:6px;text-transform:uppercase">Pídelo por DM <span class="o">·</span> Delivery en Caldera $1.500</div></div>''', ultima=True)
    b += P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px">Lo de todos los días</div>'
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
