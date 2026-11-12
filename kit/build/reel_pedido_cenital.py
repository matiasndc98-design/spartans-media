"""Reel 9:16 (15 s, estilo SOBRIO) · jueves 12 nov 2026, "Detrás de la tienda" + semana de la creatina: "Así sale tu pedido."
Tipo nuevo: PEDIDO EN VISTA CENITAL (flat lay / knolling, idea de los reels "pack an order with me" de tiendas chicas):
mesa oscura vista desde arriba, los productos del combo real caen uno por uno y quedan ordenados en ángulo recto.
Gancho completo desde el cuadro 0 (con el Whey USN ya en la mesa). Cada producto 2,5 s. Sin precios, sin numeración, sin chistes.
Combo real: proteína + creatina = shaker C4 de regalo. Productos originales y sellados (CLAUDE.md).
Sonido original: solo efectos (sonido.py), la música la pone el dueño.
Uso (desde kit/build): python3 reel_pedido_cenital.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

OR = R.OR
STEP = 2.5
R.DUR = STEP * 6  # 15 s

# producto, centro x, borde superior y, alto, inicio de la caída
ITEMS = [
    ('p_whey.png', 330, 800, 640, None),
    ('p_finaflex.png', 800, 770, 390, STEP),
    ('p_shaker.png', 800, 1200, 360, STEP * 2),
]
# (inicio, etiqueta, línea 1, línea 2 naranja, apoyo)
TEXTOS = [
    (0, 'Detrás de la tienda', 'Así sale', 'tu pedido.', 'Whey USN · 5 lb · 22 g por scoop'),
    (STEP, 'Creatina', 'Creatina.', '5 g al día.', 'Finaflex · 1 kg · 200 porciones'),
    (STEP * 2, 'Llevando proteína + creatina', 'Shaker C4.', 'De regalo.', 'Promoción vigente'),
    (STEP * 3, 'El combo', 'Proteína + creatina.', 'Shaker de regalo.', 'Todo en un pedido'),
    (STEP * 4, 'Siempre', 'Original.', 'Sellado.', 'Revisa el sello cuando te llegue'),
    (STEP * 5, 'Responde SÍ', '¿Te armamos', 'el tuyo?', 'Pídelo por DM'),
]


def scene_css():
    return P.CSS + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden;background:#060504}}
.sc{{position:absolute;inset:0;opacity:0}}
@keyframes win{{0%,100%{{opacity:1}}}}
@keyframes slam{{0%{{transform:translate(-50%,0) scale(1.28);opacity:0}}45%{{transform:translate(-50%,0) scale(.98);opacity:1}}70%,100%{{transform:translate(-50%,0) scale(1);opacity:1}}}}
@keyframes rise{{0%{{transform:translateY(24px);opacity:0}}100%{{transform:translateY(0);opacity:1}}}}
@keyframes push{{0%{{transform:scale(1)}}100%{{transform:scale(1.06)}}}}
.mesa{{position:absolute;inset:0;background:
 radial-gradient(ellipse 62% 40% at 50% 62%,#34302b 0%,#211e1b 45%,#0c0b0a 85%,#060504 100%)}}
.it{{position:absolute;filter:drop-shadow(26px 34px 22px rgba(0,0,0,.82)) drop-shadow(6px 8px 4px rgba(0,0,0,.6))}}
.tit{{position:absolute;left:70px;right:70px;top:300px}}
"""


def mesa():
    out = '<div class="mesa"></div>'
    # línea fina naranja de "knolling": guía de alineación sobre la mesa
    out += f'<div style="position:absolute;left:70px;right:70px;top:1600px;height:2px;background:{OR};opacity:.55"></div>'
    for img, cx, top, h, t in ITEMS:
        anim = f'animation:slam .55s cubic-bezier(.2,.8,.2,1) {t}s both;' if t is not None else 'transform:translate(-50%,0);'
        out += (f'<img class="it" src="{P.I(img)}" style="left:{cx}px;top:{top}px;height:{h}px;'
                f'transform-origin:50% 50%;{anim}">')
    # empuje suave de cámara en el resumen y el cierre
    return f'<div style="position:absolute;inset:0;transform-origin:540px 1200px;animation:push {STEP * 3}s linear {STEP * 3}s both">{out}</div>'


def body():
    b = mesa()
    for k, (t, lab, l1, l2, apoyo) in enumerate(TEXTOS):
        ultima = k == len(TEXTOS) - 1
        fs = 118 if len(l1) > 14 else (150 if len(l2) > 12 else 190)
        b += (f'<div class="sc" style="animation:win {STEP}s linear {t}s {"forwards" if ultima else "none"}">'
              f'<div class="tit"><div class="lab">{lab}</div>'
              f'<div class="h" style="font-size:{fs}px;margin-top:20px">{l1}</div>'
              f'<div class="h o" style="font-size:{fs}px">{l2}</div>'
              f'<div style="font-size:38px;color:#c9c4bc;margin-top:24px;font-weight:500">{apoyo}</div></div></div>')
    # cierre: datos de entrega abajo
    b += (f'<div class="sc" style="animation:win {STEP}s linear {STEP * 5}s forwards">'
          '<div style="position:absolute;left:0;right:0;bottom:262px;text-align:center;font-weight:600;font-size:28px;'
          'letter-spacing:5px;text-transform:uppercase;color:#f4f1ec">Delivery en Caldera $1.500 <span class="o">·</span> Envíos a todo Chile</div></div>')
    b += P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px">Spartans · Caldera</div>'
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
