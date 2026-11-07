"""Historias 9:16 (estilo SOBRIO) · sábado 7 nov 2026: "esto o esto" de la creatina + encuesta del día.
1: "¿Uva o sin sabor?" MuscleTech Platinum Grape Freeze vs sin sabor (encuesta en el espacio libre 700–1060).
2: "¿Hoy entrenas?" con la barra Space Protein XXL (encuesta en el espacio libre 700–1060).
Sin precios, sin numeración. Uso (desde kit/build): python3 stories_sabado_uva.py <carpeta>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

SW, SH = 1080, 1920


def h_uva():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">Esto o esto</div>'
           '<div class="h o" style="font-size:180px;margin-top:26px">¿Uva</div><div class="h" style="font-size:150px">o sin sabor?</div></div>'
         + P.heroe('p_mt_uva.png', 300, 1600, 470) + P.heroe('p_mt_sin.png', 790, 1600, 450)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">MuscleTech Platinum · 5 g al día</div>')
    return P.page(SW, SH, b, 'rgba(120,60,170,.12)')


def h_hoy():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">Sábado</div>'
           '<div class="h" style="font-size:190px;margin-top:26px">¿Hoy</div><div class="h o" style="font-size:190px">entrenas?</div></div>'
         + f'<img class="prod" src="{P.I("p_barra.png")}" style="left:540px;top:1560px;width:820px;transform:translate(-50%,-100%) rotate(-6deg)">'
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Space Protein XXL · 36% proteína · al paso</div>')
    return P.page(SW, SH, b, 'rgba(120,170,220,.12)')


if __name__ == '__main__':
    P.render([('1_uva_o_sin_sabor', h_uva()), ('2_hoy_entrenas', h_hoy())], OUT, SW, SH)
