"""Jueves 19 nov 2026 · historias "Detrás de la tienda" (estilo SOBRIO, semana de la proteína).
1 "Escribes. Respondemos." Whey USN + shaker C4: la compra es por DM y el dueño responde rápido; formas de pago reales.
2 Caja de preguntas "Pregúntanos." (las respuestas alimentan la "Pregunta espartana" del martes), espacio libre
  ~720–1080 px para el sticker. Sin precios de productos, sin numeración.
Uso (desde kit/build): python3 stories_jueves_respondemos.py <hist_dir>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

OR = P.OR
SW, SH = 1080, 1920


def h_respondemos():
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:161px">Detrás de la tienda</div>'
         + P.heroe('p_shaker.png', 300, 1560, 520) + P.heroe('p_whey.png', 680, 1560, 760)
         + '<div style="position:absolute;left:70px;top:300px"><div class="lab">Cómo se compra</div>'
           '<div class="h" style="font-size:190px;line-height:.9;margin-top:20px">Escribes.</div>'
           f'<div class="h" style="font-size:190px;line-height:.9;color:{OR}">Respondemos.</div></div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:300px;color:#d8d3cb">Pídelo por DM</div>'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">'
           'Transferencia <span class="o">·</span> Efectivo <span class="o">·</span> Tarjeta <span class="o">·</span> Mercado Pago</div>')
    return P.page(SW, SH, b, 'rgba(150,80,30,.14)')


def h_preguntas():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:300px;text-align:center"><div class="lab">Semana de la proteína</div>'
           f'<div class="h" style="font-size:220px;line-height:.92;margin-top:22px">Pregún<span style="color:{OR}">tanos.</span></div>'
           '<div style="font-size:38px;color:#c9c4bc;margin-top:24px;font-weight:500">Lo que quieras saber de la proteína.</div></div>'
         + P.heroe('p_iso100.png', 400, 1580, 420) + P.heroe('p_nitro.png', 690, 1580, 440)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Respondemos el martes</div>')
    return P.page(SW, SH, b, 'rgba(60,110,170,.12)')


if __name__ == '__main__':
    P.render([('1_escribes_respondemos', h_respondemos()), ('2_preguntanos', h_preguntas())], OUT, SW, SH)
