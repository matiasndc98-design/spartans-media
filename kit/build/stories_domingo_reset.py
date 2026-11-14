"""Historias 9:16 (estilo SOBRIO) · domingo 15 nov 2026: resumen y llamado al DM, abre la semana de la proteína.
Idea nueva: DOMINGO DE RESET (tendencia "Sunday reset": el domingo se deja lista la semana), en clave sobria.
1: "Domingo. Se prepara la semana." ISO 100 en recorte editorial gigante (25 g por scoop, 71 porciones) + DM.
2: "Esta semana: proteína." Whey USN / ISO 100 / Nitro Tech chicos en el piso; espacio libre 700–1060 para la caja de preguntas.
Sin precios, sin numeración. Uso (desde kit/build): python3 stories_domingo_reset.py <carpeta>
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

SW, SH = 1080, 1920


def h_reset():
    b = (P.marca(70, 150)
         + f'<img class="prod" src="{P.I("p_iso100.png")}" style="left:430px;top:820px;height:1150px">'
         + '<div style="position:absolute;left:70px;top:330px"><div class="lab">Domingo</div>'
           '<div class="h" style="font-size:190px;margin-top:26px">Se prepara</div><div class="h o" style="font-size:190px">la semana.</div>'
           '<div class="rule" style="margin-top:40px"></div></div>'
         + '<div style="position:absolute;left:70px;top:1000px;width:400px">'
           '<div style="font-family:Bebas;font-size:110px;line-height:.9">25 g</div>'
           '<div class="lab" style="margin-top:10px;color:#c9c4bd">Por scoop</div>'
           '<div style="font-family:Bebas;font-size:110px;line-height:.9;margin-top:50px">71</div>'
           '<div class="lab" style="margin-top:10px;color:#c9c4bd">Porciones</div></div>'
         + '<div class="foot" style="left:70px;bottom:270px;color:#f4f1ec">ISO 100 · Pídelo por DM</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.10)')


def h_semana():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:320px;text-align:center"><div class="lab">Esta semana</div>'
           '<div class="h o" style="font-size:200px;margin-top:26px">Proteína.</div>'
           '<div style="font-weight:500;font-size:34px;color:#c9c4bd;margin-top:30px;letter-spacing:1px">Pregunta lo que quieras. Te respondemos.</div></div>'
         + P.heroe('p_whey.png', 260, 1610, 420) + P.heroe('p_iso100.png', 540, 1610, 470)
         + P.heroe('p_nitro.png', 820, 1610, 430))
    return P.page(SW, SH, b, 'rgba(242,106,27,.08)')


if __name__ == '__main__':
    P.render([('1_se_prepara_la_semana', h_reset()), ('2_esta_semana_proteina', h_semana())], OUT, SW, SH)
