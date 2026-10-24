"""Historias 9:16 (estilo premium) · sábado 24 oct, cierre de la semana de la proteína: "esto o esto" del batido.
Idea nueva: cerrar con el sticker "Agrega el tuyo" (Add Yours) para que los seguidores suban su propio batido
(contenido real de clientes, cadena que se comparte). Pantallas interactivas con ~300 px libres para el sticker.
Uso (desde kit/build): python3 stories_sabado_batido.py <carpeta_salida>
"""
import sys
import premium as P

OUT = sys.argv[1] if len(sys.argv) > 1 else 'hist'
SW, SH = P.SW, P.SH
OR = P.OR
ZONA = '<div style="position:absolute;left:0;right:0;top:{y}px;text-align:center" class="foot">{t}</div>'


def h1():  # encuesta: agua o leche (sticker en 720–1050)
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:160px;color:#F26A1B">Esto o esto</div>'
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Tu batido de proteína</div>'
           '<div class="h" style="font-size:170px;margin-top:22px">¿Con agua</div><div class="h o" style="font-size:170px">o con leche?</div></div>'
         + P.heroe('p_shaker.png', 330, 1630, 470, -6) + P.heroe('p_whey.png', 700, 1640, 560))
    return P.page(SW, SH, b, 'rgba(242,106,27,.10)')


def h2():  # respuesta
    b = (P.marca(70, 150) + P.heroe('p_whey.png', 790, 1640, 560)
         + '<div style="position:absolute;left:80px;top:360px"><div class="lab">La respuesta</div>'
           '<div class="h" style="font-size:200px;margin-top:14px">Las dos</div><div class="h o" style="font-size:200px">sirven.</div></div>'
         + '<div style="position:absolute;left:80px;width:560px;top:880px"><div class="rule" style="margin-bottom:30px"></div>'
           '<div class="lab" style="color:#f4f1ec">Con agua</div>'
           '<div style="font-size:42px;line-height:1.25;font-weight:500;color:#cfcac2;margin:8px 0 30px">Más liviano y fácil de llevar.</div>'
           '<div class="lab" style="color:#f4f1ec">Con leche</div>'
           '<div style="font-size:42px;line-height:1.25;font-weight:500;color:#cfcac2;margin-top:8px">Más cremoso y suma unos 8 g de proteína por vaso.</div>'
           '<div class="foot" style="position:static;margin-top:40px;font-size:18px;letter-spacing:3px">Leche: valor aproximado, USDA</div></div>')
    return P.page(SW, SH, b, 'rgba(40,80,200,.12)')


def h3():  # encuesta: batido o barra (sticker en 720–1050)
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:160px;color:#F26A1B">Esto o esto</div>'
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Después de entrenar</div>'
           '<div class="h" style="font-size:170px;margin-top:22px">¿Batido</div><div class="h o" style="font-size:170px">o barra?</div></div>'
         + P.heroe('p_whey.png', 290, 1640, 520)
         + f'<img class="prod" src="{P.I("p_barra.png")}" style="left:520px;top:1330px;width:500px;transform:rotate(-16deg)">'
         + '<div class="lab" style="position:absolute;left:150px;width:280px;text-align:center;top:1665px">Whey USN</div>'
         + '<div class="lab" style="position:absolute;left:600px;width:360px;text-align:center;top:1665px">Barra XXL coco</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.10)')


def h4():  # "Agrega el tuyo" (sticker en 1000–1330)
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:160px">Semana de la proteína</div>'
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab o" style="color:#F26A1B">Agrega el tuyo</div>'
           '<div class="h" style="font-size:200px;margin-top:22px">Muestra</div><div class="h o" style="font-size:200px">tu batido.</div>'
           '<div style="font-size:40px;line-height:1.3;font-weight:500;color:#cfcac2;margin:36px auto 0;width:820px">Saca una foto a tu shaker de hoy y súbela con el sticker de aquí abajo.</div></div>'
         + P.heroe('p_shaker.png', 540, 1660, 300))
    return P.page(SW, SH, b, 'rgba(242,106,27,.12)')


if __name__ == '__main__':
    P.render([('1_agua_o_leche', h1()), ('2_las_dos_sirven', h2()), ('3_batido_o_barra', h3()), ('4_agrega_el_tuyo', h4())], OUT, SW, SH)
