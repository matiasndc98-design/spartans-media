"""Reel 9:16 (15 s, estilo SOBRIO) · jueves 26 nov 2026, "Detrás de la tienda": "¿Es original?"
Tipo nuevo: PROFUNDIDAD 2.5D / PARALLAX (tendencia 2026 de video de producto en capas: palabra gigante al fondo,
envase al medio y una capa desenfocada adelante que se mueven a distinta velocidad mientras la cámara avanza).
Mensaje real de la tienda: productos originales y sellados. Gancho completo desde el cuadro 0. Cada producto 2,5 s,
un solo dato del envase. Cierre: la fila de los 4 + DM. Llamado a envíos ("Mándaselo a quien entrena contigo. Guárdalo.").
Sin precios, sin numeración, sin chistes. Sonido original: solo efectos (sonido.py), la música la pone el dueño.
Uso (desde kit/build): python3 reel_original_sellado.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

STEP = 2.5
BASE_Y = 1500
R.DUR = STEP * 6  # 15 s

# img, alto, palabra de fondo, titular (2 partes), dato, glow, capa delantera desenfocada
PRODS = [
    ('p_whey.png', 860, 'ORIGINAL', ('Original.', ''), 'Whey USN · 5 lb · 22 g por scoop', 'rgba(150,80,30,.22)', 'p_iso100.png'),
    ('p_iso100.png', 820, 'SELLADO', ('Sellado.', ''), 'Dymatize ISO 100 · 5 lb · 71 porciones', 'rgba(60,110,170,.22)', 'p_nitro.png'),
    ('p_nitro.png', 860, 'FÁBRICA', ('De ', 'fábrica.'), 'MuscleTech Nitro Tech · 4 lb · 30 g por scoop', 'rgba(242,106,27,.18)', 'p_finaflex.png'),
    ('p_finaflex.png', 800, 'NSF', ('Certificada.', ''), 'Creatina Finaflex 1 kg · NSF Contents Certified', 'rgba(200,200,210,.14)', 'p_whey.png'),
]
FILA = [('p_whey.png', 175, 420), ('p_iso100.png', 420, 400), ('p_nitro.png', 665, 420), ('p_finaflex.png', 905, 380)]


def scene_css():
    return P.CSS + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden}}
.sc{{position:absolute;inset:0;opacity:0}}
@keyframes win{{0%{{opacity:1}}100%{{opacity:1}}}}
@keyframes slam{{0%{{transform:scale(1.16);opacity:.15}}35%{{transform:scale(.99);opacity:1}}60%,100%{{transform:scale(1);opacity:1}}}}
@keyframes fondo{{0%{{transform:translateX(60px) scale(1)}}100%{{transform:translateX(-60px) scale(1.05)}}}}
@keyframes medio{{0%{{transform:scale(1) translateX(-14px)}}100%{{transform:scale(1.09) translateX(14px)}}}}
@keyframes rise{{0%{{transform:translateX(140px)}}100%{{transform:translateX(-180px)}}}}
@keyframes flash{{0%{{opacity:.22}}100%{{opacity:0}}}}
.bigw{{position:absolute;left:-200px;right:-200px;top:560px;text-align:center;font-family:Bebas;font-size:560px;line-height:.8;
  color:transparent;-webkit-text-stroke:2px rgba(244,241,236,.10);letter-spacing:6px}}
.front{{position:absolute;right:-420px;top:1180px;height:1100px;filter:blur(16px) brightness(.32);opacity:.9}}
.cut{{position:absolute;inset:0;background:#f4f1ec;opacity:0;z-index:20}}
.tit{{position:absolute;left:0;right:0;top:300px;text-align:center}}
.pie{{position:absolute;top:1620px;left:0;right:0;text-align:center;font-weight:600;font-size:26px;letter-spacing:4px;text-transform:uppercase;color:#d8d3cc}}
"""


