import sys, os; sys.path.insert(0,'.')
import gen
from playwright.sync_api import sync_playwright
OR='#F26A1B'
def I(n): return gen.uri(os.path.join(gen.B,n))
FX=gen.FX.replace('height="1350"','height="1920"').replace('1080,1350','1080,1920').replace('780,1350','540,1900').replace('780,1300','540,1500').replace('y=500+r()*850','y=200+r()*1720').replace('y=r()*1350','y=r()*1920').replace('(x-790)/320','(x-540)/600')
css=gen.FONTS+f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;background:#060504;overflow:hidden;font-family:Barlow;color:#fff;position:relative}}
#fx{{position:absolute;inset:0;opacity:.8}}
.wall{{position:absolute;inset:0;background:
 repeating-linear-gradient(0deg,rgba(255,255,255,.025) 0 2px,transparent 2px 70px),
 repeating-linear-gradient(90deg,rgba(255,255,255,.02) 0 2px,transparent 2px 140px),
 radial-gradient(ellipse at 50% 55%,rgba(242,106,27,.22),transparent 60%)}}
.brand{{position:absolute;top:190px;left:70px;display:flex;align-items:center;gap:16px}}
.brand img{{height:62px}}.brand div{{font-family:Bebas;font-size:46px;letter-spacing:2px;line-height:.9}}.brand small{{display:block;font-family:Barlow;font-weight:700;font-size:20px;letter-spacing:5px;color:#bbb}}
.neon{{position:absolute;top:330px;left:0;right:0;text-align:center;font-family:Bebas;font-size:150px;line-height:.9;color:#ffe2cc;
 text-shadow:0 0 6px #fff,0 0 18px {OR},0 0 42px {OR},0 0 90px {OR}}}
.neon small{{display:block;font-size:64px;letter-spacing:10px;color:{OR};text-shadow:0 0 20px rgba(242,106,27,.8)}}
.shelf{{position:absolute;left:40px;right:40px;height:30px;border-radius:4px;
 background:linear-gradient(#3a2c22,#1b140f);box-shadow:0 18px 30px rgba(0,0,0,.8),0 -2px 0 rgba(255,160,90,.35) inset}}
.shelf:after{{content:'';position:absolute;left:0;right:0;top:30px;height:14px;background:linear-gradient(#120d0a,transparent)}}
.light{{position:absolute;left:60px;right:60px;height:6px;border-radius:3px;background:{OR};box-shadow:0 0 18px {OR},0 0 60px rgba(242,106,27,.8)}}
.row{{position:absolute;left:40px;right:40px;display:flex;align-items:flex-end;justify-content:space-evenly}}
.row img{{filter:drop-shadow(0 18px 14px rgba(0,0,0,.9));}}
.cta{{position:absolute;bottom:230px;left:0;right:0;text-align:center}}
.cta .k{{display:inline-block;background:{OR};color:#0b0705;font-family:Bebas;font-size:66px;padding:12px 40px 2px;border-radius:14px;box-shadow:0 0 40px rgba(242,106,27,.5)}}
.cta .s{{font-weight:700;font-size:30px;letter-spacing:2px;margin-top:20px;text-transform:uppercase;color:#ddd}}
"""
body=f"""{FX.replace('SEED','2026')}<div class="wall"></div>
<div class="brand"><img src="{gen.HELMET}"><div>SPARTANS<small>SUPLEMENTOS</small></div></div>
<div class="neon">STOCK<small>DISPONIBLE HOY</small></div>
<div class="light" style="top:600px"></div>
<div class="row" style="top:620px;height:440px">
 <img src="{I('p_mt_sin.png')}" style="height:330px"><img src="{I('p_whey.png')}" style="height:430px"><img src="{I('p_mt_uva.png')}" style="height:330px"></div>
<div class="shelf" style="top:1060px"></div>
<div class="light" style="top:1120px"></div>
<div class="row" style="top:1140px;height:330px">
 <img src="{I('p_usn_crea.png')}" style="height:290px"><img src="{I('p_lipo.png')}" style="height:300px"><img src="{I('p_multi.png')}" style="height:280px"><img src="{I('p_shaker.png')}" style="height:320px"></div>
<div class="shelf" style="top:1470px"></div>
<div class="cta"><div class="k">PIDE EL TUYO POR DM</div><div class="s">Delivery en Caldera $1.500 · Envíos a todo Chile</div></div>
<script>document.fonts.ready.then(()=>document.body.dataset.ok=1)</script>"""
html=f'<html><head><style>{css}</style></head><body>{body}</body></html>'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.set_content(gen.sin_emoji(html),wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
    pg.screenshot(path=sys.argv[1]); b.close()
