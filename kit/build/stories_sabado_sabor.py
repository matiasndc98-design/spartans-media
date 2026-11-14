"""Historias 9:16 (estilo SOBRIO) · sábado 14 nov 2026: después de entrenar + "esto o esto" del sabor.
1: "Después de entrenar." Whey USN + Creatina USN + shaker C4 (promo real: proteína + creatina, shaker de regalo).
2: "¿Chocolate o vainilla?" Whey USN chocolate vs Nitro Tech vainilla (encuesta en el espacio libre 700–1060).
Sin precios, sin numeración. Uso (desde kit/build): python3 stories_sabado_sabor.py <carpeta>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

SW, SH = 1080, 1920


def h_despues():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">Sábado</div>'
           '<div class="h" style="font-size:170px;margin-top:26px">Después</div><div class="h o" style="font-size:150px">de entrenar.</div>'
           '<div style="font-weight:500;font-size:34px;color:#c9c4bd;margin-top:34px;letter-spacing:1px">Proteína + creatina. El shaker va de regalo.</div></div>'
         + P.heroe('p_usn_crea.png', 250, 1600, 470) + P.heroe('p_whey.png', 790, 1600, 600)
         + P.heroe('p_shaker.png', 520, 1605, 620)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Pídelo por DM · Delivery en Caldera $1.500</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.12)')


def h_sabor():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">Esto o esto</div>'
           '<div class="h" style="font-size:170px;margin-top:26px">¿Chocolate</div><div class="h o" style="font-size:150px">o vainilla?</div></div>'
         + P.heroe('p_whey.png', 290, 1600, 470) + P.heroe('p_nitro.png', 800, 1600, 500)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Whey USN chocolate · Nitro Tech vainilla</div>')
    return P.page(SW, SH, b, 'rgba(150,95,50,.14)')


if __name__ == '__main__':
    P.render([('1_despues_de_entrenar', h_despues()), ('2_chocolate_o_vainilla', h_sabor())], OUT, SW, SH)
