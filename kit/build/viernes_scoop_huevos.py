"""Viernes 23 oct 2026 · cierre de la semana de la proteína (estilo premium).
Carrusel 4:5 comparativa "¿Cuántos huevos hay en un scoop?" (1 scoop en comida real: huevos, pollo, leche;
ISO 100 y Nitro Tech; cierre con la promo real proteína + creatina = shaker).
Historias 9:16 combo/promoción real con idea nueva REGALO MISTERIOSO (silueta borrosa -> revelación),
fórmula proteína + creatina = shaker y encuesta "¿cuál es tu dupla?" con espacio libre para el sticker.
Respaldo (USDA FoodData Central, aprox.): huevo grande ~6,3 g de proteína; pechuga de pollo cocida ~31 g/100 g;
leche ~8 g por vaso de 250 ml. 22/6,3 = 3,5 · 25/6,3 = 4 · 30/6,3 = 4,8 · 22/31*100 = 71 g · 22/8 = 2,75.
Uso (desde kit/build): python3 viernes_scoop_huevos.py <carpeta_feed> <carpeta_historias>
"""
import sys
FEED, HIST = sys.argv[1], sys.argv[2]
sys.argv = [sys.argv[0]]
import premium as P

OR = P.OR
W, H, SW, SH = P.W, P.H, P.SW, P.SH


def huevo(w, mitad=False):
    h = int(w * 1.3)
    clip = 'clip-path:inset(0 50% 0 0);' if mitad else ''
    return (f'<div style="position:relative;width:{w}px;height:{h}px;{clip}">'
            f'<div style="position:absolute;inset:0;border-radius:50% 50% 50% 50% / 60% 60% 40% 40%;'
            f'background:radial-gradient(ellipse 60% 55% at 38% 32%,#fffaf2 0%,#efe4d3 45%,#c9b89f 85%,#9c8a72 100%);'
            f'box-shadow:0 30px 40px rgba(0,0,0,.6)"></div></div>')


def num(n, total):
    return f'<div class="foot" style="right:70px;top:74px">{n:02d} / {total:02d}</div>'


def f_portada():
    b = (P.marca(70, 64) + '<div class="foot" style="right:70px;top:74px">Semana de la proteína</div>'
         + P.heroe('p_whey.png', 790, 1200, 600)
         + '<div style="position:absolute;left:70px;top:190px;width:640px"><div class="lab">Un scoop en comida real</div>'
           '<div class="h" style="font-size:150px;margin-top:20px">¿Cuántos</div><div class="h o" style="font-size:150px">huevos</div>'
           '<div class="h" style="font-size:150px">hay en un scoop?</div></div>'
         + '<div class="foot" style="left:70px;bottom:60px">Desliza</div><div class="rule" style="position:absolute;left:200px;bottom:72px;width:120px"></div>')
    return P.page(W, H, b, 'rgba(242,106,27,.12)')


def f_huevos():
    fila = ''.join(f'<div>{huevo(170)}</div>' for _ in range(3)) + f'<div>{huevo(170, True)}</div>'
    b = (P.marca(70, 64) + num(2, 6)
         + '<div style="position:absolute;left:70px;top:190px"><div class="lab">1 scoop de Whey USN · 22 g de proteína</div>'
           '<div class="h o" style="font-size:300px;margin-top:10px">3½</div><div class="h" style="font-size:150px;margin-top:-10px">huevos.</div></div>'
         + f'<div style="position:absolute;left:110px;top:800px;display:flex;gap:40px;align-items:flex-end">{fila}</div>'
         + '<div class="foot" style="left:70px;bottom:60px;font-size:18px">Un huevo grande trae unos 6 g de proteína · Fuente: USDA</div>')
    return P.page(W, H, b, 'rgba(242,190,120,.10)')


def f_dato(n, lab, grande, chico, apoyo, glow):
    b = (P.marca(70, 64) + num(n, 6) + P.heroe('p_whey.png', 860, 1190, 470)
         + f'<div style="position:absolute;left:70px;top:230px;width:720px"><div class="lab">{lab}</div>'
           f'<div class="h o" style="font-size:260px;margin-top:14px">{grande}</div><div class="h" style="font-size:120px">{chico}</div>'
           f'<div class="rule" style="margin:40px 0 26px"></div>'
           f'<div style="font-size:34px;line-height:1.3;color:#bdb8b0;font-weight:500;width:560px">{apoyo}</div></div>'
         + '<div class="foot" style="left:70px;bottom:60px;font-size:18px">Valores aproximados · Fuente: USDA</div>')
    return P.page(W, H, b, glow)


def f_tres():
    cols = [('p_whey.png', 'Whey USN', '22 g', '3½ huevos', 230, 420), ('p_iso100.png', 'ISO 100', '25 g', '4 huevos', 540, 420),
            ('p_nitro.png', 'Nitro Tech', '30 g', 'Casi 5 huevos', 850, 420)]
    row = ''.join(P.heroe(img, x, 820, hh) for img, _, _, _, x, hh in cols)
    labs = ''.join(f'<div style="position:absolute;left:{x - 160}px;width:320px;top:880px;text-align:center">'
                   f'<div class="lab">{n}</div><div class="h o" style="font-size:96px;margin-top:10px">{g}</div>'
                   f'<div class="h" style="font-size:52px;margin-top:4px">{e}</div></div>' for _, n, g, e, x, _ in cols)
    b = (P.marca(70, 64) + num(5, 6)
         + '<div style="position:absolute;left:0;right:0;top:150px;text-align:center"><div class="lab">Por scoop</div>'
           '<div class="h" style="font-size:110px;margin-top:12px">Cada tarro, <span class="o">su cuenta.</span></div></div>'
         + row + labs)
    return P.page(W, H, b, 'rgba(60,110,170,.14)')


