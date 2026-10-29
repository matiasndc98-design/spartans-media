"""Viernes 30 oct 2026 · semana de la energía (estilo premium, paquete liviano).
Carrusel 4:5 "Entrenas a las 6 PM: tu día, hora por hora" — idea nueva AGENDA HORA POR HORA con línea de tiempo
abajo que avanza en cada lámina (4 PM comer liviano → 5:15 PM Guaraná Shot → 6 PM entrenar → 7:30 PM batido + creatina
→ 10 PM dormir). Producto dentro de una rutina real, no catálogo.
Respaldo: cafeína 30–60 min antes (ISSN 2021); vida media ~5 h (EFSA 2015): shot a las 5:15 PM → ~10 PM queda la mitad;
creatina 3–5 g/día a cualquier hora (ISSN). Nada de precios.
Historias 9:16 combo/promoción real con idea nueva LA RECETA DEL COMBO (ingredientes → preparación) y encuesta
"¿Ya tienes shaker?" con espacio libre ~300 px.
Uso (desde kit/build): python3 viernes_hora_por_hora.py <carpeta_feed> <carpeta_historias>
"""
import sys
FEED, HIST = sys.argv[1], sys.argv[2]
sys.argv = [sys.argv[0]]
import premium as P

OR = P.OR
W, H, SW, SH = P.W, P.H, P.SW, P.SH
HORAS = ['4 PM', '5:15 PM', '6 PM', '7:30 PM', '10 PM']
NOTA_G = 'Guaraná Shot: contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.'


def linea(activa):
    """Línea de tiempo inferior: puntos por hora, la actual en naranjo."""
    x0, x1, y = 110, 970, 1205
    paso = (x1 - x0) / (len(HORAS) - 1)
    pr = x0 + paso * activa if activa >= 0 else x0
    s = (f'<div style="position:absolute;left:{x0}px;width:{x1 - x0}px;top:{y}px;height:2px;background:rgba(244,241,236,.18)"></div>'
         f'<div style="position:absolute;left:{x0}px;width:{pr - x0}px;top:{y}px;height:2px;background:{OR}"></div>')
    for i, hr in enumerate(HORAS):
        x = x0 + paso * i
        on = i == activa
        past = i < activa
        col = OR if (on or past) else 'rgba(244,241,236,.35)'
        d = 22 if on else 12
        s += (f'<div style="position:absolute;left:{x}px;top:{y + 1}px;width:{d}px;height:{d}px;border-radius:50%;'
              f'background:{col};transform:translate(-50%,-50%);{"box-shadow:0 0 24px rgba(242,106,27,.8)" if on else ""}"></div>'
              f'<div style="position:absolute;left:{x - 90}px;width:180px;top:{y + 26}px;text-align:center;font-weight:600;'
              f'font-size:{24 if on else 20}px;letter-spacing:3px;color:{"#f4f1ec" if on else "#8d8880"}">{hr}</div>')
    return s


def num(n):
    return f'<div class="foot" style="right:70px;top:74px">{n:02d} / 06</div>'


def nota(y=1110):
    return f'<div class="foot" style="left:70px;right:70px;top:{y}px;font-size:17px;letter-spacing:2px">{NOTA_G}</div>'


def f_portada():
    b = (P.marca(70, 64) + '<div class="foot" style="right:70px;top:74px">Semana de la energía</div>'
         + P.heroe('p_guarana.png', 830, 1060, 640, 6)
         + '<div style="position:absolute;left:70px;top:190px;width:620px"><div class="lab">Hora por hora</div>'
           '<div class="h" style="font-size:150px;margin-top:20px">Entrenas</div><div class="h o" style="font-size:150px">a las 6 PM.</div>'
           '<div class="rule" style="margin:40px 0 26px"></div>'
           '<div style="font-size:36px;line-height:1.28;color:#bdb8b0;font-weight:500;width:520px">Así se arma tu día para llegar con energía y dormir bien después.</div></div>'
         + nota() + linea(-1)
         + '<div class="foot" style="left:70px;top:1290px;font-size:18px">Desliza</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.12)')


def f_paso(n, act, lab, t1, t2, apoyo, prods, glow, extra=''):
    b = (P.marca(70, 64) + num(n)
         + f'<div class="h o" style="position:absolute;left:62px;top:150px;font-size:230px">{HORAS[act]}</div>'
         + prods
         + f'<div style="position:absolute;left:70px;top:390px;width:560px"><div class="lab">{lab}</div>'
           f'<div class="h" style="font-size:110px;margin-top:18px">{t1}</div><div class="h" style="font-size:110px">{t2}</div>'
           f'<div class="rule" style="margin:36px 0 24px"></div>'
           f'<div style="font-size:34px;line-height:1.3;color:#bdb8b0;font-weight:500">{apoyo}</div></div>'
         + extra + linea(act))
    return P.page(W, H, b, glow)


def f_cierre():
    b = (P.marca(70, 64) + num(6)
         + '<div class="h o" style="position:absolute;left:62px;top:150px;font-size:230px">10 PM</div>'
         + '<div style="position:absolute;left:70px;top:390px;width:900px"><div class="lab">Apaga la pantalla</div>'
           '<div class="h" style="font-size:130px;margin-top:18px">A dormir.</div>'
           '<div class="rule" style="margin:36px 0 24px"></div>'
           '<div style="font-size:36px;line-height:1.3;color:#bdb8b0;font-weight:500;width:820px">A esta hora todavía queda cerca de la mitad de la cafeína del shot. '
           'Si te cuesta dormir, adelanta el entreno o sáltate el shot.</div>'
           '<div class="h" style="font-size:72px;margin-top:60px">Guárdalo y <span class="o">ajústalo a tu hora.</span></div></div>'
         + '<div class="foot" style="left:70px;top:1095px;font-size:17px;letter-spacing:2px">Vida media de la cafeína: unas 5 h (EFSA) · Cafeína antes de entrenar: ISSN</div>'
         + linea(4))
    return P.page(W, H, b, 'rgba(60,90,170,.14)')


