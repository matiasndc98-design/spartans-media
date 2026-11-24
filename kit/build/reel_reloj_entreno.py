"""Reel 9:16 (15 s, estilo SOBRIO) · martes 24 nov 2026, semana de la energía: "¿Cuánto antes de entrenar?"
Tipo nuevo: RELOJ QUE AVANZA (tendencia de reels con hora en pantalla tipo "timestamps": una hora gigante que gira
como reloj de paletas en cada corte y marca el momento; el producto aparece a su hora).
Gancho completo desde el cuadro 0 (pregunta + hora del entreno + los dos productos). Cada escena 2,5 s con un solo dato.
Dato: cafeína 30 a 60 minutos antes de entrenar (ISSN, posición sobre cafeína 2021). Lipo 6 y Guaraná se presentan como
alternativas ("uno de los dos"), nunca juntos. Nota de cafeína a la vista en cada escena con producto.
Cierre en loop al encuadre del gancho con una sola acción: mándaselo + guárdalo (ajuste del 23 nov).
Sin precios, sin numeración, sin chistes. Sonido original: solo efectos (sonido.py), la música la pone el dueño.
Uso (desde kit/build): python3 reel_reloj_entreno.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

STEP = 2.5
R.DUR = STEP * 6  # 15 s
BASE = 1400
NOTA = ('Contiene cafeína: Lipo 6 Black 222 mg por cápsula · Guaraná Shot 200 mg por shot. '
        'No apto para menores ni embarazadas.')


def scene_css():
    return P.CSS + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden;background:#060504}}
.sc{{position:absolute;inset:0;opacity:0;background:#060504}}
@keyframes win{{0%{{opacity:1}}100%{{opacity:1}}}}
@keyframes flip{{0%{{transform:perspective(900px) rotateX(-88deg);opacity:.2}}45%{{transform:perspective(900px) rotateX(8deg);opacity:1}}70%,100%{{transform:perspective(900px) rotateX(0);opacity:1}}}}
@keyframes slam{{0%{{transform:scale(1.12);opacity:.25}}35%{{transform:scale(.99);opacity:1}}60%,100%{{transform:scale(1);opacity:1}}}}
@keyframes drift{{0%{{transform:scale(1)}}100%{{transform:scale(1.035)}}}}
.reloj{{position:absolute;left:0;right:0;top:300px;text-align:center;transform-origin:50% 0%}}
.hora{{font-family:Bebas;font-size:300px;line-height:.85;letter-spacing:4px}}
.hora small{{font-size:130px;letter-spacing:6px;margin-left:18px}}
.tit{{position:absolute;left:0;right:0;text-align:center}}
.dato{{font-weight:600;font-size:28px;letter-spacing:4px;text-transform:uppercase;color:#d8d3cc}}
.nota{{position:absolute;left:90px;right:90px;bottom:262px;text-align:center;font-size:24px;line-height:1.45;color:#9b958d;letter-spacing:1px}}
"""


def escena(t0, contenido, ultima=False):
    return (f'<div class="sc" style="animation:win {STEP}s linear {t0}s {"forwards" if ultima else "none"}">'
            '<div class="stage"></div><div class="floor" style="height:600px"></div>'
            f'{contenido}<div class="nota">{NOTA}</div></div>')


def glow(c, y=62):
    return f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse 50% 32% at 50% {y}%,{c},transparent 70%)"></div>'


def reloj(t, hora, am_pm, lab, anim=True):
    a = f'animation:flip .5s cubic-bezier(.2,.8,.2,1) {t}s both' if anim else ''
    return (f'<div class="reloj" style="{a}"><div class="lab">{lab}</div>'
            f'<div class="hora" style="margin-top:20px">{hora}<small class="o">{am_pm}</small></div></div>')


def prod(t, contenido):
    return f'<div style="position:absolute;inset:0;transform-origin:50% 80%;animation:drift {STEP}s linear {t}s both">{contenido}</div>'


def par():
    return P.heroe('p_lipo.png', 380, BASE, 520) + P.heroe('p_guarana.png', 720, BASE, 560)


def body():
    b = ''
    # 0 · Gancho legible desde el cuadro 0 (sin animación de entrada)
    b += escena(0, glow('rgba(242,106,27,.12)') + prod(0, par())
                + '''<div class="tit" style="top:300px"><div class="lab">Entrenas a las 7 PM</div>
 <div class="h" style="font-size:165px;margin-top:22px">¿Cuánto antes</div>
 <div class="h o" style="font-size:165px">se toma?</div></div>''')
    # 1 · 6 PM · Lipo 6
    t = STEP
    b += escena(t, glow('rgba(242,106,27,.16)') + prod(t, P.heroe('p_lipo.png', 540, BASE, 500))
                + reloj(t, '6', 'PM', 'Una hora antes')
                + f'<div class="tit" style="top:640px"><div class="h" style="font-size:120px;animation:slam .45s ease-out {t + .3}s both">Una cápsula.</div>'
                  '<div class="dato" style="margin-top:16px">Lipo 6 Black <span class="o">·</span> 222 mg de cafeína</div></div>')
    # 2 · 6 PM · o un shot
    t = STEP * 2
    b += escena(t, glow('rgba(120,170,90,.16)') + prod(t, P.heroe('p_guarana.png', 540, BASE, 540))
                + reloj(t, '6', 'PM', 'O si prefieres')
                + f'<div class="tit" style="top:640px"><div class="h" style="font-size:120px;animation:slam .45s ease-out {t + .3}s both">Un shot.</div>'
                  '<div class="dato" style="margin-top:16px">Guaraná Shot <span class="o">·</span> 200 mg <span class="o">·</span> Pera</div></div>')
    # 3 · el dato
    t = STEP * 3
    b += escena(t, glow('rgba(242,106,27,.10)', 45) + prod(t, P.heroe('p_lipo.png', 330, BASE, 400) + P.heroe('p_guarana.png', 750, BASE, 430))
                + f'''<div class="tit" style="top:330px"><div class="lab">La regla</div>
 <div class="hora o" style="margin-top:24px;animation:flip .5s cubic-bezier(.2,.8,.2,1) {t}s both">30 a 60</div>
 <div class="h" style="font-size:120px;margin-top:10px">minutos antes.</div>
 <div class="dato" style="margin-top:26px">Uno de los dos <span class="o">·</span> Nunca juntos</div></div>''')
    # 4 · 7 PM · a entrenar
    t = STEP * 4
    b += escena(t, glow('rgba(242,106,27,.14)')
                + f'<img src="{P.gen.HELMET}" style="position:absolute;left:50%;top:{BASE}px;height:520px;transform:translate(-50%,-100%);opacity:.9;animation:drift {STEP}s linear {t}s both">'
                + reloj(t, '7', 'PM', 'La hora')
                + f'<div class="tit" style="top:640px"><div class="h o" style="font-size:150px;animation:slam .45s ease-out {t + .3}s both">A entrenar.</div></div>')
    # 5 · cierre en loop al encuadre del gancho, una sola acción
    t = STEP * 5
    b += escena(t, glow('rgba(242,106,27,.12)') + prod(t, par())
                + f'''<div class="tit" style="top:300px"><div class="lab">30 a 60 minutos antes</div>
 <div class="h" style="font-size:140px;margin-top:22px;animation:slam .45s ease-out {t + .2}s both">Mándaselo a quien</div>
 <div class="h o" style="font-size:140px">entrena contigo.</div>
 <div class="dato" style="margin-top:24px">Guárdalo <span class="o">·</span> Pídelo por DM</div></div>''', ultima=True)
    b += P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px">Energía para entrenar</div>'
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
