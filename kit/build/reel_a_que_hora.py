"""Reel 9:16 (15 s, estilo SOBRIO) · martes 10 nov 2026, semana de la creatina: "¿A qué hora se toma?"
Tipo nuevo: LOOP PERFECTO con cortes duros (idea de los reels "seamless loop" de 2026: el último cuadro calza con el
primero, así el reel vuelve a empezar sin que se note y suma tiempo de visualización). El cierre repite el encuadre
del gancho (mismo tarro, mismo lugar) y deja la pregunta "¿Y tú, a qué hora?" que empalma con "¿A qué hora se toma?".
Gancho completo desde el cuadro 0. Cada producto 2,5 s. Sin precios, sin numeración, sin chistes, horas en 12 h.
Respaldo: la creatina sirve a cualquier hora; lo que cuenta es tomarla todos los días (CLAUDE.md, reglas de confianza).
Sonido original: solo efectos (sonido.py), la música la pone el dueño.
Uso (desde kit/build): python3 reel_a_que_hora.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

OR = R.OR
STEP = 2.5
BASE_Y = 1560
HORAS = [  # imagen, alto, hora, etiqueta, brillo
    ('p_usn_crea.png', 700, '7 AM', 'Creatina USN · 300 g', 'rgba(242,106,27,.12)'),
    ('p_mt_uva.png', 720, '2 PM', 'MuscleTech Platinum · Uva', 'rgba(120,60,170,.16)'),
    ('p_finaflex.png', 760, '10 PM', 'Finaflex · 1 kg', 'rgba(242,106,27,.10)'),
]
T1 = STEP                       # inicio de las horas
T2 = T1 + STEP * len(HORAS)     # 10: "Cualquier hora."
T3 = T2 + STEP                  # 12,5: cierre en loop
R.DUR = T3 + STEP               # 15 s


def scene_css():
    return P.CSS + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden}}
.sc{{position:absolute;inset:0;opacity:0}}
@keyframes win{{0%{{opacity:1}}100%{{opacity:1}}}}
@keyframes slam{{0%{{transform:scale(1.18);opacity:.2}}35%{{transform:scale(.99);opacity:1}}60%,100%{{transform:scale(1);opacity:1}}}}
@keyframes rise{{0%{{transform:translateY(30px)}}100%{{transform:translateY(0)}}}}
@keyframes push{{0%{{transform:scale(1)}}100%{{transform:scale(1.05)}}}}
.tit{{position:absolute;left:0;right:0;top:330px;text-align:center}}
"""


def fondo(glow):
    return (f'<div class="stage"></div><div style="position:absolute;inset:0;background:radial-gradient(ellipse 50% 35% at 50% 58%,{glow},transparent 70%)"></div>'
            f'<div class="floor" style="height:{int(R.H * .30)}px"></div>')


def escena(t0, dur, contenido, ultima=False):
    # corte duro: visible solo dentro de su tramo (fill none); la última queda hasta el final
    return f'<div class="sc" style="animation:win {dur}s linear {t0}s {"forwards" if ultima else "none"}">{contenido}</div>'


def tarro_gancho(t0, dur):
    # mismo encuadre en el gancho y en el cierre (loop)
    return f'<div style="position:absolute;inset:0;transform-origin:540px {BASE_Y}px;animation:push {dur}s linear {t0}s both">{P.heroe("p_mt_sin.png", 540, BASE_Y, 760)}</div>'


def body():
    b = ''
    # Gancho (cuadro 0 completo, sin animación de entrada)
    b += escena(0, STEP, fondo('rgba(242,106,27,.12)') + tarro_gancho(0, STEP) + '''<div class="tit">
 <div class="lab" style="color:#d8d3cc">Creatina</div>
 <div class="h" style="font-size:190px;margin-top:22px">¿A qué hora</div>
 <div class="h o" style="font-size:190px">se toma?</div></div>''')
    # Horas: corte duro, número enorme
    for k, (img, alto, hora, lab, glow) in enumerate(HORAS):
        t = T1 + k * STEP
        b += escena(t, STEP, fondo(glow)
                    + f'<div style="position:absolute;inset:0;animation:rise .5s ease-out {t}s both">{P.heroe(img, 540, BASE_Y, alto)}</div>'
                    + f'''<div class="tit"><div class="lab">{lab}</div>
 <div class="h" style="font-size:300px;margin-top:18px;animation:slam .45s ease-out {t}s both">{hora}</div>
 <div class="h o" style="font-size:96px;margin-top:4px">Sirve.</div></div>''')
    # Cualquier hora: las 4 juntas
    t = T2
    cuatro = (P.heroe('p_usn_crea.png', 170, BASE_Y, 400) + P.heroe('p_finaflex.png', 920, BASE_Y, 450)
              + P.heroe('p_mt_uva.png', 395, BASE_Y + 20, 480) + P.heroe('p_mt_sin.png', 680, BASE_Y + 20, 480))
    b += escena(t, STEP, fondo('rgba(242,106,27,.10)')
                + f'<div style="position:absolute;inset:0;animation:rise .5s ease-out {t}s both">{cuatro}</div>'
                + f'''<div class="tit"><div class="lab">La respuesta</div>
 <div class="h" style="font-size:170px;margin-top:22px;animation:slam .45s ease-out {t}s both">Cualquier hora.</div>
 <div class="h o" style="font-size:170px">Todos los días.</div>
 <div style="font-size:40px;color:#c9c4bc;margin-top:34px;font-weight:500">5 g al día. Lo que cuenta es la constancia.</div></div>''')
    # Cierre = encuadre del gancho (empalma con el cuadro 0 al repetirse)
    t = T3
    b += escena(t, STEP, fondo('rgba(242,106,27,.12)') + tarro_gancho(t, STEP) + f'''<div class="tit">
 <div class="lab" style="color:#d8d3cc">Responde: mañana, tarde o noche</div>
 <div class="h" style="font-size:190px;margin-top:22px;animation:slam .45s ease-out {t}s both">¿Y tú,</div>
 <div class="h o" style="font-size:190px">a qué hora?</div></div>
<div style="position:absolute;left:0;right:0;bottom:290px;text-align:center;font-weight:600;font-size:28px;letter-spacing:6px;text-transform:uppercase">
 Pídela por DM <span class="o">·</span> Delivery en Caldera $1.500</div>''', ultima=True)
    b += P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px">Semana de la creatina</div>'
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
