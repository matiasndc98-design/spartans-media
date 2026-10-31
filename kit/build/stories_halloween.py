"""Sábado 31 oct · "Esto o esto" de Halloween (estilo premium, semana de la energía, paquete liviano: 3 historias).
Idea nueva: CONTENIDO DE FECHA DEL DÍA (Halloween) con humor de gym identificable: "¿Qué da más miedo?" → lo que sí
debería asustarte (cafeína tarde) → encuesta final "¿Truco o entreno?". Espacio libre ~300 px para el sticker en 1 y 3.
Uso (desde kit/build): python3 stories_halloween.py <carpeta_salida>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
sys.argv = [sys.argv[0]]
import premium as P

W, H = P.SW, P.SH
TOP = '<div class="foot" style="right:70px;top:162px;color:#F26A1B">31 de octubre</div>'
NOTA = ('<div class="foot" style="left:80px;right:80px;bottom:270px;font-size:18px;letter-spacing:2px;line-height:1.5">'
        'Guaraná Shot: contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.</div>')


def miedo():
    # espacio libre 1150-1480 para el sticker de encuesta
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Halloween en el gym</div>'
           '<div class="h" style="font-size:150px;margin-top:22px">¿Qué da</div><div class="h o" style="font-size:150px">más miedo?</div></div>'
         + '<div style="position:absolute;left:70px;right:70px;top:760px;display:flex;align-items:center;justify-content:space-between">'
           '<div class="h" style="width:420px;text-align:center;font-size:96px">Día de<br>piernas</div>'
           '<div class="h o" style="font-size:70px">o</div>'
           '<div class="h" style="width:420px;text-align:center;font-size:96px">El shaker<br>de ayer<br>sin lavar</div></div>'
         + '<div class="rule" style="position:absolute;left:500px;top:1110px"></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:300px">Vota sin miedo</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.10)')


def cafeina_tarde():
    b = (P.marca(70, 150) + TOP + P.heroe('p_guarana.png', 800, 1560, 600, 4)
         + '<div style="position:absolute;left:80px;width:600px;top:330px"><div class="lab">Lo que sí da miedo</div>'
           '<div class="h" style="font-size:140px;margin-top:22px">Cafeína</div><div class="h" style="font-size:140px">tarde,</div>'
           '<div class="h o" style="font-size:140px">sueño corto.</div>'
           '<div class="rule" style="margin:40px 0 26px"></div>'
           '<div style="font-size:40px;line-height:1.28;font-weight:500;color:#e8e4dd">Tómala 30 a 60 min antes de entrenar. Y mientras más lejos de la hora de dormir, mejor.</div></div>'
         + '<div class="foot" style="left:80px;bottom:330px;font-size:18px;letter-spacing:3px">Momento sugerido: ISSN</div>'
         + NOTA)
    return P.page(W, H, b, 'rgba(200,150,40,.12)')


def truco():
    # espacio libre 1130-1460 para el sticker de encuesta
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:80px;right:80px;top:360px"><div class="lab">Hoy es sábado 31</div>'
           '<div class="h" style="font-size:190px;margin-top:22px">¿Truco</div><div class="h o" style="font-size:190px">o entreno?</div>'
           '<div style="font-size:40px;color:#bdb8b0;margin-top:34px;font-weight:500;width:820px">Halloween o no, la constancia no se disfraza. ¿Vas hoy?</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:300px">Pide lo tuyo por DM</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.10)')


if __name__ == '__main__':
    P.render([('1_que_da_miedo', miedo()), ('2_cafeina_tarde', cafeina_tarde()), ('3_truco_o_entreno', truco())], OUT, W, H)
