"""Historias 9:16 (estilo SOBRIO) · domingo 8 nov 2026: resumen y llamado al DM.
Idea nueva: RESPONDE ESTA HISTORIA (la respuesta a una historia llega directo al DM: llamado de una sola acción).
1: "Semana nueva. Misma base." Whey USN + Creatina USN + shaker C4 de regalo; "Responde esta historia".
2: "¿Qué te falta para el lunes?" con espacio libre 700–1060 para la caja de preguntas; Multivitamínico USN.
Sin precios de productos, sin numeración. Uso (desde kit/build): python3 stories_domingo_responde.py <carpeta>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

SW, SH = 1080, 1920


def h_semana():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">Domingo</div>'
           '<div class="h" style="font-size:200px;margin-top:26px">Semana <span class="o">nueva.</span></div>'
           '<div class="h" style="font-size:120px;color:#cfcac2;margin-top:18px">Misma base.</div></div>'
         + P.heroe('p_usn_crea.png', 255, 1420, 400) + P.heroe('p_whey.png', 560, 1440, 600)
         + P.heroe('p_shaker.png', 860, 1420, 400)
         + '<div style="position:absolute;left:0;right:0;bottom:290px;text-align:center">'
           '<div style="font-family:Barlow Condensed,Barlow;font-weight:600;font-size:40px;letter-spacing:3px;text-transform:uppercase;color:#f4f1ec">Responde esta historia</div>'
           '<div class="foot" style="position:static;margin-top:14px">Proteína + creatina · shaker de regalo</div></div>')
    return P.page(SW, SH, b)


def h_falta():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">Antes del lunes</div>'
           '<div class="h" style="font-size:170px;margin-top:26px">¿Qué te</div><div class="h o" style="font-size:170px">falta?</div></div>'
         + P.heroe('p_multi.png', 540, 1500, 400)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Te respondemos por DM · delivery Caldera $1.500</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.07)')


if __name__ == '__main__':
    P.render([('1_semana_nueva', h_semana()), ('2_que_te_falta', h_falta())], OUT, SW, SH)
