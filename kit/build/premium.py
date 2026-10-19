"""Estilo PREMIUM (pedido del dueño el 19 oct: "lo anterior parece de cabro chico").
Inspirado en marcas grandes (Gymshark, Optimum Nutrition, Ghost): una idea por imagen, titular corto y grande,
producto como héroe con luz de estudio y reflejo, mucho espacio negro, naranjo solo como acento.
Nada de timbres, recuadros, chips ni íconos de relleno.
Uso (desde kit/build): python3 premium.py <carpeta_feed> <carpeta_historias>
"""
import sys, os
sys.path.insert(0, '.')
import gen
from playwright.sync_api import sync_playwright

FEED = sys.argv[1] if len(sys.argv) > 1 else 'feed'
HIST = sys.argv[2] if len(sys.argv) > 2 else 'hist'
OR = '#F26A1B'
I = lambda n: gen.uri(os.path.join(gen.B, n))

CSS = gen.FONTS + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#0a0a0a;color:#f4f1ec;font-family:Barlow;overflow:hidden;position:relative}}
.stage{{position:absolute;inset:0;background:radial-gradient(ellipse 70% 55% at 50% 46%,#2b2b2b 0%,#151515 45%,#090909 80%)}}
.floor{{position:absolute;left:0;right:0;bottom:0;background:linear-gradient(180deg,rgba(255,255,255,0) 0%,rgba(255,255,255,.035) 40%,rgba(0,0,0,.6) 100%)}}
.grain{{position:absolute;inset:0;opacity:.07;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/></filter><rect width='200' height='200' filter='url(%23n)'/></svg>")}}
.h{{font-family:Bebas;line-height:.86;letter-spacing:1px;text-transform:uppercase}}
.lab{{font-weight:600;font-size:22px;letter-spacing:7px;text-transform:uppercase;color:#9a958e}}
.o{{color:{OR}}}
.mark{{position:absolute;display:flex;align-items:center;gap:12px;font-family:Bebas;font-size:30px;letter-spacing:4px;color:#f4f1ec}}
.mark img{{height:40px}}
.prod{{position:absolute;filter:drop-shadow(0 40px 50px rgba(0,0,0,.75))}}
.refl{{position:absolute;transform:scaleY(-1);opacity:.18;-webkit-mask-image:linear-gradient(0deg,rgba(0,0,0,.9),transparent 35%);mask-image:linear-gradient(0deg,rgba(0,0,0,.9),transparent 35%)}}
.rule{{height:2px;background:{OR};width:80px}}
.foot{{position:absolute;font-weight:600;font-size:22px;letter-spacing:5px;text-transform:uppercase;color:#8d8880}}
"""
DONE = "<script>document.fonts.ready.then(()=>document.body.dataset.ok=1)</script>"


def page(w, h, body, glow='rgba(242,106,27,.10)'):
    return (f'<html><head><style>{CSS}body{{width:{w}px;height:{h}px}}</style></head><body>'
            f'<div class="stage"></div><div style="position:absolute;inset:0;background:radial-gradient(ellipse 50% 35% at 50% 55%,{glow},transparent 70%)"></div>'
            f'<div class="floor" style="height:{int(h*.32)}px"></div>{body}<div class="grain"></div>{DONE}</body></html>')


def heroe(img, cx, base_y, height, rot=0):
    """Producto parado en el piso (base_y) con reflejo."""
    s = f'left:{cx}px;top:{base_y}px;height:{height}px;transform:translate(-50%,-100%) rotate({rot}deg)'
    r = f'left:{cx}px;top:{base_y}px;height:{height}px;transform:translate(-50%,0) scaleY(-1) rotate({-rot}deg)'
    return f'<img class="prod" src="{I(img)}" style="{s}"><img class="refl" src="{I(img)}" style="{r}">'


def marca(x, y):
    return f'<div class="mark" style="left:{x}px;top:{y}px"><img src="{gen.HELMET}">SPARTANS</div>'


# ---------------- CARRUSEL 4:5 "4 mitos de la proteína" ----------------
W, H = 1080, 1350
MITOS = [
    ('01', 'Si no la tomas apenas<br>terminas, se pierde.', 'Lo que importa es cuánta proteína comes en el día. Tómala cuando te acomode.', 'p_whey.png', 'rgba(40,80,200,.16)'),
    ('02', 'Es solo para<br>ponerse enormes.', 'Es proteína de leche en polvo. Te ayuda a llegar a tu meta del día, entrenes por fuerza, salud o rendimiento.', 'p_iso100.png', 'rgba(60,110,170,.16)'),
    ('03', 'Daña los riñones.', 'En personas sanas y a dosis recomendadas no se ha visto daño. Si tienes una enfermedad renal, consulta a tu médico.', 'p_nitro.png', 'rgba(200,30,30,.14)'),
    ('04', 'Un batido reemplaza<br>una comida.', 'Es un complemento. Primero comida real; el scoop completa lo que te falta.', 'p_barra.png', 'rgba(120,170,220,.14)'),
]


def portada():
    b = (marca(70, 64) + '<div class="foot" style="right:70px;top:74px">Semana de la proteína</div>'
         + heroe('p_whey.png', 540, 1190, 560)
         + '<div style="position:absolute;left:70px;top:180px"><div class="lab">Lo que nadie te explica</div>'
           '<div class="h" style="font-size:190px;margin-top:18px">4 mitos</div><div class="h o" style="font-size:120px">de la proteína.</div></div>'
         + '<div class="foot" style="left:70px;bottom:60px">Desliza</div><div class="rule" style="position:absolute;left:200px;bottom:72px;width:120px"></div>')
    return page(W, H, b, 'rgba(242,106,27,.12)')


def mito(n, frase, verdad, img, glow):
    big_side = 'p_barra.png' != img
    prod = (heroe(img, 890, 1190, 640) if big_side else
            f'<img class="prod" src="{I(img)}" style="left:600px;top:820px;width:560px;transform:rotate(-24deg)">')
    b = (marca(70, 64) + f'<div class="foot" style="right:70px;top:74px">Mito {n} / 04</div>'
         + f'<div class="h" style="position:absolute;left:56px;top:150px;font-size:260px;color:transparent;-webkit-text-stroke:2px rgba(244,241,236,.22)">{n}</div>'
         + prod
         + f'<div style="position:absolute;left:70px;top:430px;width:500px"><div class="lab o" style="color:{OR}">Mito</div>'
           f'<div class="h" style="font-size:84px;margin-top:16px">“{frase}”</div>'
           f'<div class="rule" style="margin:40px 0 26px"></div><div class="lab" style="color:#f4f1ec">La verdad</div>'
           f'<div style="font-size:34px;line-height:1.3;color:#bdb8b0;margin-top:12px;font-weight:500">{verdad}</div></div>'
         + '<div class="foot" style="left:70px;bottom:60px;font-size:18px">Fuente: Sociedad Internacional de Nutrición Deportiva (ISSN)</div>')
    return page(W, H, b, glow)


def cierre():
    b = (marca(70, 64) + '<div class="foot" style="right:70px;top:74px">Spartans</div>'
         + heroe('p_iso100.png', 300, 1060, 470) + heroe('p_whey.png', 560, 1080, 520) + heroe('p_nitro.png', 815, 1060, 470)
         + '<div style="position:absolute;left:0;right:0;top:170px;text-align:center"><div class="lab">La verdad</div>'
           '<div class="h" style="font-size:150px;margin-top:16px">1 scoop.</div><div class="h o" style="font-size:150px">22 a 30 g.</div>'
           '<div style="font-size:30px;color:#bdb8b0;margin-top:22px;font-weight:500">Whey USN · ISO 100 · Nitro Tech</div></div>'
         + '<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center;font-weight:600;font-size:26px;letter-spacing:6px;text-transform:uppercase">'
           'Pídela por DM <span class="o">·</span> Con creatina, shaker de regalo</div>')
    return page(W, H, b, 'rgba(242,106,27,.10)')


# ---------------- HISTORIAS 9:16 ----------------
SW, SH = 1080, 1920


def h1():
    b = (marca(70, 150) + heroe('p_iso100.png', 540, 1500, 820)
         + '<div style="position:absolute;left:0;right:0;top:300px;text-align:center"><div class="lab">Desde hoy</div>'
           '<div class="h" style="font-size:150px;margin-top:20px">Semana de la</div><div class="h o" style="font-size:230px">proteína.</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:280px">Mitos, dudas y cuál elegir</div>')
    return page(SW, SH, b, 'rgba(60,110,170,.18)')


def h2():
    b = (marca(70, 150) + '<div style="position:absolute;left:80px;right:80px;top:420px"><div class="lab o" style="color:#F26A1B">¿Mito o verdad?</div>'
         '<div class="h" style="font-size:130px;margin-top:26px">“Si no la tomas apenas terminas de entrenar,</div><div class="h o" style="font-size:130px">se pierde.”</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:300px">Responde y mira la siguiente</div>')
    return page(SW, SH, b, 'rgba(242,106,27,.08)')


def h3():
    b = (marca(70, 150) + heroe('p_whey.png', 780, 1560, 560)
         + '<div style="position:absolute;left:80px;top:400px"><div class="lab">La respuesta</div><div class="h o" style="font-size:330px;margin-top:10px">Mito.</div></div>'
         + '<div style="position:absolute;left:80px;width:520px;top:840px"><div class="rule" style="margin-bottom:28px"></div>'
           '<div style="font-size:44px;line-height:1.25;font-weight:500;color:#e8e4dd">Lo que importa es cuánta proteína comes en el día. Tómala cuando te acomode.</div>'
           '<div class="foot" style="position:static;margin-top:40px">3 mitos más en el post de hoy</div></div>')
    return page(SW, SH, b, 'rgba(40,80,200,.14)')


def h4():
    items = [('p_whey.png', 'Chocolate', 330), ('p_iso100.png', 'Cocoa Pebbles', 330), ('p_nitro.png', 'Vainilla', 320)]
    row = ''.join(heroe(img, x, 1060, hh) for (img, _, hh), x in zip(items, [230, 540, 850]))
    labs = ''.join(f'<div style="position:absolute;top:1100px;left:{x - 150}px;width:300px;text-align:center" class="lab">{t}</div>'
                   for (_, t, _), x in zip(items, [230, 540, 850]))
    b = (marca(70, 150) + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Elige uno</div>'
         '<div class="h" style="font-size:150px;margin-top:20px">¿Qué sabor</div><div class="h o" style="font-size:150px">te tienta?</div></div>'
         + row + labs)
    return page(SW, SH, b, 'rgba(242,106,27,.10)')


def render(pages, out, w, h):
    os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch(); pg = br.new_page(viewport={'width': w, 'height': h})
        for n, html in pages:
            pg.set_content(gen.sin_emoji(html), wait_until='load'); pg.wait_for_selector('body[data-ok]'); pg.wait_for_timeout(300)
            png = os.path.join(out, n + '.png'); pg.screenshot(path=png)
            from PIL import Image
            Image.open(png).convert('RGB').save(png[:-4] + '.jpg', quality=92); os.remove(png); print(n)
        br.close()


if __name__ == '__main__':
    render([('1_portada', portada())] + [(f'{i + 2}_mito{i + 1}', mito(*m)) for i, m in enumerate(MITOS)] + [('6_la_verdad', cierre())], FEED, W, H)
    render([('1_semana_proteina', h1()), ('2_mito_o_verdad', h2()), ('3_respuesta', h3()), ('4_sabores', h4())], HIST, SW, SH)
