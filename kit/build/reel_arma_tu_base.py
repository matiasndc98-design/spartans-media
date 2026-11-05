"""Reel 9:16 (15,5 s, estilo SOBRIO) · jueves 5 nov 2026, semana "base y constancia": "Arma tu base."
Tipo nuevo: STACK QUE SE ARMA (producto). El piso parte con 4 siluetas vacías (gancho legible en el cuadro 0)
y cada producto ocupa su lugar cada 2,5 s (multivitamínico, Omega 3, creatina, proteína); el activo se ve
encendido y los anteriores quedan atenuados. Remate: los 4 encendidos "Lo básico. Todos los días." + DM.
Idea tomada de los reels "my daily stack" de marcas de suplementos, en versión sobria (sin texto animado con chistes).
Sin precios, sin numeración. Sonido original: solo efectos (sonido.py), la música la pone el dueño.
Uso (desde kit/build): python3 reel_arma_tu_base.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

OR = R.OR
HOOK, STEP = 2.5, 2.5
BASE_Y = 1380
PRODS = [  # imagen, x centro, alto, etiqueta, titular, dato
    ('p_multi.png', 150, 380, 'USN · Super Daily Formula', 'Multivitamínico.', '30 porciones.'),
    ('p_omega.png', 345, 400, 'USN · Fish Oil 1000 mg', 'Omega 3.', '90 cápsulas.'),
    ('p_mt_sin.png', 575, 380, 'MuscleTech Platinum · 400 g', 'Creatina.', '5 g al día.'),
    ('p_iso100.png', 868, 480, 'Dymatize ISO 100 · 5 lb', 'Proteína.', '25 g por scoop.'),
]
TEND = HOOK + STEP * len(PRODS)  # 12,5
R.DUR = TEND + 3.0               # 15,5 s


def scene_css():
    return P.CSS + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden}}
.sc{{position:absolute;inset:0;opacity:0}}
@keyframes show{{0%{{opacity:0}}6%{{opacity:1}}94%{{opacity:1}}100%{{opacity:0}}}}
@keyframes showEnd{{0%{{opacity:0}}12%{{opacity:1}}100%{{opacity:1}}}}
@keyframes out{{0%{{opacity:1}}100%{{opacity:0}}}}
@keyframes rise{{0%{{transform:translateY(120px);opacity:0}}60%{{transform:translateY(-6px);opacity:1}}100%{{transform:translateY(0);opacity:1}}}}
@keyframes dim{{0%{{opacity:1}}100%{{opacity:.32}}}}
@keyframes lit{{0%{{opacity:.32}}100%{{opacity:1}}}}
@keyframes up{{0%{{transform:translateY(24px);opacity:0}}100%{{transform:translateY(0);opacity:1}}}}
@keyframes slam{{0%{{transform:scale(1.25);opacity:0}}45%{{transform:scale(.98);opacity:1}}70%,100%{{transform:scale(1);opacity:1}}}}
@keyframes bar{{0%{{width:0}}100%{{width:100%}}}}
.prog{{position:absolute;left:70px;right:70px;top:255px;height:4px;background:rgba(255,255,255,.10);border-radius:2px;z-index:9}}
.prog i{{display:block;height:100%;background:{OR};animation:bar {R.DUR}s linear both}}
.sil{{position:absolute;filter:brightness(0) drop-shadow(0 0 2px rgba(244,241,236,.75));opacity:.9}}
.tit{{position:absolute;left:0;right:0;top:360px;text-align:center}}
"""


def silueta(img, cx, h):
    return f'<img class="sil" src="{P.I(img)}" style="left:{cx}px;top:{BASE_Y}px;height:{h}px;transform:translate(-50%,-100%)">'


def body():
    b = ('<div class="stage"></div><div style="position:absolute;inset:0;background:radial-gradient(ellipse 55% 30% at 50% 62%,rgba(242,106,27,.10),transparent 70%)"></div>'
         f'<div class="floor" style="height:{int(R.H * .34)}px"></div>'
         + P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px">Semana de la constancia</div><div class="prog"><i></i></div>')
    # Siluetas vacías del piso (fijas; los productos las tapan al llegar)
    b += ''.join(silueta(img, x, h) for img, x, h, *_ in PRODS)
    # Gancho: completo desde el cuadro 0, sin animación de entrada
    b += f'''<div class="tit" style="animation:out .25s linear {HOOK - .25}s both">
 <div class="lab">Tu stack diario</div>
 <div class="h" style="font-size:210px;margin-top:22px">Arma tu</div>
 <div class="h o" style="font-size:210px">base.</div>
</div>'''
    # Productos: llegan a su lugar, se atenúan cuando entra el siguiente y se encienden todos al final
    for k, (img, x, h, lab, t1, t2) in enumerate(PRODS):
        t = HOOK + k * STEP
        anim = f'rise .55s cubic-bezier(.2,.8,.2,1) {t}s both'
        if k < len(PRODS) - 1:
            anim += f',dim .35s ease-out {t + STEP}s forwards,lit .4s ease-out {TEND}s forwards'
        b += f'<div style="position:absolute;inset:0;animation:{anim}">{P.heroe(img, x, BASE_Y, h)}</div>'
        b += f'''<div class="sc" style="animation:show {STEP}s linear {t}s both"><div class="tit">
 <div class="lab" style="animation:up .4s ease-out {t + .05}s both">{lab}</div>
 <div class="h" style="font-size:170px;margin-top:22px;animation:up .4s ease-out {t + .1}s both">{t1}</div>
 <div class="h o" style="font-size:130px;margin-top:6px;animation:up .4s ease-out {t + .25}s both">{t2}</div>
</div></div>'''
    # Remate
    t = TEND
    b += f'''<div class="sc" style="animation:showEnd {R.DUR - t}s linear {t}s both"><div class="tit">
 <div class="lab">Spartans</div>
 <div class="h" style="font-size:180px;margin-top:22px;animation:slam .5s ease-out {t}s both">Lo básico.</div>
 <div class="h o" style="font-size:180px;animation:slam .5s ease-out {t + .45}s both">Todos los días.</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:300px;text-align:center;font-weight:600;font-size:28px;letter-spacing:6px;text-transform:uppercase;animation:up .4s ease-out {t + 1}s both">
 Pídelo por DM <span class="o">·</span> Proteína + creatina: shaker de regalo</div></div>'''
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
