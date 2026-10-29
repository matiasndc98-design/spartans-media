"""Reel 9:16 (~15 s, estilo premium) · jueves 29 oct, semana de la energía: "¿Shot o cápsula?"
Tipo nuevo: ESTO O ESTO en pantalla dividida (Guaraná Shot vs Lipo 6), distinto del anterior (educativo con cálculo).
Idea nueva (tendencia 2026 de reels comparativos "this or that" en split screen): los dos productos quedan fijos
a cada lado y las filas de la comparación se van sumando; remate "Elige uno. Nunca los dos." + "comenta SHOT o CÁPSULA".
Gancho legible completo desde el cuadro 0. Sin precios. Notas de cafeína de ambos productos en pantalla todo el reel.
Uso (desde kit/build): python3 reel_shot_o_capsula.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

OR = R.OR
HOOK, FILA = 2.6, 2.3
FILAS = [  # etiqueta, shot, cápsula
    ('Cafeína', '200 mg', '222 mg'),
    ('Cómo se toma', 'De un trago', '1 con agua'),
    ('Sabor', 'Pera', 'No tiene'),
    ('Rinde', '1 shot', '60 cápsulas'),
]
TEND = HOOK + FILA * len(FILAS)  # 11,8
R.DUR = TEND + 3.2               # 15,0 s
NOTAS = ('Guaraná Shot: contiene cafeína (200 mg por shot). Lipo 6: contiene cafeína (222 mg por cápsula). '
         'No aptos para menores ni embarazadas.')


def scene_css():
    return P.CSS + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden}}
.sc{{position:absolute;inset:0;opacity:0}}
.big{{font-family:Bebas;line-height:.88;text-transform:uppercase}}
@keyframes show{{0%{{opacity:0}}5%{{opacity:1}}95%{{opacity:1}}100%{{opacity:0}}}}
@keyframes showEnd{{0%{{opacity:0}}10%{{opacity:1}}100%{{opacity:1}}}}
@keyframes out{{0%{{opacity:1}}100%{{opacity:0}}}}
@keyframes inL{{0%{{transform:translateX(-60px);opacity:0}}100%{{transform:translateX(0);opacity:1}}}}
@keyframes inR{{0%{{transform:translateX(60px);opacity:0}}100%{{transform:translateX(0);opacity:1}}}}
@keyframes slam{{0%{{transform:scale(1.4);opacity:0}}40%{{transform:scale(.97);opacity:1}}60%,100%{{transform:scale(1);opacity:1}}}}
@keyframes pop{{0%{{transform:scale(.6);opacity:0}}60%{{transform:scale(1.05);opacity:1}}100%{{transform:scale(1);opacity:1}}}}
@keyframes hi{{0%{{background:transparent}}100%{{background:rgba(242,106,27,.13)}}}}
@keyframes lo{{0%{{background:rgba(242,106,27,.13)}}100%{{background:transparent}}}}
@keyframes bar{{0%{{width:0}}100%{{width:100%}}}}
.prog{{position:absolute;left:70px;right:70px;top:255px;height:4px;background:rgba(255,255,255,.10);border-radius:2px;z-index:9}}
.prog i{{display:block;height:100%;background:{OR};animation:bar {R.DUR}s linear both}}
.fila{{position:absolute;left:60px;right:60px;height:110px;border-radius:14px;opacity:0}}
.fila .l{{position:absolute;left:0;right:0;top:12px;text-align:center;font-weight:600;font-size:20px;letter-spacing:6px;text-transform:uppercase;color:#9a958e}}
.fila .a,.fila .b{{position:absolute;top:38px;width:430px;font-family:Bebas;font-size:66px;line-height:1;text-transform:uppercase}}
.fila .a{{left:20px;text-align:center}}.fila .b{{right:20px;text-align:center}}
.nota{{position:absolute;left:80px;right:80px;font-weight:600;font-size:18px;letter-spacing:2px;text-transform:uppercase;color:#8d8880;line-height:1.5;text-align:center}}
"""


