"""Reel 9:16 (15 s, estilo premium) · sábado 31 oct (Halloween), semana de la energía: "POV: son las 6 PM y tu batería dice que no".
Tipo POV CON BATERÍA (distinto del anterior, "esto o esto"). Rehace el antiguo reel_pov_energia.py en estilo premium
con gancho completo en el cuadro 0: una batería grande queda fija en pantalla y su % cambia con cada paso
(excusa la baja; zapatillas, agua y comida liviana, y el shot 30–60 min antes la suben). Remate "comenta tu %".
Sin precios. Nota de cafeína del Guaraná Shot en pantalla todo el reel.
Uso (desde kit/build): python3 reel_pov_bateria.py <salida.mp4>
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import premium as P

OR = R.OR
HOOK, PASO = 2.6, 2.3
PASOS = [  # texto, detalle, nivel %, color
    ('“Mejor voy mañana”', 'La excusa de siempre', 5, '#d33b2c'),
    ('Te pones las zapatillas', 'Ya ganaste la mitad', 35, '#e08a1e'),
    ('Agua y algo liviano', '1 a 2 horas antes', 65, '#e8b21e'),
    ('Guaraná Shot', '30 a 60 min antes, si toleras la cafeína', 100, OR),
]
TEND = HOOK + PASO * len(PASOS)  # 11,8
R.DUR = TEND + 3.2               # 15,0 s
NOTA = 'Guaraná Shot: contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.'
BX, BY, BW, BH = 300, 640, 480, 230   # batería


def scene_css():
    css = P.CSS + f"""
