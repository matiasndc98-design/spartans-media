"""Reel 9:16 (15 s, estilo SOBRIO) · sábado 28 nov 2026: "¿Qué va en tu bolso?"
Tipo nuevo: STOP MOTION (tendencia de reels de producto 2026 hechos "a mano": el producto avanza a saltos de
8 cuadros por segundo, con un leve temblor de posición y giro en cada paso y un clic de obturador por paso).
Gancho completo desde el cuadro 0 (sin animación de entrada en el titular). Cada producto 2,5 s, un solo dato.
Shaker C4 (promoción real: por compra de proteína + creatina) · Whey USN 22 g · barra Space Protein XXL 36% ·
Guaraná Shot 200 mg (con nota de cafeína). Cierre: los 4 juntos "Bolso listo." + DM + delivery + llamado a envíos.
Sin precios de productos, sin numeración, sin chistes. Sonido original: solo efectos (sonido.py).
Uso (desde kit/build): python3 reel_stop_motion_bolso.py <salida.mp4>
"""
import sys, random
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

STEP = 2.5
BASE_Y = 1480
R.DUR = STEP * 6  # 15 s
NOTA = 'Contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.'

# img, alto, titular (blanco, naranjo), dato, glow
PRODS = [
    ('p_shaker.png', 780, ('Shaker C4.<br>', 'De regalo.'), 'Por compra de proteína + creatina', 'rgba(230,200,40,.14)'),
    ('p_whey.png', 700, ('La ', 'proteína.'), 'Whey USN · 22 g por scoop', 'rgba(150,80,30,.20)'),
    ('p_barra.png', 0, ('Al ', 'paso.'), 'Barra Space Protein XXL · 36% proteína', 'rgba(60,110,170,.20)'),
    ('p_guarana.png', 720, ('Un ', 'shot.'), 'Guaraná Shot · 80 ml · 200 mg de cafeína', 'rgba(170,200,60,.14)'),
]
rnd = random.Random(28)


def stop_kf(nombre, desde_y, pasos=6, rot0=-14):
    """Entrada a saltos: el producto sube desde abajo en `pasos` posiciones fijas, cada una con temblor."""
    fr = []
    for k in range(pasos + 1):
        f = k / pasos
        y = desde_y * (1 - f)
        rot = rot0 * (1 - f) + (rnd.uniform(-2.5, 2.5) if k < pasos else 0)
        x = rnd.uniform(-10, 10) if k < pasos else 0
        fr.append(f'{f * 100 * .55:.2f}%{{transform:translate({x:.0f}px,{y:.0f}px) rotate({rot:.1f}deg)}}')
    # después, quieto con micro-temblor de stop motion
    for k, f in enumerate([.65, .75, .85, .95]):
        fr.append(f'{f * 100:.0f}%{{transform:translate({rnd.uniform(-3, 3):.0f}px,{rnd.uniform(-2, 2):.0f}px) rotate({rnd.uniform(-.8, .8):.1f}deg)}}')
    fr.append('100%{transform:translate(0,0) rotate(0deg)}')
    return f'@keyframes {nombre}{{{"".join(fr)}}}'


def scene_css():
    kfs = ''.join(stop_kf(f'sm{i}', 900) for i in range(4)) + ''.join(stop_kf(f'fi{i}', 700, 4, 10 - 6 * i) for i in range(4))
    return P.CSS + kfs + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden}}
