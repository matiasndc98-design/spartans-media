"""Reel 9:16 (15 s, estilo SOBRIO) · sábado 7 nov 2026, semana "base y constancia": "El sábado también cuenta."
Tipo nuevo: DE CERCA → COMPLETO (macro que se abre). Cada producto parte en primerísimo plano de su etiqueta
y la cámara se aleja hasta mostrarlo entero en el piso de estudio (2,5 s por producto). Idea tomada de los
reels de producto de marcas grandes (macro / texture shots con push-out lento), sin texto animado con chistes.
Gancho legible desde el cuadro 0 (sobre el macro del Finaflex). Sin precios, sin numeración.
Sonido original: solo efectos (sonido.py), la música la pone el dueño.
Uso (desde kit/build): python3 reel_sabado_de_cerca.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

OR = R.OR
HOOK, STEP = 3.0, 2.5
BASE_Y = 1520
PRODS = [  # imagen, alto o ancho, foco del macro (fracción vertical del envase), etiqueta, titular, dato, brillo
    ('p_finaflex.png', 'h', 860, .55, 'Finaflex · Creatina 1 kg', '200 porciones.', '5 g al día.', 'rgba(242,106,27,.12)'),
    ('p_mt_uva.png', 'h', 820, .55, 'MuscleTech Platinum · Grape Freeze', 'Sabor uva.', '5 g. 60 porciones.', 'rgba(120,60,170,.16)'),
    ('p_barra.png', 'w', 980, .5, 'Space Protein XXL · Coco', 'Al paso.', '36% proteína.', 'rgba(120,170,220,.14)'),
]
TEND = HOOK + STEP * len(PRODS)  # 10,5
R.DUR = TEND + 4.5               # 15 s


def scene_css():
    return P.CSS + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden}}
.sc{{position:absolute;inset:0;opacity:0}}
@keyframes show{{0%{{opacity:0}}6%{{opacity:1}}94%{{opacity:1}}100%{{opacity:0}}}}
@keyframes showEnd{{0%{{opacity:0}}12%{{opacity:1}}100%{{opacity:1}}}}
@keyframes out{{0%{{opacity:1}}100%{{opacity:0}}}}
@keyframes rise{{0%{{transform:scale(3.4)}}100%{{transform:scale(1)}}}}
@keyframes up{{0%{{transform:translateY(24px);opacity:0}}100%{{transform:translateY(0);opacity:1}}}}
@keyframes slam{{0%{{transform:scale(1.25);opacity:0}}45%{{transform:scale(.98);opacity:1}}70%,100%{{transform:scale(1);opacity:1}}}}
@keyframes bar{{0%{{width:0}}100%{{width:100%}}}}
.prog{{position:absolute;left:70px;right:70px;top:255px;height:4px;background:rgba(255,255,255,.10);border-radius:2px;z-index:9}}
.prog i{{display:block;height:100%;background:{OR};animation:bar {R.DUR}s linear both}}
.tit{{position:absolute;left:0;right:0;top:330px;text-align:center}}
"""


def producto(img, modo, tam):
    if modo == 'h':
        return P.heroe(img, 540, BASE_Y, tam), tam
    h = int(tam * 428 / 1492)
    s = f'left:540px;top:{BASE_Y - 160}px;width:{tam}px;transform:translate(-50%,-100%) rotate(-6deg)'
    return f'<img class="prod" src="{P.I(img)}" style="{s}">', h


def body():
    b = '<div class="stage"></div>'
    for k, (img, modo, tam, foco, lab, t1, t2, glow) in enumerate(PRODS):
        t = HOOK + k * STEP
        html, alto = producto(img, modo, tam)
        fy = BASE_Y - (160 if modo == 'w' else 0) - alto * (1 - foco)
        # capa de producto: el primero está en macro desde el cuadro 0 (gancho)
        vis = (f'out .3s linear {t + STEP - .3}s both' if k == 0 else
               f'show {STEP}s linear {t}s both')
        b += f'''<div style="position:absolute;inset:0;{'opacity:0;' if k else ''}animation:{vis}">
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 50% 35% at 50% 58%,{glow},transparent 70%)"></div>
<div class="floor" style="height:{int(R.H * .30)}px"></div>
<div style="position:absolute;inset:0;transform-origin:540px {fy:.0f}px;animation:rise 1.1s cubic-bezier(.3,.6,.2,1) {t}s both">{html}</div></div>'''
    b += P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px">Fin de semana</div><div class="prog"><i></i></div>'
    # Gancho: completo desde el cuadro 0, sobre el macro oscurecido
    b += f'''<div style="position:absolute;inset:0;background:rgba(6,5,4,.74);animation:out .4s linear {HOOK - .4}s both"></div>
<div class="tit" style="top:620px;animation:out .3s linear {HOOK - .3}s both">
 <div class="lab" style="color:#d8d3cc">Sábado</div>
 <div class="h" style="font-size:190px;margin-top:22px">El sábado</div>
 <div class="h o" style="font-size:150px">también cuenta.</div>
</div>'''
    for k, (img, modo, tam, foco, lab, t1, t2, glow) in enumerate(PRODS):
        t = HOOK + k * STEP
        b += f'''<div class="sc" style="animation:show {STEP}s linear {t}s both"><div class="tit">
 <div class="lab" style="animation:up .4s ease-out {t + .7}s both">{lab}</div>
 <div class="h" style="font-size:170px;margin-top:22px;animation:up .4s ease-out {t + .8}s both">{t1}</div>
 <div class="h o" style="font-size:110px;margin-top:6px;animation:up .4s ease-out {t + .95}s both">{t2}</div>
</div></div>'''
    # Remate: los tres juntos en el piso
    t = TEND
    trio = (P.heroe('p_finaflex.png', 250, BASE_Y, 560) + P.heroe('p_mt_uva.png', 800, BASE_Y, 540)
            + f'<img class="prod" src="{P.I("p_barra.png")}" style="left:530px;top:{BASE_Y}px;width:520px;transform:translate(-50%,-100%) rotate(-6deg)">')
    b += f'''<div class="sc" style="animation:showEnd {R.DUR - t}s linear {t}s both">
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 55% 30% at 50% 62%,rgba(242,106,27,.10),transparent 70%)"></div>
<div class="floor" style="height:{int(R.H * .30)}px"></div>
<div style="position:absolute;inset:0;animation:up .5s ease-out {t}s both">{trio}</div>
<div class="tit"><div class="lab">Spartans</div>
 <div class="h" style="font-size:180px;margin-top:22px;animation:slam .5s ease-out {t + .2}s both">Lo básico.</div>
 <div class="h o" style="font-size:150px;animation:slam .5s ease-out {t + .6}s both">También el sábado.</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:300px;text-align:center;font-weight:600;font-size:28px;letter-spacing:6px;text-transform:uppercase;animation:up .4s ease-out {t + 1.1}s both">
 Pídelo por DM <span class="o">·</span> Delivery en Caldera $1.500</div></div>'''
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
