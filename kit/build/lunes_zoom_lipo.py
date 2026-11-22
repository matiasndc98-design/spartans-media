"""Lunes 23 nov 2026 · abre la semana de la energía · estilo SOBRIO.
Carrusel 4:5 "Energía. Para entrenar." con idea nueva ZOOM PROGRESIVO (cada lámina se acerca más al envase:
de producto completo a primerísimo plano de la etiqueta; el deslizar se siente como un acercamiento de cámara).
Lipo 6 Black: 60 cápsulas, una al día (lo dice la etiqueta: "One pill daily"), 222 mg de cafeína por cápsula.
Lámina 5: Guaraná Shot como alternativa ("Elige uno. Los dos tienen cafeína."), nunca combinados.
Historias 9:16: macro "Lunes. Se enciende." + encuesta "¿A qué hora entrenas?".
Sin precios, sin numeración en historias. Uso (desde kit/build): python3 lunes_zoom_lipo.py <carpeta_feed> <carpeta_historias>
"""
import sys
FEED = sys.argv[1] if len(sys.argv) > 1 else 'feed'
HIST = sys.argv[2] if len(sys.argv) > 2 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

W, H, N = 1080, 1350, 6
SW, SH = P.SW, P.SH
OR = P.OR
NOTA_LIPO = 'Contiene cafeína (222 mg por cápsula). No apto para menores ni embarazadas.'
NOTA_GUA = 'Contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.'
LIPO_AR = 566 / 1120  # ancho / alto de p_lipo.png


def num(i):
    return f'<div class="foot" style="right:70px;top:74px">{i:02d} / 0{N}</div>'


def lipo(cx, cy, h, extra=''):
    """Envase de Lipo 6 centrado en (cx, cy) con alto h (sin piso: toma de cámara)."""
    return (f'<img class="prod" src="{P.I("p_lipo.png")}" style="left:{cx}px;top:{cy}px;height:{h}px;'
            f'transform:translate(-50%,-50%);{extra}">')


def sombra_txt(lado='left', ancho=60):
    # degradado negro para que el titular se lea sobre el envase ampliado
    d = '90deg' if lado == 'left' else '270deg'
    return (f'<div style="position:absolute;inset:0;background:linear-gradient({d},rgba(6,5,4,.92) 0%,'
            f'rgba(6,5,4,.75) {ancho - 20}%,transparent {ancho}%)"></div>')


def l1():
    b = (P.marca(70, 64) + num(1) + P.heroe('p_lipo.png', 780, 1200, 620)
         + '<div style="position:absolute;left:70px;top:230px"><div class="lab">Semana de la energía</div>'
           '<div class="h" style="font-size:200px;margin-top:30px">Energía.</div>'
           '<div class="h o" style="font-size:150px">Para entrenar.</div></div>'
         + '<div style="position:absolute;left:70px;top:820px;width:420px">'
           '<div style="font-family:Bebas;font-size:120px;line-height:.9">60 <span class="o">días.</span></div>'
           '<div class="lab" style="margin-top:12px;color:#c9c4bd">60 cápsulas · una al día</div></div>'
         + '<div class="foot" style="left:70px;bottom:70px">Guárdalo · Desliza</div>'
           '<div class="rule" style="position:absolute;left:400px;bottom:82px;width:120px"></div>')
    return P.page(W, H, b, 'rgba(200,30,30,.10)')


def l2():
    # más cerca: el envase llena el alto y se corta abajo
    b = (lipo(900, 860, 1500) + sombra_txt('left', 50) + P.marca(70, 64) + num(2)
         + '<div style="position:absolute;left:70px;top:300px"><div class="lab">Lipo 6 Black · Nutrex</div>'
           '<div class="h" style="font-size:210px;margin-top:24px">Una</div>'
           '<div class="h o" style="font-size:210px">al día.</div></div>'
         + '<div class="foot" style="left:70px;bottom:70px;color:#c9c4bd">Una cápsula por porción</div>')
    return P.page(W, H, b, 'rgba(200,30,30,.10)')


def l3():
    # primer plano del "LIPO 6"
    b = (lipo(780, 760, 2300) + sombra_txt('left', 72) + P.marca(70, 64) + num(3)
         + '<div style="position:absolute;left:70px;top:330px"><div class="lab">Cafeína por cápsula</div>'
           '<div class="h o" style="font-size:300px;margin-top:20px">222 mg.</div></div>'
         + f'<div class="foot" style="left:70px;bottom:70px;width:700px;line-height:1.5;color:#c9c4bd;font-size:20px">{NOTA_LIPO}</div>')
    return P.page(W, H, b, 'rgba(200,30,30,.08)')


