"""Sábado 28 nov 2026 · foto de feed automática (Metricool 10 AM) + historias "esto o esto" (estilo SOBRIO).
Idea nueva: PRODUCTO FLOTANDO / LEVITACIÓN (tendencia 2026 de foto de producto "floating product": el envase
suspendido en el aire, inclinado, con su sombra suave en el piso bastante más abajo; sensación de liviano, "al paso").
Feed 4:5: Barra Space Protein XXL 80 g coco "Proteína. Al paso." (36% proteína).
Historias 9:16: 1 "Sábado. Bolso listo." (shaker C4 + barra, recorte por el borde) · 2 encuesta "¿Barra o batido?"
(barra vs Whey USN, espacio libre ~720–1060 para el sticker). Sin precios, sin numeración.
Uso (desde kit/build): python3 sabado_flota.py <feed_dir> <hist_dir>
"""
import sys
FEED_OUT = sys.argv[1] if len(sys.argv) > 1 else 'feed'
HIST_OUT = sys.argv[2] if len(sys.argv) > 2 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P

OR = P.OR


def flotando(img, cx, cy, width, rot, piso_y, sombra_w):
    """Producto suspendido (centro cx,cy) y su sombra difusa en el piso, más abajo."""
    return (f'<div style="position:absolute;left:{cx - sombra_w // 2}px;top:{piso_y - 30}px;width:{sombra_w}px;height:60px;'
            'border-radius:50%;background:radial-gradient(closest-side,rgba(0,0,0,.85),rgba(0,0,0,.35) 60%,transparent);filter:blur(14px)"></div>'
            f'<div style="position:absolute;left:{cx - sombra_w // 2 + 60}px;top:{piso_y - 12}px;width:{sombra_w - 120}px;height:24px;'
            'border-radius:50%;background:rgba(0,0,0,.7);filter:blur(8px)"></div>'
            f'<img src="{P.I(img)}" style="position:absolute;left:{cx}px;top:{cy}px;width:{width}px;'
            f'transform:translate(-50%,-50%) rotate({rot}deg);filter:drop-shadow(0 50px 40px rgba(0,0,0,.6))">')


def feed():
    W, H = 1080, 1350
    b = (P.marca(70, 64) + '<div class="foot" style="right:70px;top:74px">Sábado</div>'
         + '<div style="position:absolute;left:0;right:0;top:150px;text-align:center">'
           '<div class="h" style="font-size:200px">Proteína.</div>'
           f'<div class="h o" style="font-size:200px">Al paso.</div></div>'
         + flotando('p_barra.png', 540, 790, 900, -13, 1130, 640)
         + '<div style="position:absolute;left:70px;right:70px;bottom:70px;text-align:center">'
           '<div class="lab" style="color:#d8d3cb">Barra Space Protein XXL · 80 g · Coco</div>'
           f'<div style="width:80px;height:2px;background:{OR};margin:24px auto 22px"></div>'
           '<div style="font-weight:600;font-size:26px;letter-spacing:5px;text-transform:uppercase;color:#c9c4bd">36% proteína</div></div>')
    return P.page(W, H, b, 'rgba(242,106,27,.09)')


def h_bolso():
    SW, SH = 1080, 1920
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:160px">Sábado</div>'
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center">'
           '<div class="h" style="font-size:190px">Sábado.</div>'
           '<div class="h o" style="font-size:190px">Bolso listo.</div></div>'
         + P.heroe('p_shaker.png', 330, 1420, 680, -4)
         + flotando('p_barra.png', 790, 1080, 600, -18, 1420, 400)
         + '<div style="position:absolute;left:0;right:0;bottom:262px;text-align:center">'
           '<div class="lab" style="color:#d8d3cb">Shaker C4 · Barra Space Protein XXL</div>'
           f'<div style="width:80px;height:2px;background:{OR};margin:24px auto"></div>'
           '<div style="font-weight:600;font-size:26px;letter-spacing:5px;text-transform:uppercase;color:#c9c4bd">Pídelo por DM</div></div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.09)')


def h_encuesta():
    SW, SH = 1080, 1920
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:160px">Esto o esto</div>'
         + '<div style="position:absolute;left:0;right:0;top:300px;text-align:center"><div class="lab">Después de entrenar</div>'
           '<div class="h" style="font-size:180px;margin-top:22px">¿Barra</div><div class="h o" style="font-size:180px">o batido?</div></div>'
         + flotando('p_barra.png', 300, 1260, 480, -16, 1450, 340)
         + P.heroe('p_whey.png', 790, 1450, 470)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Barra Space Protein XXL · Whey USN chocolate</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.08)')


if __name__ == '__main__':
    P.render([('1_proteina_al_paso', feed())], FEED_OUT, 1080, 1350)
    P.render([('1_bolso_listo', h_bolso()), ('2_barra_o_batido', h_encuesta())], HIST_OUT, 1080, 1920)
