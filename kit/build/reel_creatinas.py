"""Reel comparativa 9:16: ¿Qué creatina te conviene? (barras animadas, sin precios).
Uso (desde kit/build): python3 reel_creatinas.py <salida.mp4>
Datos del catálogo: USN 300 g (60 porciones), MuscleTech Platinum 400 g (80), Finaflex 1 kg (200); 5 g por porción.
Las tres son creatina monohidrato.
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import gen

OR = R.OR
I = R.I
SC = [0, 2.8, 8.0, 12.2, 15.4]
R.DUR = 18.6

EXTRA = '<style>@keyframes gx{0%{transform:scaleX(0)}100%{transform:scaleX(1)}}</style>'
CRE = [('p_usn_crea.png', 'USN', '300 g', 60), ('p_mt_sin.png', 'MUSCLETECH', '400 g', 80), ('p_finaflex.png', 'FINAFLEX', '1 KG', 200)]


def body():
    t = SC
    b = EXTRA + f'{R.FX.replace("SEED", "7171")}<div class="brand"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div><div class="prog"><i></i></div>'
    # 1 gancho: tres frascos que aparecen uno a uno
    jars = ''.join(f'<img src="{I(p[0])}" style="height:{h}px;margin:0 6px;filter:drop-shadow(0 24px 20px #000);animation:rise .7s ease-out {.9 + k * .25}s both">'
                   for k, (p, h) in enumerate(zip(CRE, [380, 400, 420])))
    b += f'''<div class="sc" style="animation:show {t[1]}s linear 0s both"><div class="glow"></div>
<div style="position:absolute;top:400px;left:0;right:0;text-align:center;animation:slam .8s ease-out .05s both"><div class="big" style="font-size:130px">¿QUÉ CREATINA</div></div>
<div style="position:absolute;top:530px;left:0;right:0;text-align:center;animation:slam .8s ease-out .35s both"><div class="big o" style="font-size:190px;text-shadow:0 0 40px rgba(242,106,27,.6)">TE CONVIENE?</div></div>
<div style="position:absolute;top:880px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end">{jars}</div>
<div class="big" style="position:absolute;top:1400px;left:0;right:0;text-align:center;font-size:60px;color:#ddd;animation:pulse 1s ease-in-out 1.6s 1 both">COMPARAMOS 3 👇</div></div>'''
    # 2 cuánto te dura: barras
    rows = ''
    for k, (img, name, size, days) in enumerate(CRE):
        d = t[1] + .5 + k * .45
        w = int(560 * days / 200)
        rows += f'''<div style="display:flex;align-items:center;gap:26px;margin-bottom:46px;animation:inL .5s ease-out {d}s both">
 <div style="width:150px;height:190px;display:flex;align-items:flex-end;justify-content:center;flex:none"><img src="{I(img)}" style="max-height:190px;max-width:150px;filter:drop-shadow(0 12px 10px #000)"></div>
 <div style="flex:1"><div style="font-weight:700;font-size:34px;letter-spacing:1px;color:#ddd">{name} · {size}</div>
  <div style="display:flex;align-items:center;gap:20px;margin-top:10px"><div style="height:54px;width:{w}px;border-radius:10px;background:linear-gradient(90deg,#b8440c,{OR});box-shadow:0 0 24px rgba(242,106,27,.5);transform-origin:left;animation:gx .9s cubic-bezier(.2,.8,.2,1) {d + .3}s both"></div>
  <div class="big o" style="font-size:90px;animation:pop .5s ease-out {d + 1}s both">{days}</div></div></div></div>'''
    b += f'''<div class="flash" style="animation:flash .35s ease-out {t[1]}s forwards"></div>
<div class="sc" style="animation:show {t[2] - t[1]}s linear {t[1]}s both"><div class="glow" style="top:700px"></div>
<div style="position:absolute;top:380px;left:70px;right:70px;animation:inL .5s ease-out {t[1] + .05}s both"><div class="big" style="font-size:110px">¿CUÁNTOS DÍAS</div><div class="big o" style="font-size:130px">TE DURA?</div></div>
<div style="position:absolute;top:720px;left:60px;right:60px">{rows}</div>
<div style="position:absolute;top:1520px;left:0;right:0;text-align:center;font-weight:700;font-size:32px;color:#bbb;text-transform:uppercase;animation:showEnd .6s linear {t[1] + 2.4}s both">Tomando 5 g al día, todos los días</div></div>'''
    # 3 qué las diferencia
    tiles = [('USN', 'Formato chico', 'Ideal para partir'), ('MUSCLETECH', 'Micronizada', 'Sin sabor o uva'), ('FINAFLEX', 'Micronizada · 1 kg', 'Certificada NSF')]
    tl = ''.join(f'''<div style="border:2px solid rgba(242,106,27,.6);background:rgba(16,11,8,.9);border-radius:22px;padding:30px 36px;margin-bottom:28px;display:flex;align-items:center;gap:28px;animation:rise .6s ease-out {t[2] + .3 + k * .3}s both">
 <img src="{I(CRE[k][0])}" style="height:150px;filter:drop-shadow(0 10px 10px #000)"><div><div class="big o" style="font-size:66px">{a}</div><div class="big" style="font-size:58px">{x}</div><div style="font-weight:700;font-size:30px;color:#bbb;text-transform:uppercase">{y}</div></div></div>'''
                 for k, (a, x, y) in enumerate(tiles))
    b += f'''<div class="flash" style="animation:flash .35s ease-out {t[2]}s forwards"></div>
<div class="sc" style="animation:show {t[3] - t[2]}s linear {t[2]}s both">
<div style="position:absolute;top:380px;left:70px;right:70px;animation:inL .5s ease-out {t[2] + .05}s both"><div class="big" style="font-size:110px">¿QUÉ LAS</div><div class="big o" style="font-size:130px">DIFERENCIA?</div></div>
<div style="position:absolute;top:700px;left:60px;right:60px">{tl}</div></div>'''
    # 4 la misma base
    b += f'''<div class="flash" style="animation:flash .35s ease-out {t[3]}s forwards"></div>
<div class="sc" style="animation:show {t[4] - t[3]}s linear {t[3]}s both"><div class="glow"></div>
<div class="big" style="position:absolute;top:420px;left:70px;font-size:70px;color:#bbb;animation:inL .5s ease-out {t[3] + .05}s both">LO IMPORTANTE</div>
<div style="position:absolute;top:540px;left:0;right:0;text-align:center;animation:slam .8s ease-out {t[3] + .25}s both"><div class="big" style="font-size:120px">LAS 3 SON</div><div class="big o" style="font-size:150px;text-shadow:0 0 40px rgba(242,106,27,.6)">MONOHIDRATO</div></div>
<div style="position:absolute;top:900px;left:90px;right:90px;text-align:center;font-weight:700;font-size:46px;line-height:1.2;text-transform:uppercase;color:#eee;animation:rise .6s ease-out {t[3] + .9}s both">La más estudiada.<br>Elige por cuánto te dura<br>y si la quieres con sabor.</div>
<div style="position:absolute;top:1240px;left:0;right:0;display:flex;justify-content:center;color:{OR};animation:pop .6s ease-out {t[3] + 1.4}s both">{gen.icon("shield-check", 170)}</div></div>'''
    # 5 cierre
    row = ''.join(f'<img src="{I(p[0])}" style="height:{h}px;margin:0 4px;filter:drop-shadow(0 20px 16px #000)">' for p, h in zip(CRE, [300, 320, 340]))
    b += f'''<div class="flash" style="animation:flash .35s ease-out {t[4]}s forwards"></div>
<div class="sc" style="animation:showEnd {R.DUR - t[4]}s linear {t[4]}s both"><div class="glow"></div>
<div style="position:absolute;top:420px;left:0;right:0;text-align:center;animation:slam .7s ease-out {t[4] + .05}s both"><div class="big" style="font-size:120px">¿CUÁL ES</div><div class="big o" style="font-size:150px">LA TUYA?</div></div>
<div style="position:absolute;top:800px;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;animation:rise .7s ease-out {t[4] + .4}s both">{row}</div>
<div style="position:absolute;top:1250px;left:0;right:0;text-align:center;animation:pop .6s ease-out {t[4] + 1}s both">
 <span class="big" style="display:inline-block;background:{OR};color:#0b0705;font-size:84px;padding:14px 40px 0;border-radius:18px;box-shadow:0 0 50px rgba(242,106,27,.6)">GUÁRDALO 📌 Y ESCRÍBENOS</span></div></div>'''
    return b


R.body = body
if __name__ == '__main__':
    R.main()
