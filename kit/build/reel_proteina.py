"""Reel educativo 9:16: ¿Cuánta proteína necesitas al día? (no centrado en productos).
Uso (desde kit/build): python3 reel_proteina.py <salida.mp4>
Datos: ISSN (Jäger et al. 2017) 1,4–2,0 g/kg/día para personas que entrenan. Equivalencias aproximadas.
"""
import sys, os
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else 'out.mp4']
import reel as R   # reutiliza FX, CSS base y el renderizador
import gen

OR = R.OR
SC = [0, 2.6, 6.0, 9.6, 13.6]   # inicio de cada escena
R.DUR = 17.2
I = R.I


def tile(icon, qty, what, d):
    return (f'<div style="border:2px solid rgba(242,106,27,.6);background:rgba(16,11,8,.9);border-radius:24px;padding:26px 20px;text-align:center;animation:rise .6s ease-out {d}s both">'
            f'<div style="color:{OR}">{gen.icon(icon, 110)}</div><div class="big o" style="font-size:96px;margin-top:6px">{qty}</div>'
            f'<div style="font-weight:700;font-size:30px;text-transform:uppercase;color:#ddd;line-height:1.1">{what}</div></div>')


def body():
    b = f'{R.FX.replace("SEED", "5151")}<div class="brand"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div><div class="prog"><i></i></div>'
    t = SC
    # 1 gancho
    b += f'''<div class="sc" style="animation:show {t[1]}s linear 0s both"><div class="glow"></div>
<div style="position:absolute;top:520px;left:0;right:0;text-align:center;animation:slam .8s ease-out .1s both"><div class="big" style="font-size:150px">¿CUÁNTA</div></div>
<div style="position:absolute;top:670px;left:0;right:0;text-align:center;animation:slam .8s ease-out .45s both"><div class="big o" style="font-size:210px;text-shadow:0 0 40px rgba(242,106,27,.6)">PROTEÍNA</div></div>
<div style="position:absolute;top:880px;left:0;right:0;text-align:center;animation:slam .8s ease-out .8s both"><div class="big" style="font-size:120px">NECESITAS AL DÍA?</div></div>
<div style="position:absolute;top:1120px;left:0;right:0;display:flex;justify-content:center;color:{OR};animation:pulse 1s ease-in-out 1.2s 2 both">{gen.icon("barbell", 220)}</div></div>'''
    # 2 regla
    b += f'''<div class="flash" style="animation:flash .35s ease-out {t[1]}s forwards"></div>
<div class="sc" style="animation:show {t[2] - t[1]}s linear {t[1]}s both"><div class="glow"></div>
<div class="big" style="position:absolute;top:420px;left:70px;font-size:70px;color:#bbb;animation:inL .5s ease-out {t[1] + .05}s both">SI ENTRENAS</div>
<div style="position:absolute;top:560px;left:0;right:0;text-align:center;animation:slam .8s ease-out {t[1] + .3}s both"><div class="big o" style="font-size:330px;text-shadow:0 0 50px rgba(242,106,27,.6)">1,4 – 2 G</div></div>
<div style="position:absolute;top:900px;left:0;right:0;text-align:center;animation:rise .7s ease-out {t[1] + .9}s both"><div class="big" style="font-size:110px">DE PROTEÍNA</div><div class="big" style="font-size:110px">POR KILO DE PESO</div></div>
<div style="position:absolute;top:1560px;left:0;right:0;text-align:center;font-size:24px;color:#999;animation:showEnd .6s linear {t[1] + 1.4}s both">Referencia: Sociedad Internacional de Nutrición Deportiva (ISSN)</div></div>'''
    # 3 ejemplo
    b += f'''<div class="flash" style="animation:flash .35s ease-out {t[2]}s forwards"></div>
<div class="sc" style="animation:show {t[3] - t[2]}s linear {t[2]}s both"><div class="glow"></div>
<div class="big" style="position:absolute;top:420px;left:70px;font-size:70px;color:#bbb;animation:inL .5s ease-out {t[2] + .05}s both">EJEMPLO</div>
<div style="position:absolute;top:540px;left:70px;animation:inL .6s ease-out {t[2] + .2}s both"><div class="big" style="font-size:150px">SI PESAS</div><div class="big o" style="font-size:240px">70 KG</div></div>
<div style="position:absolute;top:1010px;left:0;right:0;text-align:center;color:{OR};animation:rise .5s ease-out {t[2] + .9}s both">{gen.icon("arrow-right", 120).replace("<svg", "<svg style=\'transform:rotate(90deg)\'")}</div>
<div style="position:absolute;top:1160px;left:0;right:0;text-align:center;animation:pop .6s ease-out {t[2] + 1.3}s both">
 <span class="big" style="display:inline-block;background:{OR};color:#0b0705;font-size:150px;padding:16px 50px 0;border-radius:20px;box-shadow:0 0 50px rgba(242,106,27,.6)">98 A 140 G</span>
 <div class="big" style="font-size:70px;margin-top:20px">AL DÍA</div></div></div>'''
    # 4 cómo llegar
    tiles = ''.join(tile(*x, t[3] + .3 + k * .2) for k, x in enumerate([
        ('egg', '≈6 G', '1 huevo'), ('meat', '≈30 G', '100 g de pollo cocido'),
        ('fish', '≈25 G', '1 lata de atún'), ('glass-full', '≈25 G', '1 scoop de whey')]))
    b += f'''<div class="flash" style="animation:flash .35s ease-out {t[3]}s forwards"></div>
<div class="sc" style="animation:show {t[4] - t[3]}s linear {t[3]}s both">
<div style="position:absolute;top:400px;left:70px;right:70px;animation:inL .5s ease-out {t[3] + .05}s both"><div class="big" style="font-size:120px">¿CÓMO</div><div class="big o" style="font-size:150px">LLEGAR?</div></div>
<div style="position:absolute;top:760px;left:60px;right:60px;display:grid;grid-template-columns:1fr 1fr;gap:26px">{tiles}</div>
<div style="position:absolute;top:1560px;left:0;right:0;text-align:center;font-size:24px;color:#999">Valores aproximados</div></div>'''
    # 5 cierre
    b += f'''<div class="flash" style="animation:flash .35s ease-out {t[4]}s forwards"></div>
<div class="sc" style="animation:showEnd {R.DUR - t[4]}s linear {t[4]}s both"><div class="glow"></div>
<div style="position:absolute;top:430px;left:70px;right:70px;animation:inL .5s ease-out {t[4] + .05}s both"><div class="big" style="font-size:110px">¿NO LLEGAS</div><div class="big" style="font-size:110px">SOLO CON COMIDA?</div></div>
<div style="position:absolute;top:720px;left:70px;right:70px;font-weight:700;font-size:44px;text-transform:uppercase;color:#ddd;line-height:1.15;animation:rise .6s ease-out {t[4] + .5}s both">Un scoop de proteína al día te acerca a tu meta.</div>
<div style="position:absolute;top:960px;left:0;right:0;display:flex;justify-content:center;gap:10px;align-items:flex-end;animation:rise .7s ease-out {t[4] + .8}s both">
 <img src="{I("p_whey.png")}" style="height:330px;filter:drop-shadow(0 20px 16px #000)"><img src="{I("p_nitro.png")}" style="height:300px;filter:drop-shadow(0 20px 16px #000)"><img src="{I("p_iso100.png")}" style="height:330px;filter:drop-shadow(0 20px 16px #000)"></div>
<div style="position:absolute;top:1360px;left:0;right:0;text-align:center;animation:pop .6s ease-out {t[4] + 1.4}s both">
 <span class="big" style="display:inline-block;background:{OR};color:#0b0705;font-size:84px;padding:14px 40px 0;border-radius:18px;box-shadow:0 0 50px rgba(242,106,27,.6)">GUÁRDALO 📌 Y ESCRÍBENOS</span></div></div>'''
    return b


R.body = body
if __name__ == '__main__':
    R.main()