FEED_PAGES = lambda: [
    ('1_portada', f_portada()),
    ('2_4pm_come_liviano', f_paso(2, 0, 'Antes de salir', 'Come algo', '<span class="o">liviano.</span>',
                                  'Una comida chica 1 a 2 horas antes. Ni con el estómago vacío ni recién almorzado.',
                                  f'<img class="prod" src="{P.I("p_barra.png")}" style="left:640px;top:640px;width:420px;transform:rotate(-24deg)">',
                                  'rgba(200,150,60,.10)',
                                  '<div class="foot" style="left:640px;top:1000px;width:400px;font-size:18px;letter-spacing:3px">¿Sin tiempo? Una barra al paso</div>')),
    ('3_515pm_el_shot', f_paso(3, 1, '45 min antes', 'El shot.', '<span class="o">Si lo toleras.</span>',
                               '200 mg de cafeína, sabor pera. Rinde mejor entre 30 y 60 minutos antes. Si ya tomaste café hoy, sáltatelo.',
                               P.heroe('p_guarana.png', 830, 1040, 600, 4), 'rgba(200,170,40,.12)', nota(1100))),
    ('4_6pm_a_entrenar', f_paso(4, 2, 'Hora de la verdad', 'A entrenar.', '<span class="o">Agua a mano.</span>',
                                'El shot te da energía; las series las pones tú. Llega hidratado y toma agua entre series.',
                                '<div class="h" style="position:absolute;right:60px;top:430px;font-size:300px;color:transparent;-webkit-text-stroke:2px rgba(242,106,27,.35);line-height:.8;text-align:right">60<br>min</div>',
                                'rgba(242,106,27,.10)')),
    ('5_730pm_batido', f_paso(5, 3, 'Al llegar a casa', 'Batido', '<span class="o">+ creatina.</span>',
                              'Un scoop si no llegas a tu proteína con la comida. La creatina, 5 g, a cualquier hora y todos los días.',
                              P.heroe('p_whey.png', 760, 1040, 470) + P.heroe('p_usn_crea.png', 960, 1040, 330),
                              'rgba(60,110,170,.12)',
                              '<div class="foot" style="left:70px;top:1100px;font-size:20px;letter-spacing:4px;color:#f4f1ec">Proteína + creatina <span class="o">·</span> Shaker C4 de regalo</div>')),
    ('6_10pm_a_dormir', f_cierre()),
]


# ---------------- HISTORIAS ----------------
TOP = '<div class="foot" style="right:70px;top:162px;color:#F26A1B">Viernes de combo</div>'


def fila(a, b_):
    return (f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:30px 0;border-top:1px solid rgba(244,241,236,.14)">'
            f'<div class="h" style="font-size:78px">{a}</div><div style="font-size:32px;color:#bdb8b0;font-weight:500;text-align:right;width:440px">{b_}</div></div>')


def h_receta():
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:80px;right:80px;top:320px"><div class="lab">La receta del combo</div>'
           '<div class="h" style="font-size:170px;margin-top:20px">Ingredientes</div>'
           '<div style="margin-top:40px">'
           + fila('1 proteína', 'Whey USN, ISO 100 o Nitro Tech') + fila('1 creatina', 'La que quieras, con o sin sabor')
           + '<div style="border-top:1px solid rgba(244,241,236,.14)"></div></div></div>'
         + P.heroe('p_whey.png', 330, 1600, 460) + P.heroe('p_finaflex.png', 790, 1600, 380)
         + '<div class="h o" style="position:absolute;left:565px;top:1330px;font-size:130px;transform:translateX(-50%)">+</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.12)')


def h_resultado():
    b = (P.marca(70, 150) + TOP + P.heroe('p_shaker.png', 540, 1580, 760, -4)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">Resultado</div>'
           '<div class="h" style="font-size:190px;margin-top:20px">Shaker C4</div><div class="h o" style="font-size:190px">de regalo.</div></div>'
         + '<div style="position:absolute;left:0;right:0;top:1640px;text-align:center;font-weight:600;font-size:26px;letter-spacing:5px;text-transform:uppercase">'
           'Pídelo por DM <span class="o">·</span> Delivery en Caldera $1.500</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.14)')


def h_encuesta():
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">Responde</div>'
           '<div class="h" style="font-size:190px;margin-top:20px">¿Ya tienes</div><div class="h o" style="font-size:190px">shaker?</div></div>'
         # espacio libre ~300 px (y 820-1150) para el sticker de encuesta
         + P.heroe('p_shaker.png', 300, 1590, 380, -6) + P.heroe('p_whey.png', 560, 1590, 330) + P.heroe('p_usn_crea.png', 780, 1590, 250)
         + '<div style="position:absolute;left:0;right:0;top:1615px;text-align:center;font-weight:600;font-size:24px;letter-spacing:5px;text-transform:uppercase;color:#d6d1c9">'
           'Si te falta, va gratis en tu combo</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.10)')


if __name__ == '__main__':
    P.render(FEED_PAGES(), FEED, W, H)
    P.render([('1_receta_ingredientes', h_receta()), ('2_resultado_shaker', h_resultado()),
              ('3_encuesta_shaker', h_encuesta())], HIST, SW, SH)
