import sys, os, json, base64
from playwright.sync_api import sync_playwright

B = os.path.dirname(os.path.abspath(__file__))
NM = os.path.join(B, '..', 'npmw', 'node_modules')
FS = os.path.join(NM, '@fontsource')
IC = os.path.join(NM, '@tabler', 'icons', 'icons', 'outline')
OUT = sys.argv[1] if len(sys.argv) > 1 else "."

def uri(p):
    ext = p.rsplit('.', 1)[1]
    mime = {'png': 'image/png', 'jpg': 'image/jpeg', 'woff2': 'font/woff2'}[ext]
    return f"data:{mime};base64," + base64.b64encode(open(p, 'rb').read()).decode()

def icon(name, size=46):
    s = open(os.path.join(IC, name + '.svg')).read()
    s = s.replace('width="24"', f'width="{size}"').replace('height="24"', f'height="{size}"')
    return s.replace('stroke-width="2"', 'stroke-width="1.8"')

def font(fam, file, weight):
    return f"@font-face{{font-family:'{fam}';src:url({uri(os.path.join(FS, file))}) format('woff2');font-weight:{weight};}}"

FONTS = (font('Bebas', 'bebas-neue/files/bebas-neue-latin-400-normal.woff2', 400)
         + font('Bebas', 'bebas-neue/files/bebas-neue-latin-ext-400-normal.woff2', 400)
         + ''.join(font('Barlow', f'barlow-condensed/files/barlow-condensed-latin-{w}-normal.woff2', w) for w in (500, 600, 700, 800)))

HELMET = uri(os.path.join(B, 'helmet.png'))
BADGE = uri(os.path.join(B, 'badge.jpg'))
OR = '#F26A1B'