def escena(t0, dur, contenido, ultima=False):
    return f'<div class="sc" style="animation:win {dur}s linear {t0}s {"forwards" if ultima else "none"}">{contenido}</div>'


def fondo(glow):
    return P.page(R.W, R.H, '', glow).split('<body>')[1].split('<div class="grain">')[0]


def capas(t, palabra, img, alto, front):
    """Tres capas a distinta velocidad: palabra al fondo, envase al medio, envase desenfocado adelante."""
    return (f'<div class="bigw" style="animation:fondo {STEP}s linear {t}s both">{palabra}</div>'
            f'<div style="position:absolute;inset:0;transform-origin:540px {BASE_Y}px;animation:medio {STEP}s linear {t}s both">'
            f'{P.heroe(img, 540, BASE_Y, alto)}</div>'
            f'<img class="front" src="{P.I(front)}" style="animation:rise {STEP}s linear {t}s both">')


def body():
    b = ''
    # Gancho legible desde el cuadro 0: sin animación de entrada en el titular
    b += escena(0, STEP, fondo('rgba(242,106,27,.08)') + capas(0, 'SPARTANS', 'p_whey.png', 620, 'p_finaflex.png')
                + '''<div class="tit"><div class="lab" style="color:#d8d3cc">Detrás de la tienda</div>
 <div class="h" style="font-size:220px;margin-top:22px">¿Es</div>
 <div class="h o" style="font-size:220px">original?</div></div>
<div class="pie">Todo lo que vendemos <span class="o">·</span> Mira</div>''')
    for i, (img, alto, palabra, tit, dato, glow, front) in enumerate(PRODS):
        t = STEP * (i + 1)
        s1, s2 = tit
        fs = 230 if len(s1 + s2) <= 9 else 190
        h = (f'<div class="h" style="font-size:{fs}px;margin-top:20px;animation:slam .45s ease-out {t + .1}s both">'
             + (f'{s1}<span class="o">{s2}</span></div>' if s2 else f'<span class="o">{s1}</span></div>'))
        b += (f'<div class="cut" style="animation:flash .3s ease-out {t}s"></div>'
              + escena(t, STEP, fondo(glow) + capas(t, palabra, img, alto, front)
                       + f'<div class="tit"><div class="lab">Original y sellado</div>{h}</div>'
                       + f'<div class="pie">{dato}</div>'))
    # Cierre: la fila de los 4
    t = STEP * 5
    fila = ''.join(P.heroe(img, cx, BASE_Y, alto) for img, cx, alto in FILA)
    b += (f'<div class="cut" style="animation:flash .3s ease-out {t}s"></div>'
          + escena(t, STEP, fondo('rgba(242,106,27,.12)')
                   + f'<div class="bigw" style="animation:fondo {STEP}s linear {t}s both">SELLADO</div>'
                   + f'<div style="position:absolute;inset:0;transform-origin:540px {BASE_Y}px;animation:medio {STEP}s linear {t}s both">{fila}</div>'
                   + f'''<div class="tit"><div class="lab" style="color:#d8d3cc">Siempre</div>
 <div class="h" style="font-size:200px;margin-top:22px;animation:slam .45s ease-out {t + .1}s both">Original</div>
 <div class="h o" style="font-size:200px">y sellado.</div></div>
<div style="position:absolute;left:0;right:0;top:1600px;text-align:center;font-weight:600;font-size:28px;letter-spacing:6px;text-transform:uppercase">
 Pídelo por DM <span class="o">·</span> Delivery en Caldera $1.500</div>
<div style="position:absolute;left:0;right:0;top:1652px;text-align:center;font-weight:500;font-size:25px;letter-spacing:3px;text-transform:uppercase;color:#a9a39b">
 Mándaselo a quien entrena contigo <span class="o">·</span> Guárdalo</div>''', ultima=True))
    b += P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px">Detrás de la tienda</div>'
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