body{{width:{R.W}px;height:{R.H}px;overflow:hidden}}
.sc{{position:absolute;inset:0;opacity:0}}
.big{{font-family:Bebas;line-height:.88;text-transform:uppercase}}
@keyframes show{{0%{{opacity:0}}5%{{opacity:1}}95%{{opacity:1}}100%{{opacity:0}}}}
@keyframes showEnd{{0%{{opacity:0}}10%{{opacity:1}}100%{{opacity:1}}}}
@keyframes out{{0%{{opacity:1}}100%{{opacity:0}}}}
@keyframes slam{{0%{{transform:scale(1.4);opacity:0}}40%{{transform:scale(.97);opacity:1}}60%,100%{{transform:scale(1);opacity:1}}}}
@keyframes pop{{0%{{transform:scale(.6);opacity:0}}60%{{transform:scale(1.05);opacity:1}}100%{{transform:scale(1);opacity:1}}}}
@keyframes rise{{0%{{transform:translateY(80px);opacity:0}}100%{{transform:translateY(0);opacity:1}}}}
@keyframes bar{{0%{{width:0}}100%{{width:100%}}}}
.prog{{position:absolute;left:70px;right:70px;top:255px;height:4px;background:rgba(255,255,255,.10);border-radius:2px;z-index:9}}
.prog i{{display:block;height:100%;background:{OR};animation:bar {R.DUR}s linear both}}
.bat{{position:absolute;left:{BX}px;top:{BY}px;width:{BW}px;height:{BH}px;border:8px solid #f4f1ec;border-radius:34px;padding:14px}}
.bat:after{{content:'';position:absolute;right:-34px;top:70px;width:22px;height:74px;background:#f4f1ec;border-radius:0 10px 10px 0}}
.lvl{{position:absolute;left:14px;top:14px;bottom:14px;border-radius:18px}}
.pct{{position:absolute;left:0;right:0;top:{BY + BH + 40}px;text-align:center;font-family:Bebas;font-size:130px;line-height:1}}
.nota{{position:absolute;left:80px;right:80px;font-weight:600;font-size:18px;letter-spacing:2px;text-transform:uppercase;color:#8d8880;line-height:1.5;text-align:center}}
"""
    # animación de nivel de la batería por paso
    inner = BW - 16 - 28
    niv = [12] + [p[2] for p in PASOS]
    for k in range(len(PASOS)):
        a, b = niv[k], niv[k + 1]
        css += f"@keyframes l{k}{{0%{{width:{inner * a / 100:.0f}px}}100%{{width:{inner * b / 100:.0f}px}}}}\n"
    return css


def body():
    b = ('<div class="stage"></div><div style="position:absolute;inset:0;background:radial-gradient(ellipse 50% 30% at 50% 40%,rgba(242,106,27,.09),transparent 70%)"></div>'
         f'<div class="floor" style="height:{int(R.H * .32)}px"></div>'
         + P.marca(70, 175) + '<div class="foot" style="right:70px;top:186px;color:#F26A1B">POV</div><div class="prog"><i></i></div>')
    inner = BW - 16 - 28
    # Gancho fijo desde el cuadro 0 (titular arriba), se mantiene todo el reel
    b += '''<div style="position:absolute;left:0;right:0;top:320px;text-align:center">
 <div class="lab">POV · Son las 6 PM</div>
 <div class="big" style="font-size:120px;margin-top:18px">Tu batería dice <span class="o">que no</span></div>
</div>'''
    # Batería: nivel inicial 12% visible en el cuadro 0
    b += f'<div class="bat"><div class="lvl" style="width:{inner * .12:.0f}px;background:#d33b2c"></div>'
    for k, (_, _, n, col) in enumerate(PASOS):
        t = HOOK + k * PASO
        b += (f'<div class="lvl" style="background:{col};opacity:0;animation:l{k} .7s ease-out {t}s both,showEnd .01s linear {t}s both'
              + (f',out .01s linear {t + PASO}s forwards' if k < len(PASOS) - 1 else '') + '"></div>')
    b += '</div>'
    # porcentaje
    b += f'<div class="pct" style="color:#d33b2c;animation:out .01s linear {HOOK}s forwards">12%</div>'
    for k, (_, _, n, col) in enumerate(PASOS):
        t = HOOK + k * PASO
        b += (f'<div class="pct" style="color:{col};opacity:0;animation:pop .35s ease-out {t + .3}s both'
              + (f',out .01s linear {t + PASO}s forwards' if k < len(PASOS) - 1 else '') + f'">{n}%</div>')
    # Gancho inferior (cuadro 0)
    b += f'''<div class="sc" style="opacity:1;animation:out .2s linear {HOOK - .2}s both">
<div style="position:absolute;left:0;right:0;top:1140px;text-align:center">
 <div style="font-size:44px;font-weight:500;color:#e8e4dd">Cero ganas de entrenar.</div>
 <div class="big o" style="font-size:96px;margin-top:14px">Así se carga</div>
</div></div>'''
    # Pasos
    for k, (txt, det, n, col) in enumerate(PASOS):
        t = HOOK + k * PASO
        last = k == len(PASOS) - 1
        anim = f'show {PASO}s linear {t}s both'
        prod = ''
        if last:
            prod = P.heroe('p_guarana.png', 540, 1575, 280)
        b += f'''<div class="sc" style="animation:{anim}">
<div style="position:absolute;left:60px;right:60px;top:1120px;text-align:center;animation:rise .4s ease-out {t}s both">
 <div class="big" style="font-size:{100 if len(txt) < 22 else 88}px;color:{"#f4f1ec" if k else "#bdb8b0"}">{txt}</div>
 <div style="font-size:38px;font-weight:500;color:#bdb8b0;margin-top:16px">{det}</div>
</div>{prod}</div>'''
    # Remate
    t = TEND
    b += f'''<div class="sc" style="z-index:5;animation:showEnd {R.DUR - t}s linear {t}s both">
<div style="position:absolute;left:0;right:0;top:1110px;text-align:center">
 <div class="big" style="font-size:120px;animation:slam .45s ease-out {t}s both">Modo <span class="o">espartano</span></div>
 <div class="big" style="font-size:80px;margin-top:10px;animation:slam .45s ease-out {t + .5}s both">Ni en Halloween te salvas</div>
 <div class="lab" style="font-size:30px;letter-spacing:5px;color:#e8e4dd;margin-top:34px;animation:pop .4s ease-out {t + 1.1}s both">¿Con cuánta batería llegas hoy? <span class="o">Comenta tu %</span></div>
</div></div>'''
    b += f'<div class="nota" style="bottom:270px;z-index:6">{NOTA}</div>'
    return b + '<div class="grain"></div>'


R.scene_css = scene_css
R.body = body
if __name__ == '__main__':
    R.main()