CSS = FONTS + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#060504;overflow:hidden;font-family:Barlow;color:#fff;position:relative}}
#fx{{position:absolute;inset:0}}
.stripes{{position:absolute;right:-120px;top:-60px;width:620px;height:520px;
 background:repeating-linear-gradient(-45deg,rgba(242,106,27,.10) 0 3px,transparent 3px 26px);
 mask-image:radial-gradient(closest-side,#000 30%,transparent);-webkit-mask-image:radial-gradient(closest-side,#000 30%,transparent)}}
.hdr{{position:absolute;left:70px;top:58px;width:470px;text-align:center}}
.hdr .s1{{font-weight:700;font-size:34px;letter-spacing:6px}}
.hdr .s2{{font-family:Bebas;font-size:132px;line-height:.86;letter-spacing:2px;color:#f1ece6;text-shadow:0 4px 0 rgba(0,0,0,.6)}}
.hdr .ln{{display:flex;align-items:center;gap:16px;margin:8px auto 10px;width:420px}}
.hdr .ln i{{flex:1;height:3px;background:linear-gradient(90deg,transparent,{OR})}}
.hdr .ln i:last-child{{background:linear-gradient(90deg,{OR},transparent)}}
.hdr .ln img{{height:58px}}
.hdr .s3{{font-weight:600;font-size:23px;letter-spacing:5px;color:#ddd}}
.hdr .s3 b{{color:{OR}}}
.h1{{position:absolute;left:70px;top:360px;width:520px}}
.h1 .a{{font-weight:800;font-style:italic;font-size:58px;line-height:1;transform:skewX(-6deg);transform-origin:left;text-transform:uppercase}}
.h1 .b{{font-family:Bebas;font-size:128px;white-space:nowrap;display:inline-block;line-height:.9;color:{OR};text-shadow:0 0 30px rgba(242,106,27,.35)}}
.h1 .c{{font-weight:600;font-size:29px;line-height:1.15;text-transform:uppercase;margin-top:14px;color:#eee}}
.ben{{position:absolute;left:70px;top:690px;width:470px}}
.row{{display:flex;align-items:center;gap:22px;padding:15px 0;border-bottom:1px solid rgba(242,106,27,.35)}}
.row:last-child{{border:none}}
.hex{{width:84px;height:92px;flex:none;display:grid;place-items:center;color:{OR};position:relative}}
.hex svg.h{{position:absolute;inset:0}}
.row .t1{{font-weight:700;font-size:30px;text-transform:uppercase;line-height:1}}
.row .t2{{font-weight:500;font-size:24px;text-transform:uppercase;color:#cfcfcf;margin-top:4px}}
.prod{{position:absolute;left:560px;width:470px;top:250px;height:870px;display:flex;align-items:flex-end;justify-content:center}}
.prod img{{max-width:100%;max-height:100%;position:relative;z-index:2;filter:drop-shadow(0 30px 30px rgba(0,0,0,.8))}}
.glow{{position:absolute;left:440px;top:260px;width:720px;height:880px;
 background:radial-gradient(closest-side,rgba(242,106,27,.7),rgba(160,50,0,.25) 55%,transparent);filter:blur(10px)}}
.ped{{position:absolute;left:575px;top:1078px;width:440px;height:74px;border-radius:50%;
 background:radial-gradient(ellipse at 50% 40%,#2a221d,#0d0a08 70%);box-shadow:0 -6px 30px rgba(242,106,27,.35), inset 0 6px 14px rgba(255,140,60,.25)}}
.price{{position:absolute;left:70px;top:1068px;display:flex;align-items:center;gap:0;z-index:5}}
.price .lb{{background:#111;border:2px solid {OR};border-right:none;color:#fff;font-weight:700;font-size:26px;letter-spacing:3px;padding:0 18px;height:92px;display:flex;align-items:center;border-radius:14px 0 0 14px}}
.price .v{{background:{OR};color:#0b0705;font-family:Bebas;font-size:92px;line-height:1;padding:6px 26px 0;height:92px;border-radius:0 14px 14px 0;box-shadow:0 0 40px rgba(242,106,27,.45)}}
.bar{{position:absolute;left:40px;right:40px;bottom:38px;height:116px;border:1.5px solid rgba(242,106,27,.55);border-radius:16px;
 background:rgba(10,8,6,.85);display:flex;align-items:center}}
.bar .it{{flex:1;display:flex;align-items:center;justify-content:center;gap:14px;color:{OR};border-right:1px solid rgba(255,255,255,.18);height:70px}}
.bar .it:last-child{{border:none}}
.bar .it span{{color:#fff;font-weight:600;font-size:23px;line-height:1.05;text-transform:uppercase}}
.note{{position:absolute;left:72px;top:1166px;font-size:17px;color:#aaa;font-weight:500;letter-spacing:.5px}}
"""

HEXSVG = f'<svg class="h" viewBox="0 0 84 92"><polygon points="42,3 80,24 80,68 42,89 4,68 4,24" fill="rgba(242,106,27,.07)" stroke="{OR}" stroke-width="2.5"/></svg>'

BAR = [('shield-check', 'Calidad<br>garantizada'), ('award', 'Productos<br>originales'),
       ('run', 'Máximo<br>rendimiento'), ('truck-delivery', 'Envíos a<br>todo Chile')]

FIT = "<script>document.fonts.ready.then(()=>{document.querySelectorAll('.h1 .b,.fit').forEach(e=>{let f=parseFloat(getComputedStyle(e).fontSize);const W=+(e.dataset.w||500);while(e.scrollWidth>W&&f>60){f-=2;e.style.fontSize=f+'px'}});document.body.dataset.ok=1});</script>"
FX = """<canvas id="fx" width="1080" height="1350"></canvas><script>
const c=document.getElementById('fx').getContext('2d');let s=SEED;function r(){s=(s*16807)%2147483647;return s/2147483647}
let g=c.createRadialGradient(780,1350,50,780,1300,900);g.addColorStop(0,'rgba(200,70,10,.35)');g.addColorStop(1,'rgba(0,0,0,0)');c.fillStyle=g;c.fillRect(0,0,1080,1350);
for(let i=0;i<14;i++){let x=r()*1080,y=500+r()*850,rad=150+r()*260;let gg=c.createRadialGradient(x,y,0,x,y,rad);gg.addColorStop(0,'rgba(120,60,30,.10)');gg.addColorStop(1,'rgba(0,0,0,0)');c.fillStyle=gg;c.fillRect(0,0,1080,1350)}
for(let i=0;i<260;i++){let x=r()*1080,y=r()*1350,w=r();let bias=Math.exp(-Math.pow((x-790)/320,2));if(r()>bias*0.85+0.15)continue;
 c.fillStyle=`rgba(255,${120+r()*90|0},${30+r()*40|0},${0.25+w*0.7})`;c.shadowColor='rgba(255,120,30,.9)';c.shadowBlur=6+w*10;
 c.beginPath();c.arc(x,y,0.6+w*2.4,0,7);c.fill()}
</script>"""

def bar_html():
    return '<div class="bar">' + ''.join(f'<div class="it">{icon(i, 44)}<span>{t}</span></div>' for i, t in BAR) + '</div>'

def header():
    return (f'<div class="hdr"><div class="s1">SUPLEMENTOS</div><div class="s2">SPARTANS</div>'
            f'<div class="ln"><i></i><img src="{HELMET}"><i></i></div>'
            f'<div class="s3">FUERZA <b>•</b> RENDIMIENTO <b>•</b> DISCIPLINA</div></div>')

def product_slide(d, seed):
    rows = ''.join(f'<div class="row"><div class="hex">{HEXSVG}{icon(ic, 42)}</div><div><div class="t1">{a}</div><div class="t2">{b}</div></div></div>'
                   for ic, a, b in d['ben'])
    note = f'<div class="note">{d["note"]}</div>' if d.get('note') else ''
    return (f'<html><head><style>{CSS}</style></head><body>{FX.replace("SEED", str(seed))}<div class="stripes"></div>'
            f'<div class="glow"></div><div class="ped"></div>'
            f'<div class="prod" style="height:{d.get("h", 820)}px;top:{1100 - d.get("h", 820)}px;align-items:{d.get("align", "flex-end")}"><img src="{uri(os.path.join(B, d["img"]))}" style="{d.get("imgstyle", "")}"></div>'
            f'{header()}<div class="h1"><div class="a">{d["a"]}</div><div class="b">{d["b"]}</div><div class="c">{d["c"]}</div></div>'
            f'<div class="ben">{rows}</div><div class="price"><div class="lb">PRECIO</div><div class="v">{d["price"]}</div></div>'
            f'{note}{bar_html()}{FIT}</body></html>')

def render(pages):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1080, 'height': 1350})
        for name, html in pages:
            pg.set_content(html, wait_until='load'); pg.wait_for_selector('body[data-ok]');pg.wait_for_timeout(300)
            pg.screenshot(path=os.path.join(OUT, name + '.png'))
            print(name)
        b.close()
