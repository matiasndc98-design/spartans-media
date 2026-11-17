"""Reel 9:16 (15 s, estilo SOBRIO) · martes 17 nov 2026, semana de la proteína: "¿Antes o después de entrenar?"
Tipo nuevo: PANTALLA DIVIDIDA (split screen "esto o esto", formato de comparación lado a lado que usan las marcas
en Reels 2026). Izquierda ANTES (ISO 100), derecha DESPUÉS (Nitro Tech), separadas por una línea naranja fina.
Cada lado se enciende 2,5 s mientras el otro se apaga; después la línea se cierra y queda la respuesta a pantalla
completa. El cierre vuelve al encuadre dividido del gancho (empalma al repetirse, como el loop del 10 nov).
Gancho completo desde el cuadro 0. Sin precios, sin numeración, sin chistes. 4 productos máximo, 2,5 s cada tramo.
Respaldo: ISSN (timing de nutrientes): antes o después sirven; lo que más pesa es la proteína total del día.
Llamado del 16 nov: una palabra, 2 opciones ("antes o después").
Sonido original: solo efectos (sonido.py), la música la pone el dueño.
Uso (desde kit/build): python3 reel_antes_o_despues.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

STEP = 2.5
BASE_Y = 1540
R.DUR = STEP * 6  # 15 s
GL_L = 'rgba(60,110,170,.20)'   # ISO 100
GL_R = 'rgba(242,106,27,.16)'   # Nitro Tech


def scene_css():
    return P.CSS + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden}}
.sc{{position:absolute;inset:0;opacity:0}}
@keyframes win{{0%{{opacity:1}}100%{{opacity:1}}}}
@keyframes slam{{0%{{transform:scale(1.18);opacity:.2}}35%{{transform:scale(.99);opacity:1}}60%,100%{{transform:scale(1);opacity:1}}}}
@keyframes rise{{0%{{transform:translateY(30px)}}100%{{transform:translateY(0)}}}}
@keyframes push{{0%{{transform:scale(1)}}100%{{transform:scale(1.04)}}}}
@keyframes dim{{0%{{opacity:0}}100%{{opacity:.78}}}}
@keyframes cierra{{0%{{transform:scaleY(1)}}100%{{transform:scaleY(0)}}}}
.tit{{position:absolute;left:0;right:0;top:330px;text-align:center}}
.half{{position:absolute;top:0;bottom:0;width:540px;overflow:hidden}}
.tag{{position:absolute;top:760px;left:0;right:0;text-align:center;font-family:Bebas;font-size:92px;letter-spacing:4px;line-height:1}}
.pie{{position:absolute;top:1650px;left:0;right:0;text-align:center;font-weight:600;font-size:26px;letter-spacing:4px;text-transform:uppercase;color:#d8d3cc}}
"""


def escena(t0, dur, contenido, ultima=False):
    return f'<div class="sc" style="animation:win {dur}s linear {t0}s {"forwards" if ultima else "none"}">{contenido}</div>'


def mitad(lado, glow, img, alto, tag, pie, t, apagada=False, pie_on=True):
    x = 0 if lado == 'L' else 540
    dim = f'<div style="position:absolute;inset:0;background:#060504;animation:dim .35s ease-out {t}s both"></div>' if apagada else ''
    return (f'<div class="half" style="left:{x}px"><div class="stage"></div>'
            f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse 70% 32% at 50% 64%,{glow},transparent 70%)"></div>'
            f'<div class="floor" style="height:{int(R.H * .30)}px"></div>'
            f'{P.heroe(img, 270, BASE_Y, alto)}'
            f'<div class="tag">{tag}</div>'
            + (f'<div class="pie">{pie}</div>' if pie_on else '') + f'{dim}</div>')


def dividida(t, apaga=None, tags=('Antes', 'Después'), pies=True):
    return (mitad('L', GL_L, 'p_iso100.png', 560, tags[0], 'ISO 100 · 25 g', t, apaga == 'L', pies)
            + mitad('R', GL_R, 'p_nitro.png', 600, f'<span class="o">{tags[1]}</span>', 'Nitro Tech · 30 g', t, apaga == 'R', pies)
            + '<div style="position:absolute;left:539px;top:300px;bottom:300px;width:2px;background:#F26A1B"></div>')


