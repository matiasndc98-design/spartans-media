"""Martes 27 oct · "Pregunta espartana" (estilo premium, semana de la energía): ¿la cafeína te deshidrata?
Paquete liviano (ajuste del 26 oct): 3 historias, la primera con quiz y la última con caja de preguntas (espacio ~300 px).
Respaldo: Maughan y Griffin 2003 (revisión: la cafeína en dosis habituales no deshidrata); Killer et al. 2014
(café a 4 mg/kg hidrata igual que el agua en bebedores habituales).
Uso (desde kit/build): python3 stories_pregunta_cafeina.py <carpeta_salida>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
sys.argv = [sys.argv[0]]
import premium as P

OR = P.OR
W, H = P.SW, P.SH
TOP = '<div class="foot" style="right:70px;top:162px;color:#F26A1B">Pregunta espartana</div>'
GUA = 'Guaraná Shot: contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.'


def quiz():
    # espacio libre 1150-1500 para el sticker de quiz
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:80px;right:80px;top:380px"><div class="lab">Responde</div>'
           '<div class="h" style="font-size:190px;margin-top:24px">¿La cafeína</div><div class="h o" style="font-size:190px">te deshidrata?</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:300px">La respuesta en la siguiente</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.08)')


def respuesta():
    b = (P.marca(70, 150) + TOP + P.heroe('p_guarana.png', 800, 1540, 620, 4)
         + '<div style="position:absolute;left:80px;top:360px;width:640px"><div class="lab">La respuesta</div>'
           '<div class="h" style="font-size:150px;margin-top:22px">En dosis</div><div class="h" style="font-size:150px">normales,</div>'
           '<div class="h o" style="font-size:260px">no.</div></div>'
         + '<div style="position:absolute;left:80px;width:520px;top:1010px"><div class="rule" style="margin-bottom:26px"></div>'
           '<div style="font-size:40px;line-height:1.28;font-weight:500;color:#e8e4dd">Un café o un shot no te secan. El agua igual va: llega hidratado al gym.</div>'
           '<div class="foot" style="position:static;margin-top:30px;font-size:17px;letter-spacing:2px">Maughan y Griffin, 2003 · Killer et al., 2014</div></div>'
         + f'<div class="foot" style="left:80px;right:80px;bottom:270px;font-size:18px;letter-spacing:2px;line-height:1.5">{GUA}</div>')
    return P.page(W, H, b, 'rgba(120,170,90,.12)')


def caja():
    # espacio libre 1100-1450 para la caja de preguntas
    b = (P.marca(70, 150) + TOP
         + '<div style="position:absolute;left:80px;right:80px;top:380px;text-align:center"><div class="lab">Tu turno</div>'
           '<div class="h" style="font-size:190px;margin-top:24px">¿Qué duda</div><div class="h o" style="font-size:190px">tienes?</div>'
           '<div style="font-size:40px;color:#bdb8b0;margin-top:30px;font-weight:500">La respondemos el próximo martes.</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:300px">Energía, cafeína, lo que sea</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.09)')


if __name__ == '__main__':
    P.render([('1_quiz_cafeina_deshidrata', quiz()), ('2_respuesta_dosis_normales', respuesta()), ('3_caja_de_preguntas', caja())], OUT, W, H)