.sc{{position:absolute;inset:0;opacity:0}}
@keyframes win{{0%{{opacity:1}}100%{{opacity:1}}}}
@keyframes tick{{0%{{opacity:0}}100%{{opacity:0}}}}
@keyframes jit{{0%{{transform:translate(0,0)}}25%{{transform:translate(2px,-1px)}}50%{{transform:translate(-1px,1px)}}75%{{transform:translate(1px,2px)}}100%{{transform:translate(0,0)}}}}
.tit{{position:absolute;left:0;right:0;top:300px;text-align:center}}
.pie{{position:absolute;top:1620px;left:0;right:0;text-align:center;font-weight:600;font-size:26px;letter-spacing:4px;text-transform:uppercase;color:#d8d3cc}}
.tk{{position:absolute;width:1px;height:1px;opacity:0}}
"""


def escena(t0, dur, contenido, ultima=False):
    return f'<div class="sc" style="animation:win {dur}s linear {t0}s {"forwards" if ultima else "none"}">{contenido}</div>'


def fondo(glow):
    return P.page(R.W, R.H, '', glow).split('<body>')[1].split('<div class="grain">')[0]


def clics(t, n, dur):
    """Un clic de obturador en cada salto del stop motion (efecto 'tick' de sonido.py, que suena 0,1 s después)."""
    return ''.join(f'<div class="tk" style="animation:tick .05s linear {t + k / n * .55 * dur - .1:.3f}s"></div>' for k in range(1, n + 1))


def producto(img, alto, cx=540, base=BASE_Y):
    if img == 'p_barra.png':
        return (f'<img class="prod" src="{P.I(img)}" style="left:{cx}px;top:{base - 330}px;width:900px;transform:translate(-50%,-50%) rotate(-12deg)">'
                f'<div style="position:absolute;left:{cx - 300}px;top:{base - 30}px;width:600px;height:50px;border-radius:50%;'
                'background:radial-gradient(closest-side,rgba(0,0,0,.8),transparent);filter:blur(12px)"></div>')
    return P.heroe(img, cx, base, alto)


def body():
    b = ''
    # Gancho legible desde el cuadro 0: titular fijo; el shaker ya está en escena, quieto con temblor de stop motion
    b += escena(0, STEP, fondo('rgba(242,106,27,.08)')
                + f'<div style="position:absolute;inset:0;animation:jit .5s steps(4) 0s 5">{producto("p_shaker.png", 640)}</div>'
                + '''<div class="tit"><div class="lab" style="color:#d8d3cc">Sábado</div>
 <div class="h" style="font-size:200px;margin-top:22px">¿Qué va en</div>
 <div class="h o" style="font-size:200px">tu bolso?</div></div>
<div class="pie">Lo básico para entrenar <span class="o">·</span> Mira</div>''')
    for i, (img, alto, tit, dato, glow) in enumerate(PRODS):
        t = STEP * (i + 1)
        s1, s2 = tit
        fs = 190 if len(s1 + s2) > 10 else 230
        fs = 180 if '<br>' in s1 else fs
        h = f'<div class="h" style="font-size:{fs}px;margin-top:20px">{s1}<span class="o">{s2}</span></div>'
        nota = (f'<div style="position:absolute;left:90px;right:90px;top:1672px;text-align:center;font-size:22px;color:#8d8880;font-weight:500">{NOTA}</div>'
                if img == 'p_guarana.png' else '')
        b += escena(t, STEP, fondo(glow)
                    + f'<div style="position:absolute;inset:0;animation:sm{i} {STEP}s steps(1,end) {t}s both">{producto(img, alto)}</div>'
                    + clics(t, 6, STEP)
                    + f'<div class="tit"><div class="lab">Al bolso</div>{h}</div>'
                    + f'<div class="pie">{dato}</div>' + nota)
    # Cierre: los 4 entran a saltos, uno tras otro, y quedan juntos
    t = STEP * 5
    fila = [('p_shaker.png', 190, 520), ('p_whey.png', 440, 440), ('p_guarana.png', 650, 430)]
    cont = ''
    for k, (img, cx, alto) in enumerate(fila):
        cont += (f'<div style="position:absolute;inset:0;animation:fi{k} .9s steps(1,end) {t + k * .25:.2f}s both">'
                 f'{P.heroe(img, cx, BASE_Y, alto)}</div>')
    cont += (f'<div style="position:absolute;inset:0;animation:fi3 .9s steps(1,end) {t + .75:.2f}s both">'
             f'<img class="prod" src="{P.I("p_barra.png")}" style="left:880px;top:{BASE_Y - 190}px;width:380px;transform:translate(-50%,-50%) rotate(-62deg)"></div>')
    b += escena(t, STEP, fondo('rgba(242,106,27,.12)') + cont + ''.join(clics(t + k * .25, 4, .9) for k in range(4))
                + '''<div class="tit"><div class="lab" style="color:#d8d3cc">Sábado</div>
 <div class="h" style="font-size:220px;margin-top:22px">Bolso</div>
 <div class="h o" style="font-size:220px">listo.</div></div>
<div style="position:absolute;left:0;right:0;top:1600px;text-align:center;font-weight:600;font-size:28px;letter-spacing:6px;text-transform:uppercase">
 Pídelo por DM <span class="o">·</span> Delivery en Caldera $1.500</div>
<div style="position:absolute;left:0;right:0;top:1652px;text-align:center;font-weight:500;font-size:25px;letter-spacing:3px;text-transform:uppercase;color:#a9a39b">
 Mándaselo a quien entrena contigo <span class="o">·</span> Guárdalo</div>
<div style="position:absolute;left:90px;right:90px;top:1706px;text-align:center;font-size:20px;color:#7d7870;font-weight:500">Guaraná Shot: ''' + NOTA + '</div>',
                ultima=True)
    b += P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px">Sábado</div>'
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