def l4():
    # primerísimo plano del "60" de la etiqueta (esquina inferior izquierda del envase)
    h = 2500
    w = h * LIPO_AR
    # el "60" está en ~(0.13, 0.84) del envase: llevarlo a (360, 760) en la lámina
    cx = 250 - (0.13 - 0.5) * w
    cy = 760 - (0.84 - 0.5) * h
    b = (lipo(cx, cy, h) + sombra_txt('right', 66) + P.marca(70, 64) + num(4)
         + '<div style="position:absolute;right:70px;top:300px;text-align:right"><div class="lab">Un frasco</div>'
           '<div class="h" style="font-size:230px;margin-top:24px">60</div>'
           '<div class="h o" style="font-size:230px">días.</div></div>'
         + '<div class="foot" style="right:70px;bottom:70px;text-align:right;color:#c9c4bd">60 cápsulas · una al día</div>')
    return P.page(W, H, b, 'rgba(200,30,30,.06)')


def l5():
    b = (P.marca(70, 64) + num(5) + P.heroe('p_guarana.png', 800, 1180, 760)
         + '<div style="position:absolute;left:70px;top:230px;width:560px"><div class="lab">Guaraná Shot · OstroVit · pera</div>'
           '<div class="h" style="font-size:170px;margin-top:24px">¿Mejor</div>'
           '<div class="h o" style="font-size:170px">un shot?</div>'
           '<div style="font-size:36px;color:#c9c4bc;font-weight:500;margin-top:34px;line-height:1.3">80 ml. 200 mg de cafeína.<br>'
           'Elige uno. Los dos tienen cafeína.</div></div>'
         + f'<div class="foot" style="left:70px;bottom:70px;width:560px;line-height:1.5;color:#c9c4bd;font-size:20px">{NOTA_GUA}</div>')
    return P.page(W, H, b, 'rgba(160,200,80,.08)')


def l6():
    b = (P.marca(70, 64) + num(6)
         + P.heroe('p_lipo.png', 340, 1060, 480) + P.heroe('p_guarana.png', 760, 1060, 480)
         + '<div style="position:absolute;left:0;right:0;top:160px;text-align:center"><div class="lab">Responde con una palabra</div>'
           '<div class="h" style="font-size:150px;margin-top:16px">¿Cápsula</div><div class="h o" style="font-size:150px">o shot?</div></div>'
         + '<div style="position:absolute;left:0;right:0;bottom:120px;text-align:center;font-weight:600;font-size:26px;'
           'letter-spacing:6px;text-transform:uppercase">Pídelo por DM <span class="o">·</span> Delivery Caldera $1.500</div>'
         + '<div class="foot" style="left:0;right:0;bottom:66px;text-align:center;font-size:17px;letter-spacing:2px">'
           'Contienen cafeína: 222 mg por cápsula · 200 mg por shot. No apto para menores ni embarazadas.</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.08)')


def h_enciende():
    h = 3600
    b = (lipo(560, 860, h) + '<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,5,4,.2) 0%,'
         'rgba(6,5,4,.0) 30%,rgba(6,5,4,.85) 62%,rgba(6,5,4,.97) 78%)"></div>'
         + P.marca(70, 280)
         + '<div style="position:absolute;left:70px;top:1150px"><div class="lab">Lunes</div>'
           '<div class="h" style="font-size:210px;margin-top:20px">Se <span class="o">enciende.</span></div>'
           '<div class="foot" style="position:static;margin-top:30px;color:#f4f1ec">Lipo 6 Black · Una al día · Pídelo por DM</div>'
           f'<div style="margin-top:22px;font-weight:500;font-size:26px;line-height:1.3;color:#8d8880;width:900px">{NOTA_LIPO}</div></div>')
    return P.page(SW, SH, b, 'rgba(200,30,30,.06)')


def h_hora():
    # espacio libre ~720–1080 para el sticker de encuesta
    b = (P.marca(70, 280)
         + '<div style="position:absolute;left:0;right:0;top:360px;text-align:center"><div class="lab">Semana de la energía</div>'
           '<div class="h" style="font-size:160px;margin-top:24px">¿A qué hora</div><div class="h o" style="font-size:160px">entrenas?</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:300px;color:#c9c4bd">Mañana o tarde · Vota</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.07)')


if __name__ == '__main__':
    P.render([('1_energia_para_entrenar', l1()), ('2_una_al_dia', l2()), ('3_222_mg', l3()),
              ('4_60_dias', l4()), ('5_mejor_un_shot', l5()), ('6_capsula_o_shot', l6())], FEED, W, H)
    P.render([('1_lunes_se_enciende', h_enciende()), ('2_a_que_hora_entrenas', h_hora())], HIST, SW, SH)
