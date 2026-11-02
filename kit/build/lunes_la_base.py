"""Lunes 2 nov 2026 · semana "base y constancia" · estilo SOBRIO (dirección del dueño del 1 nov).
Carrusel 4:5 "La base. No se negocia." con idea nueva RECORTE EDITORIAL (producto gigante cortado por el borde,
como las campañas de marcas grandes) + historias 9:16 con la foto real del dueño (Finaflex en la mano).
Uso (desde kit/build): python3 lunes_la_base.py <carpeta_feed> <carpeta_historias>
"""
import sys, os
FEED = sys.argv[1] if len(sys.argv) > 1 else 'feed'
HIST = sys.argv[2] if len(sys.argv) > 2 else 'hist'
sys.argv = [sys.argv[0]]
import premium as P
import gen

W, H = 1080, 1350
SW, SH = P.SW, P.SH
OR = P.OR


def num(n):
    return f'<div class="foot" style="right:70px;top:74px">{n:02d} / 06</div>'


def portada():
    row = (P.heroe('p_omega.png', 215, 1130, 330) + P.heroe('p_finaflex.png', 425, 1150, 430)
           + P.heroe('p_whey.png', 690, 1160, 500) + P.heroe('p_multi.png', 905, 1130, 330))
    b = (P.marca(70, 64) + num(1) + row
         + '<div style="position:absolute;left:70px;top:190px"><div class="lab">Semana de la constancia</div>'
           '<div class="h" style="font-size:200px;margin-top:18px">La base.</div><div class="h o" style="font-size:130px">No se negocia.</div></div>'
         + '<div class="foot" style="left:70px;bottom:60px">Desliza</div><div class="rule" style="position:absolute;left:200px;bottom:72px;width:120px"></div>')
    return P.page(W, H, b, 'rgba(242,106,27,.10)')


def recorte(n, img, lab, t1, t2, dato, glow, left=560, top=170, alto=1450, rot=-8):
    """Producto gigante que se sale del cuadro por la derecha y abajo."""
    prod = (f'<img class="prod" src="{P.I(img)}" style="left:{left}px;top:{top}px;height:{alto}px;transform:rotate({rot}deg)">')
    sombra = ('<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,8,8,.95) 0%,rgba(8,8,8,.8) 42%,'
              'rgba(8,8,8,0) 72%)"></div>')
    b = (prod + sombra + P.marca(70, 64) + num(n)
         + f'<div style="position:absolute;left:70px;bottom:150px;width:560px"><div class="lab">{lab}</div>'
           f'<div class="h" style="font-size:170px;margin-top:20px">{t1}</div><div class="h o" style="font-size:120px">{t2}</div>'
           f'<div class="rule" style="margin-top:34px"></div></div>'
         + f'<div class="foot" style="left:70px;bottom:70px">{dato}</div>')
    return P.page(W, H, b, glow)


def cierre():
    b = (P.marca(70, 64) + num(6)
         + P.heroe('p_finaflex.png', 330, 1080, 470) + P.heroe('p_whey.png', 600, 1100, 540) + P.heroe('p_shaker.png', 850, 1080, 400)
         + '<div style="position:absolute;left:0;right:0;top:170px;text-align:center"><div class="lab">Spartans</div>'
           '<div class="h" style="font-size:150px;margin-top:16px">Lo básico.</div><div class="h o" style="font-size:150px">Todos los días.</div></div>'
         + '<div style="position:absolute;left:0;right:0;bottom:70px;text-align:center;font-weight:600;font-size:26px;letter-spacing:6px;text-transform:uppercase">'
           'Pídelo por DM <span class="o">·</span> Proteína + creatina: shaker de regalo</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.10)')


FOTO = gen.uri(os.path.join(gen.B, '..', 'fotos_dueno', 'finaflex_mano.jpg'))


def h_foto():
    b = (f'<img src="{FOTO}" style="position:absolute;inset:0;width:{SW}px;height:{SH}px;object-fit:cover">'
         '<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,8,8,.9) 0%,rgba(8,8,8,.55) 20%,rgba(8,8,8,0) 34%,'
         'rgba(8,8,8,0) 66%,rgba(8,8,8,.8) 80%,rgba(8,8,8,.95) 100%)"></div>'
         + P.marca(70, 150)
         + '<div style="position:absolute;left:70px;top:260px"><div class="lab" style="color:#cfc9c0">Esta semana</div>'
           '<div class="h" style="font-size:170px;margin-top:18px">Constancia.</div></div>'
         + '<div style="position:absolute;left:70px;right:70px;bottom:290px"><div class="rule" style="margin-bottom:26px"></div>'
           '<div class="h" style="font-size:90px">200 porciones.</div><div class="h o" style="font-size:90px">Cero excusas.</div>'
           '<div class="foot" style="position:static;margin-top:22px;color:#bdb8b0">Creatina Finaflex 1 kg · Pídela por DM</div></div>')
    return P.page(SW, SH, b)


def h_promo():
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Promoción vigente</div>'
           '<div class="h" style="font-size:150px;margin-top:26px">Proteína + creatina.</div><div class="h o" style="font-size:150px">Shaker de regalo.</div></div>'
         + P.heroe('p_whey.png', 330, 1440, 560) + P.heroe('p_shaker.png', 580, 1440, 470) + P.heroe('p_usn_crea.png', 800, 1440, 380)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:280px">Pídelo por DM · Delivery en Caldera $1.500</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.10)')


def h_encuesta():
    # sticker en 760–1080 (libre)
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:340px;text-align:center"><div class="lab">Noviembre</div>'
           '<div class="h" style="font-size:150px;margin-top:26px">¿Cuántos días</div><div class="h o" style="font-size:150px">entrenas?</div></div>'
         + P.heroe('p_finaflex.png', 540, 1560, 400)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:280px">Lo básico. Todos los días.</div>')
    return P.page(SW, SH, b, 'rgba(60,110,170,.10)')


if __name__ == '__main__':
    P.render([
        ('1_la_base', portada()),
        ('2_creatina', recorte(2, 'p_finaflex.png', 'Creatina · Finaflex 1 kg', '5 g.', 'Todos los días.', '200 porciones · Micronizada', 'rgba(242,106,27,.12)')),
        ('3_proteina', recorte(3, 'p_whey.png', 'Proteína · Whey USN 5 lb', '22 g.', 'Por scoop.', 'Premium Whey+ · Chocolate', 'rgba(140,70,30,.16)', left=520, top=170, alto=1450)),
        ('4_omega3', recorte(4, 'p_omega.png', 'Omega 3 · USN Fish Oil', 'Omega 3.', 'Sin pausa.', '1000 mg · 90 cápsulas blandas', 'rgba(60,110,170,.14)')),
        ('5_multivitaminico', recorte(5, 'p_multi.png', 'Multivitamínico · USN', 'Un mes.', '30 porciones.', 'Super Daily Formula · 60 tabletas', 'rgba(242,106,27,.10)')),
        ('6_pidelo', cierre()),
    ], FEED, W, H)
    P.render([('1_constancia', h_foto()), ('2_shaker_de_regalo', h_promo()), ('3_cuantos_dias', h_encuesta())], HIST, SW, SH)
