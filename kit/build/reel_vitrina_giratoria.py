"""Reel 9:16 (15,5 s, estilo SOBRIO) · sábado 14 nov 2026: "¿Qué va después de entrenar?"
Tipo nuevo: VITRINA GIRATORIA (tornamesa 360). Los 4 productos están sobre una plataforma elíptica que gira
un cuarto de vuelta cada 2,5 s y deja uno al frente (idea de los "product turntable / 360 spin" de marcas grandes).
Al cierre salen de la tornamesa y quedan en fila con un número cada uno: "¿Cuál es la tuya? 1, 2, 3 o 4".
Gancho legible desde el cuadro 0. Sin precios, sin numeración de lámina.
Sonido original: solo efectos (sonido.py), la música la pone el dueño.
Uso (desde kit/build): python3 reel_vitrina_giratoria.py <salida.mp4>
"""
import sys, math
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

OR = R.OR
HOOK, STEP, TURN = 2.5, 2.5, 0.7
PRODS = [  # imagen, modo (h: alto / w: ancho), tamaño al frente, etiqueta, titular, dato, tamaño en fila
    ('p_whey.png', 'h', 740, 'USN Premium Whey+ · Chocolate', '22 g.', 'Por scoop.', 400),
    ('p_iso100.png', 'h', 760, 'Dymatize ISO 100 · Cocoa Pebbles', '25 g.', '100% isolate.', 410),
    ('p_nitro.png', 'h', 760, 'MuscleTech Nitro Tech · Vainilla', '30 g.', '+ 3 g de creatina.', 410),
    ('p_barra.png', 'w', 720, 'Space Protein XXL · Coco', 'Al paso.', '36% proteína.', 290),
]
N = len(PRODS)
TEND = HOOK + STEP * N        # 12,5: sale de la tornamesa
R.DUR = TEND + 3.0            # 15,5 s
CX, CY, RX, RY = 540, 1470, 310, 95
FILA_Y, FILA_X = 1420, [170, 420, 670, 915]


def ease(u):
    u = max(0.0, min(1.0, u))
    return u * u * (3 - 2 * u)


def giro(t):
    """Cuartos de vuelta acumulados en el tiempo t."""
    r = 0.0
    for k in range(1, N):
        t1 = HOOK + STEP * k
        r += ease((t - (t1 - TURN)) / TURN)
    return r


def estado(k, t):
    img, modo, tam = PRODS[k][:3]
    th = (k - giro(t)) * math.pi / 2
    c = math.cos(th)
    s = 0.42 + 0.58 * (1 + c) / 2
    x, y = CX + RX * math.sin(th), CY + RY * c
    luz = 0.35 + 0.65 * (1 + c) / 2
    z = int(10 + 10 * c)
    # salida a la fila
    u = ease((t - TEND) / 0.8)
    if u > 0:
        fs = PRODS[k][6] / tam
        x, y = x + (FILA_X[k] - x) * u, y + (FILA_Y - y) * u
        s, luz = s + (fs - s) * u, luz + (1 - luz) * u
    return x, y, s, luz, z


def keyframes():
    css, n = '', 160
    for k in range(N):
        css += f'@keyframes orb{k}{{'
        for i in range(n + 1):
            t = R.DUR * i / n
            x, y, s, luz, z = estado(k, t)
            css += (f'{100 * i / n:.3f}%{{left:{x:.1f}px;top:{y:.1f}px;transform:translate(-50%,-100%) scale({s:.4f});'
                    f'filter:brightness({luz:.3f});z-index:{z}}}')
        css += '}'
    return css


def scene_css():
    return P.CSS + keyframes() + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden}}