def f_cierre():
    b = (P.marca(70, 64) + num(6, 6)
         + P.heroe('p_whey.png', 330, 1080, 470) + P.heroe('p_usn_crea.png', 590, 1080, 380) + P.heroe('p_shaker.png', 820, 1080, 420, rot=6)
         + '<div style="position:absolute;left:0;right:0;top:160px;text-align:center"><div class="lab">La comida primero</div>'
           '<div class="h" style="font-size:120px;margin-top:16px">El scoop, cuando</div><div class="h o" style="font-size:120px">no llegas.</div>'
           '<div style="font-size:32px;color:#bdb8b0;margin-top:20px;font-weight:500">Sin cocinar y en 30 segundos.</div></div>'
         + '<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center;font-weight:600;font-size:26px;letter-spacing:6px;text-transform:uppercase">'
           'Proteína + creatina <span class="o">·</span> Shaker de regalo</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.10)')


# ---------------- HISTORIAS ----------------
TOP = '<div class="foot" style="right:70px;top:162px;color:#F26A1B">Viernes de combo</div>'


def h_misterio():
    sil = (f'<img src="{P.I("p_shaker.png")}" style="position:absolute;left:540px;top:1520px;height:760px;'
           f'transform:translate(-50%,-100%);filter:brightness(0) blur(14px) drop-shadow(0 0 40px rgba(242,106,27,.55));opacity:.95">')
    b = (P.marca(70, 150) + TOP + sil
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Va gratis en tu pedido</div>'
           '<div class="h" style="font-size:200px;margin-top:22px">¿Adivinas</div><div class="h o" style="font-size:200px">qué es?</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:280px;color:#d6d1c9">Sigue mirando</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.16)')


def h_revela():
    b = (P.marca(70, 150) + TOP + P.heroe('p_shaker.png', 540, 1600, 820, rot=-4)
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Revelado</div>'
           '<div class="h" style="font-size:200px;margin-top:22px">Shaker C4.</div><div class="h o" style="font-size:200px">De regalo.</div></div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.14)')


def h_formula():
    sim = lambda s, x, y: f'<div class="h o" style="position:absolute;left:{x}px;top:{y}px;font-size:150px;transform:translate(-50%,-50%)">{s}</div>'
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Cómo se gana</div>'
           '<div class="h" style="font-size:170px;margin-top:22px">La fórmula</div><div class="h o" style="font-size:170px">espartana.</div></div>'
         + P.heroe('p_whey.png', 200, 1300, 380) + sim('+', 370, 1140) + P.heroe('p_usn_crea.png', 540, 1300, 330)
         + sim('=', 710, 1140) + P.heroe('p_shaker.png', 880, 1300, 380)
         + ''.join(f'<div class="lab" style="position:absolute;left:{x - 140}px;width:280px;top:1340px;text-align:center;color:#f4f1ec">{t}</div>'
                   for t, x in [('Proteína', 200), ('Creatina', 540), ('Gratis', 880)])
         + '<div style="position:absolute;left:0;right:0;top:1440px;text-align:center;font-size:36px;color:#d6d1c9;font-weight:500">Cualquier proteína + cualquier creatina.</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.10)')


def h_dupla():
    duo = lambda a, b_, x, lab: (P.heroe(a, x - 85, 1580, 300) + P.heroe(b_, x + 85, 1580, 250)
                                 + f'<div class="lab" style="position:absolute;left:{x - 220}px;width:440px;top:1612px;text-align:center;color:#f4f1ec">{lab}</div>')
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Elige una</div>'
           '<div class="h" style="font-size:180px;margin-top:22px">¿Cuál es</div><div class="h o" style="font-size:180px">tu dupla?</div></div>'
         + duo('p_whey.png', 'p_usn_crea.png', 290, 'Whey USN + Creatina USN') + duo('p_iso100.png', 'p_finaflex.png', 790, 'ISO 100 + Finaflex 1 kg')
         + '<div style="position:absolute;left:0;right:0;top:1190px;text-align:center;font-weight:600;font-size:26px;letter-spacing:6px;text-transform:uppercase">'
           'Pídelo por DM <span class="o">·</span> Delivery en Caldera $1.500</div>')
    # espacio libre ~300 px (y 760-1170) para el sticker de encuesta
    return P.page(SW, SH, b, 'rgba(242,106,27,.10)')


if __name__ == '__main__':
    P.render([('1_portada', f_portada()), ('2_huevos', f_huevos()),
              ('3_pollo', f_dato(3, 'O en pechuga de pollo cocida', '70 g', 'de pollo.', 'La pechuga cocida trae unos 31 g de proteína cada 100 g.', 'rgba(200,120,60,.10)')),
              ('4_leche', f_dato(4, 'O en leche', 'Casi 3', 'vasos de leche.', 'Un vaso de 250 ml trae unos 8 g de proteína.', 'rgba(120,170,220,.12)')),
              ('5_cada_tarro', f_tres()), ('6_la_comida_primero', f_cierre())], FEED, W, H)
    P.render([('1_regalo_misterioso', h_misterio()), ('2_revelado', h_revela()), ('3_formula', h_formula()),
              ('4_encuesta_tu_dupla', h_dupla())], HIST, SW, SH)
