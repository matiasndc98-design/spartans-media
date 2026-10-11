"""Reel POV 9:16: sin energía para entrenar después del trabajo (batería que se carga).
Uso (desde kit/build): python3 reel_pov_energia.py <salida.mp4>
Respaldo: ISSN (Guest et al. 2021): la cafeína mejora el rendimiento, tomada ~30-60 min antes.
Incluye la nota obligatoria del Guaraná Shot. No mezclar con Lipo 6.
"""
import sys
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R
import gen

OR = R.OR
I = R.I
GREEN = '#3ccf6e'
RED = '#e5372c'
SC = [0, 3.4, 10.4, 13.8]
R.DUR = 17.2
NOTE = 'Contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.'


def pct(t):
    return round(t / R.DUR * 100, 2)


def charge_css():
    # nivel de la batería en el tiempo (segundos, ancho %, color)
    pts = [(0, 14, RED), (SC[1] + .6, 14, RED), (SC[1] + 1.2, 40, OR), (SC[1] + 3.0, 40, OR), (SC[1] + 3.6, 62, OR),
           (SC[1] + 5.4, 62, OR), (SC[1] + 6.0, 86, OR), (SC[3] + .3, 86, OR), (SC[3] + 1.0, 100, GREEN), (R.DUR, 100, GREEN)]
    k = ''.join(f'{pct(t)}%{{width:{w}%;background:{c}}}' for t, w, c in pts)
    lab = ''.join(f'{pct(t)}%{{opacity:{o}}}' for t, o in [(0, 1), (SC[1] + 1.1, 1), (SC[1] + 1.2, 1)])
    return (f'<style>@keyframes charge{{{k}}}@keyframes blink{{0%,100%{{opacity:1}}50%{{opacity:.35}}}}'
            f'@keyframes tick{{0%{{transform:scale(0)}}60%{{transform:scale(1.2)}}100%{{transform:scale(1)}}}}</style>')


def battery():
    return f'''<div style="position:absolute;top:350px;left:0;right:0;display:flex;justify-content:center;z-index:8">
 <div style="position:relative;width:420px;height:150px;border:9px solid #eee;border-radius:26px;padding:10px">
  <div style="height:100%;border-radius:12px;box-shadow:0 0 30px rgba(242,106,27,.5);animation:charge {R.DUR}s linear 0s both"></div>
  <div style="position:absolute;right:-30px;top:40px;width:20px;height:52px;background:#eee;border-radius:0 8px 8px 0"></div>
 </div></div>'''