def body():
    b = ('<div class="stage"></div><div style="position:absolute;inset:0;background:radial-gradient(ellipse 50% 30% at 50% 45%,rgba(242,106,27,.09),transparent 70%)"></div>'
         f'<div class="floor" style="height:{int(R.H * .32)}px"></div>'
         + P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px;color:#F26A1B">Esto o esto</div><div class="prog"><i></i></div>')
    # Fijo todo el reel (gancho completo en el cuadro 0): titular + los dos productos + línea divisoria
    b += '''<div style="position:absolute;left:0;right:0;top:330px;text-align:center">
 <div class="lab">Energía para entrenar</div>
 <div class="big" style="font-size:160px;margin-top:20px">¿Shot o <span class="o">cápsula?</span></div>
</div>
<div style="position:absolute;left:539px;top:560px;width:2px;height:520px;background:linear-gradient(180deg,transparent,rgba(242,106,27,.7) 20%,rgba(242,106,27,.7) 80%,transparent)"></div>'''
    b += P.heroe('p_guarana.png', 290, 960, 380) + P.heroe('p_lipo.png', 790, 960, 310)
    b += ('<div style="position:absolute;left:60px;width:460px;top:985px;text-align:center"><div class="big" style="font-size:60px">Guaraná Shot</div>'
          '<div class="lab" style="font-size:18px;letter-spacing:4px;margin-top:6px">OstroVit · 80 ml</div></div>'
          '<div style="position:absolute;right:60px;width:460px;top:985px;text-align:center"><div class="big" style="font-size:60px">Lipo 6 Black</div>'
          '<div class="lab" style="font-size:18px;letter-spacing:4px;margin-top:6px">Nutrex · 60 cápsulas</div></div>')
    # Gancho: invitación a mirar (desaparece al llegar la primera fila)
    b += f'''<div class="sc" style="opacity:1;animation:out .2s linear {HOOK - .2}s both">
<div style="position:absolute;left:0;right:0;top:1180px;text-align:center">
 <div style="font-size:44px;font-weight:500;color:#e8e4dd">Los dos te dan energía.</div>
 <div class="big o" style="font-size:90px;margin-top:14px">Mira la diferencia</div>
</div></div>'''
    # Filas que se van sumando
    for k, (lab, a, c) in enumerate(FILAS):
        t = HOOK + k * FILA
        top = 1095 + k * 116
        anim = f'animation:pop .3s ease-out {t}s both,hi .25s ease-out {t}s both,lo .4s ease-out {t + FILA}s forwards'
        if k == len(FILAS) - 1:
            anim = f'animation:pop .3s ease-out {t}s both,hi .25s ease-out {t}s both'
        anim += f',out .3s linear {TEND}s forwards'
        b += (f'<div class="fila" style="top:{top}px;{anim}"><div class="l">{lab}</div>'
              f'<div class="a" style="animation:inL .35s ease-out {t + .15}s both">{a}</div>'
              f'<div class="b" style="animation:inR .35s ease-out {t + .45}s both">{c}</div></div>')
    # Remate sobre las filas
    t = TEND
    b += f'''<div class="sc" style="z-index:5;animation:showEnd {R.DUR - t}s linear {t}s both">
<div style="position:absolute;left:0;right:0;top:1060px;height:500px;background:linear-gradient(180deg,rgba(14,14,14,0),rgba(14,14,14,1) 8%,rgba(14,14,14,1) 80%,rgba(14,14,14,0))"></div>
<div style="position:absolute;left:0;right:0;top:1120px;text-align:center">
 <div class="big" style="font-size:130px;animation:slam .45s ease-out {t}s both">Elige uno.</div>
 <div class="big o" style="font-size:130px;animation:slam .45s ease-out {t + .5}s both">Nunca los dos.</div>
 <div class="lab" style="color:#e8e4dd;margin-top:26px;animation:pop .4s ease-out {t + 1.1}s both">¿Team shot o team cápsula? <span class="o">Coméntalo</span></div>
</div></div>'''
    b += f'<div class="nota" style="bottom:270px;z-index:6">{NOTAS}</div>'
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