.sc{{position:absolute;inset:0;opacity:0}}
@keyframes show{{0%{{opacity:0}}6%{{opacity:1}}94%{{opacity:1}}100%{{opacity:0}}}}
@keyframes showEnd{{0%{{opacity:0}}12%{{opacity:1}}100%{{opacity:1}}}}
@keyframes out{{0%{{opacity:1}}100%{{opacity:0}}}}
@keyframes up{{0%{{transform:translateY(24px);opacity:0}}100%{{transform:translateY(0);opacity:1}}}}
@keyframes slam{{0%{{transform:scale(1.25);opacity:0}}45%{{transform:scale(.98);opacity:1}}70%,100%{{transform:scale(1);opacity:1}}}}
@keyframes inL{{0%{{opacity:0}}100%{{opacity:0}}}}
@keyframes bar{{0%{{width:0}}100%{{width:100%}}}}
@keyframes spin{{0%{{transform:rotate(0)}}100%{{transform:rotate(-270deg)}}}}
.prog{{position:absolute;left:70px;right:70px;top:255px;height:4px;background:rgba(255,255,255,.10);border-radius:2px;z-index:30}}
.prog i{{display:block;height:100%;background:{OR};animation:bar {R.DUR}s linear both}}
.tit{{position:absolute;left:0;right:0;top:330px;text-align:center;z-index:30}}
.it{{position:absolute;transform-origin:50% 100%}}
.it img{{display:block;filter:drop-shadow(0 30px 34px rgba(0,0,0,.8))}}
.it .sh{{position:absolute;left:10%;right:10%;bottom:-22px;height:44px;border-radius:50%;background:radial-gradient(closest-side,rgba(0,0,0,.75),transparent)}}
"""


def plataforma():
    # disco elíptico con borde naranjo fino y un brillo que gira (se ve como tornamesa)
    return f'''<div style="position:absolute;inset:0;animation:out .6s linear {TEND}s both">
<div style="position:absolute;left:{CX - 470}px;top:{CY - 135}px;width:940px;height:270px;border-radius:50%;
 background:radial-gradient(ellipse at 50% 40%,#2a2a2a,#121212 70%);box-shadow:0 30px 60px rgba(0,0,0,.8),inset 0 2px 0 rgba(255,255,255,.08)"></div>
<div style="position:absolute;left:{CX - 470}px;top:{CY - 135}px;width:940px;height:270px;border-radius:50%;border:2px solid rgba(242,106,27,.55)"></div>
<div style="position:absolute;left:{CX - 470}px;top:{CY - 135}px;width:940px;height:270px;border-radius:50%;overflow:hidden;opacity:.5">
 <div style="position:absolute;left:220px;top:-335px;width:500px;height:940px;transform:scaleY(.287)">
  <div style="position:absolute;inset:0;border-radius:50%;background:conic-gradient(from 0deg,transparent 0 70%,rgba(255,255,255,.10) 80%,transparent 90%);animation:spin {TEND}s linear both"></div></div></div>
<div style="position:absolute;left:{CX - 470}px;top:{CY + 120}px;width:940px;height:40px;border-radius:50%;background:rgba(0,0,0,.6);filter:blur(14px);z-index:-1"></div></div>'''


def body():
    b = ('<div class="stage"></div>'
         '<div style="position:absolute;inset:0;background:radial-gradient(ellipse 55% 30% at 50% 66%,rgba(242,106,27,.11),transparent 70%)"></div>'
         f'<div class="floor" style="height:{int(R.H * .30)}px"></div>' + plataforma())
    for k, (img, modo, tam, *_r) in enumerate(PRODS):
        st = f'height:{tam}px' if modo == 'h' else f'width:{tam}px;transform:rotate(-6deg)'
        b += (f'<div class="it" style="animation:orb{k} {R.DUR}s linear both"><div class="sh"></div>'
              f'<img src="{P.I(img)}" style="{st}"></div>')
    b += P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px;z-index:30">Después de entrenar</div><div class="prog"><i></i></div>'
    # Gancho completo desde el cuadro 0
    b += f'''<div class="tit" style="animation:out .25s linear {HOOK - .25}s both">
 <div class="lab" style="color:#d8d3cc">Sábado</div>
 <div class="h" style="font-size:165px;margin-top:22px">¿Qué va</div>
 <div class="h o" style="font-size:132px">después de entrenar?</div></div>'''
    # sonido de giro en cada cuarto de vuelta
    for k in range(1, N):
        b += f'<i style="animation:inL .1s linear {HOOK + STEP * k - TURN}s both"></i>'
    for k, (img, modo, tam, lab, t1, t2, _f) in enumerate(PRODS):
        t0 = HOOK + STEP * k
        dur = STEP - TURN + (0.1 if k == 0 else 0) + (TURN if k == N - 1 else 0)
        b += f'''<div class="sc" style="z-index:30;animation:show {dur}s linear {t0 - (0.1 if k else 0)}s both"><div class="tit">
 <div class="lab" style="animation:up .35s ease-out {t0}s both">{lab}</div>
 <div class="h" style="font-size:190px;margin-top:22px;animation:slam .45s ease-out {t0 + .05}s both">{t1}</div>
 <div class="h o" style="font-size:110px;margin-top:6px;animation:up .4s ease-out {t0 + .25}s both">{t2}</div></div></div>'''
    # Cierre: en fila, con número
    t = TEND
    nums = ''.join(f'<div class="h" style="position:absolute;left:{x}px;top:{FILA_Y + 30}px;transform:translateX(-50%);font-size:76px;color:{OR};animation:up .4s ease-out {t + .7 + i * .12}s both">{i + 1}</div>'
                   for i, x in enumerate(FILA_X))
    b += f'''<div class="sc" style="z-index:30;animation:showEnd {R.DUR - t}s linear {t}s both">
<div class="tit"><div class="lab">Después de entrenar</div>
 <div class="h" style="font-size:150px;margin-top:22px;animation:slam .5s ease-out {t + .3}s both">¿Cuál es la tuya?</div>
 <div class="h o" style="font-size:130px;animation:slam .5s ease-out {t + .7}s both">1, 2, 3 o 4.</div></div>
{nums}
<div style="position:absolute;left:0;right:0;bottom:300px;text-align:center;font-weight:600;font-size:28px;letter-spacing:6px;text-transform:uppercase;animation:up .4s ease-out {t + 1.2}s both">
 Pídelo por DM <span class="o">·</span> Delivery en Caldera $1.500</div></div>'''
    return b + '<div class="grain" style="z-index:40"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
