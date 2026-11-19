"""Reel 9:16 (15 s, estilo SOBRIO) · jueves 19 nov 2026, semana de la proteína: "Elige tu sabor."
Tipo nuevo: BARRIDO DE LUZ / REVELADO EN SILUETA (idea de los "light sweep reveal" de lanzamientos de autos y
marcas grandes: el envase parte en silueta negra con luz de contorno y una franja de luz lo cruza y lo enciende).
Gancho completo desde el cuadro 0 (fila de 4 siluetas + titular). Cada producto 2,5 s, un solo dato: su sabor.
Cierre: la misma fila, ahora encendida (empalma con el gancho al repetirse). Llamado de una palabra, 2 opciones.
Sin precios, sin numeración, sin chistes. Sonido original: solo efectos (sonido.py), la música la pone el dueño.
Uso (desde kit/build): python3 reel_elige_sabor.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

STEP = 2.5
BASE_Y = 1540
R.DUR = STEP * 6  # 15 s

PRODS = [  # img, alto, sabor (2 líneas), dato, glow
    ('p_whey.png', 820, ('Chocolate.', ''), 'Whey USN · 22 g por scoop', 'rgba(150,80,30,.20)'),
    ('p_iso100.png', 780, ('Cocoa', 'Pebbles.'), 'ISO 100 · 25 g por scoop', 'rgba(60,110,170,.20)'),
    ('p_nitro.png', 820, ('Vainilla.', ''), 'Nitro Tech · 30 g + 3 g de creatina', 'rgba(242,106,27,.16)'),
    ('p_barra.png', 240, ('Coco.', ''), 'Barra Space Protein XXL · 36% proteína', 'rgba(120,170,220,.16)'),
]
FILA = [('p_whey.png', 225, 400, -40), ('p_iso100.png', 540, 385, -40), ('p_nitro.png', 855, 400, -40), ('p_barra.png', 540, 95, 40)]


def scene_css():
    return P.CSS + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden}}
.sc{{position:absolute;inset:0;opacity:0}}
@keyframes win{{0%{{opacity:1}}100%{{opacity:1}}}}
@keyframes slam{{0%{{transform:scale(1.18);opacity:.2}}35%{{transform:scale(.99);opacity:1}}60%,100%{{transform:scale(1);opacity:1}}}}
@keyframes enciende{{0%{{filter:brightness(.07) contrast(1.2)}}100%{{filter:brightness(1) contrast(1)}}}}
@keyframes inL{{0%{{transform:translateX(-1300px) skewX(-18deg)}}100%{{transform:translateX(1300px) skewX(-18deg)}}}}
@keyframes push{{0%{{transform:scale(1)}}100%{{transform:scale(1.04)}}}}
.sil img{{filter:brightness(.07) contrast(1.2)}}
.sil{{filter:drop-shadow(0 0 2px rgba(242,140,80,.55)) drop-shadow(0 0 18px rgba(242,106,27,.18))}}
.band{{position:absolute;top:0;bottom:0;left:340px;width:400px;background:linear-gradient(90deg,transparent,rgba(255,236,210,.16) 45%,rgba(255,236,210,.22) 50%,rgba(255,236,210,.16) 55%,transparent);mix-blend-mode:screen}}
.tit{{position:absolute;left:0;right:0;top:330px;text-align:center}}
.pie{{position:absolute;top:1650px;left:0;right:0;text-align:center;font-weight:600;font-size:26px;letter-spacing:4px;text-transform:uppercase;color:#d8d3cc}}
"""


def escena(t0, dur, contenido, ultima=False):
    return f'<div class="sc" style="animation:win {dur}s linear {t0}s {"forwards" if ultima else "none"}">{contenido}</div>'


def fondo(glow):
    return P.page(R.W, R.H, '', glow).split('<body>')[1].split('<div class="grain">')[0]


def fila(sil):
    h = ''.join(P.heroe(img, cx, BASE_Y + dy, alto) for img, cx, alto, dy in FILA)
    return f'<div class="{"sil" if sil else ""}" style="position:absolute;inset:0">{h}</div>'


def body():
    b = ''
    # Gancho: fila de 4 siluetas con luz de contorno + titular, legible desde el cuadro 0
    b += escena(0, STEP, fondo('rgba(242,106,27,.06)')
                + f'<div style="position:absolute;inset:0;animation:push {STEP}s linear 0s both">{fila(True)}</div>'
                + '''<div class="tit"><div class="lab" style="color:#d8d3cc">Proteína</div>
 <div class="h" style="font-size:230px;margin-top:22px">Elige tu</div>
 <div class="h o" style="font-size:230px">sabor.</div></div>
<div class="pie">Cuatro opciones <span class="o">·</span> Una es la tuya</div>''')
    # Un producto por tramo: parte en silueta, la franja de luz lo cruza y lo enciende
    for i, (img, alto, sabor, dato, glow) in enumerate(PRODS):
        t = STEP * (i + 1)
        cx = 560 if img != 'p_barra.png' else 540
        rot = -8 if img == 'p_barra.png' else 0
        base = BASE_Y - (60 if img == 'p_barra.png' else 0)
        s1, s2 = sabor
        tit = (f'<div class="h" style="font-size:{200 if s2 else 230}px;margin-top:20px;animation:slam .45s ease-out {t + .35}s both">'
               + (f'{s1}</div><div class="h o" style="font-size:200px">{s2}</div>' if s2 else f'<span class="o">{s1}</span></div>'))
        b += escena(t, STEP, fondo(glow)
                    + f'<div style="position:absolute;inset:0;animation:enciende .55s ease-out {t + .1}s both">{P.heroe(img, cx, base, alto, rot)}</div>'
                    + f'<div class="band" style="animation:inL .7s ease-in-out {t}s both"></div>'
                    + f'<div class="tit" style="top:300px"><div class="lab">Sabor</div>{tit}</div>'
                    + f'<div class="pie">{dato}</div>')
    # Cierre: la misma fila del gancho, ahora encendida
    t = STEP * 5
    b += escena(t, STEP, fondo('rgba(242,106,27,.10)')
                + f'<div style="position:absolute;inset:0;animation:enciende .5s ease-out {t}s both">{fila(False)}</div>'
                + f'<div class="band" style="animation:inL .7s ease-in-out {t}s both"></div>'
                + f'''<div class="tit"><div class="lab" style="color:#d8d3cc">Responde con una palabra</div>
 <div class="h" style="font-size:180px;margin-top:22px;animation:slam .45s ease-out {t + .2}s both">¿Chocolate</div>
 <div class="h o" style="font-size:180px">o vainilla?</div></div>
<div style="position:absolute;left:0;right:0;top:1650px;text-align:center;font-weight:600;font-size:28px;letter-spacing:6px;text-transform:uppercase">
 Pídela por DM <span class="o">·</span> Delivery en Caldera $1.500</div>''', ultima=True)
    b += P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px">Semana de la proteína</div>'
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