def body():
    t = SC
    b = charge_css() + f'{R.FX.replace("SEED", "4343")}<div class="brand"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div>' + battery()
    # 1 POV
    b += f'''<div class="sc" style="animation:show {t[1]}s linear 0s both"><div class="glow" style="top:700px"></div>
<div class="big" style="position:absolute;top:610px;left:70px;font-size:150px;color:{OR};animation:slam .7s ease-out .05s both">POV:</div>
<div style="position:absolute;top:780px;left:70px;right:70px;animation:rise .7s ease-out .5s both"><div class="big" style="font-size:104px">SON LAS 6 PM,</div><div class="big" style="font-size:104px">SALISTE DEL TRABAJO</div><div class="big" style="font-size:104px;color:#bbb">Y CERO GANAS DE</div><div class="big o" style="font-size:104px">ENTRENAR</div></div>
<div class="big" style="position:absolute;top:1290px;left:0;right:0;text-align:center;font-size:72px;color:{RED};animation:blink .8s ease-in-out 1.4s 3 both">BATERÍA BAJA 🪫</div></div>'''
    # 2 plan
    steps = [('bowl', 'COME ALGO', 'Liviano, 1 a 2 horas antes'), ('droplet', 'TOMA AGUA', 'Llega hidratado al gym'),
             ('bolt', 'CAFEÍNA', '30 a 60 min antes, si la toleras')]
    st = ''
    for k, (ic, a, d) in enumerate(steps):
        tk = t[1] + .6 + k * 2.4
        st += f'''<div style="display:flex;align-items:center;gap:28px;border:2px solid rgba(242,106,27,.6);background:rgba(16,11,8,.92);border-radius:24px;padding:28px 34px;margin-bottom:28px;animation:inL .5s ease-out {tk}s both">
 <div style="flex:none;width:110px;height:110px;border-radius:50%;background:{OR};color:#0b0705;display:grid;place-items:center">{gen.icon(ic, 64)}</div>
 <div style="flex:1"><div class="big" style="font-size:76px">{a}</div><div style="font-weight:700;font-size:34px;text-transform:uppercase;color:#cfcfcf">{d}</div></div>
 <div style="color:{GREEN};animation:tick .4s ease-out {tk + .6}s both">{gen.icon("check", 70)}</div></div>'''
    b += f'''<div class="flash" style="animation:flash .35s ease-out {t[1]}s forwards"></div>
<div class="sc" style="animation:show {t[2] - t[1]}s linear {t[1]}s both">
<div class="big" style="position:absolute;top:580px;left:70px;font-size:110px;animation:inL .5s ease-out {t[1] + .05}s both">TU PLAN 🔋</div>
<div style="position:absolute;top:740px;left:60px;right:60px">{st}</div></div>'''
    # 3 producto
    b += f'''<div class="flash" style="animation:flash .35s ease-out {t[2]}s forwards"></div>
<div class="sc" style="animation:show {t[3] - t[2]}s linear {t[2]}s both"><div class="glow" style="top:640px"></div>
<div style="position:absolute;top:580px;left:70px;animation:inL .5s ease-out {t[2] + .05}s both"><div class="big" style="font-size:96px;color:#bbb">AL PASO:</div><div class="big o" style="font-size:130px">GUARANÁ SHOT</div><div style="font-weight:700;font-size:36px;text-transform:uppercase;color:#ddd;margin-top:10px">OstroVit · 80 ml · sabor pera</div></div>
<div style="position:absolute;top:700px;right:90px;height:640px;display:flex;align-items:flex-end;animation:rise .7s ease-out {t[2] + .3}s both"><img src="{I("p_guarana.png")}" style="height:600px;transform:rotate(8deg);filter:drop-shadow(0 30px 26px #000)"></div>
<div style="position:absolute;top:1000px;left:70px;animation:pop .5s ease-out {t[2] + .9}s both"><span class="big" style="display:inline-block;background:{OR};color:#0b0705;font-size:84px;padding:12px 32px 0;border-radius:16px">200 MG CAFEÍNA</span></div>
<div style="position:absolute;top:1160px;left:70px;width:520px;font-weight:700;font-size:30px;text-transform:uppercase;color:#bbb;animation:showEnd .6s linear {t[2] + 1.3}s both">Si entrenas muy tarde, ojo con el sueño.</div>
<div style="position:absolute;top:1560px;left:70px;right:70px;text-align:center;font-size:26px;color:#aaa">{NOTE}</div></div>'''
    # 4 cierre
    b += f'''<div class="flash" style="animation:flash .35s ease-out {t[3]}s forwards"></div>
<div class="sc" style="animation:showEnd {R.DUR - t[3]}s linear {t[3]}s both"><div class="glow"></div>
<div style="position:absolute;top:620px;left:0;right:0;text-align:center;animation:slam .8s ease-out {t[3] + .9}s both"><div class="big" style="font-size:120px;color:{GREEN}">BATERÍA LLENA</div><div class="big" style="font-size:160px">A ENTRENAR 💪</div></div>
<div style="position:absolute;top:1060px;left:0;right:0;text-align:center;animation:pop .6s ease-out {t[3] + 1.6}s both">
 <span class="big" style="display:inline-block;background:{OR};color:#0b0705;font-size:78px;padding:14px 40px 0;border-radius:18px;box-shadow:0 0 50px rgba(242,106,27,.6)">GUÁRDALO 📌 Y ESCRÍBENOS</span></div>
<div style="position:absolute;top:1560px;left:70px;right:70px;text-align:center;font-size:26px;color:#aaa">Guaraná Shot: {NOTE}</div></div>'''
    return b


R.body = body
if __name__ == '__main__':
    R.main()