def body():
    b = ''
    # Gancho: encuadre dividido completo desde el cuadro 0
    b += escena(0, STEP, f'<div style="position:absolute;inset:0;animation:push {STEP}s linear 0s both">{dividida(0)}</div>'
                + '''<div class="tit"><div class="lab" style="color:#d8d3cc">Proteína</div>
 <div class="h" style="font-size:160px;margin-top:22px">¿Antes o después</div>
 <div class="h o" style="font-size:160px">de entrenar?</div></div>''')
    # Antes: se apaga la derecha
    t = STEP
    b += escena(t, STEP, dividida(t, apaga='R') + f'''<div class="tit"><div class="lab">Antes de entrenar</div>
 <div class="h" style="font-size:240px;margin-top:18px;animation:slam .45s ease-out {t}s both">Sirve.</div></div>''')
    # Después: se apaga la izquierda
    t = STEP * 2
    b += escena(t, STEP, dividida(t, apaga='L') + f'''<div class="tit"><div class="lab">Después de entrenar</div>
 <div class="h o" style="font-size:240px;margin-top:18px;animation:slam .45s ease-out {t}s both">Sirve.</div></div>''')
    # La respuesta: la línea se cierra, pantalla completa
    t = STEP * 3
    b += escena(t, STEP, P.page(R.W, R.H, '', 'rgba(242,106,27,.10)').split('<body>')[1].split('<div class="grain">')[0]
                + f'<div style="position:absolute;inset:0;animation:rise .5s ease-out {t}s both">{P.heroe("p_whey.png", 540, BASE_Y, 720)}</div>'
                + f'<div style="position:absolute;left:539px;top:300px;bottom:300px;width:2px;background:#F26A1B;transform-origin:50% 50%;animation:cierra .4s ease-in {t}s both"></div>'
                + f'''<div class="tit"><div class="lab">Lo que más cuenta</div>
 <div class="h" style="font-size:170px;margin-top:22px;animation:slam .45s ease-out {t}s both">El total</div>
 <div class="h o" style="font-size:170px">del día.</div>
 <div style="font-size:40px;color:#c9c4bc;margin-top:30px;font-weight:500">Las dos sirven. Tómala cuando te acomode.</div></div>
<div class="pie" style="position:absolute">Whey USN · 22 g por scoop</div>''')
    # Al paso también suma: barra
    t = STEP * 4
    b += escena(t, STEP, P.page(R.W, R.H, '', 'rgba(120,170,220,.14)').split('<body>')[1].split('<div class="grain">')[0]
                + f'<div style="position:absolute;inset:0;animation:rise .5s ease-out {t}s both">{P.heroe("p_barra.png", 540, BASE_Y - 60, 300, -8)}</div>'
                + f'''<div class="tit"><div class="lab">Y en el día</div>
 <div class="h" style="font-size:170px;margin-top:22px;animation:slam .45s ease-out {t}s both">Al paso</div>
 <div class="h o" style="font-size:170px">también suma.</div></div>
<div class="pie" style="position:absolute">Barra Space Protein XXL · 36% proteína</div>''')
    # Cierre = encuadre dividido del gancho (loop)
    t = STEP * 5
    b += escena(t, STEP, f'<div style="position:absolute;inset:0;animation:push {STEP}s linear {t}s both">{dividida(t, pies=False)}</div>'
                + f'''<div class="tit"><div class="lab" style="color:#d8d3cc">Responde con una palabra</div>
 <div class="h" style="font-size:160px;margin-top:22px;animation:slam .45s ease-out {t}s both">¿Y tú? ¿Antes</div>
 <div class="h o" style="font-size:160px">o después?</div></div>
<div style="position:absolute;left:0;right:0;top:1650px;text-align:center;font-weight:600;font-size:28px;letter-spacing:6px;text-transform:uppercase">
 Pídela por DM <span class="o">·</span> Delivery en Caldera $1.500</div>''', ultima=True)
    b += P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px">Semana de la proteína</div>'
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
