"""Viernes 13 nov 2026 · cierre de la semana de la creatina (2ª vuelta) · estilo SOBRIO.
Carrusel 4:5 "Arma tu combo." con idea nueva MENÚ CON CÓDIGOS (como los "build your bundle" de las marcas DTC:
paso 1 proteína con número, paso 2 creatina con letra, paso 3 shaker de regalo; la respuesta es un código de 2
caracteres, "1D", el llamado de menor esfuerzo posible) + 2 historias: foto real del dueño con el Finaflex y caja
de preguntas "Arma tu combo".
Uso (desde kit/build): python3 viernes_arma_combo.py <carpeta_feed> <carpeta_historias>
"""
import sys, os
FEED = sys.argv[1] if len(sys.argv) > 1 else 'feed'
HIST = sys.argv[2] if len(sys.argv) > 2 else 'hist'
sys.argv = [sys.argv[0]]
import gen
import premium as P

W, H = 1080, 1350
SW, SH = P.SW, P.SH
FOTO = gen.uri(os.path.join(gen.B, '..', 'fotos_dueno', 'finaflex_mano.jpg'))


def num(n):
    return f'<div class="foot" style="right:70px;top:74px">{n:02d} / 06</div>'


def titulo(lab, t1, t2, top=170, fs=120):
    return (f'<div style="position:absolute;left:0;right:0;top:{top}px;text-align:center"><div class="lab">{lab}</div>'
            f'<div class="h" style="font-size:{fs}px;margin-top:16px">{t1}</div><div class="h o" style="font-size:{fs}px">{t2}</div></div>')


def portada():
    b = (P.marca(70, 64) + num(1)
         + P.heroe('p_whey.png', 300, 1170, 560) + P.heroe('p_finaflex.png', 790, 1170, 470) + P.heroe('p_shaker.png', 555, 1190, 430)
         + '<div style="position:absolute;left:70px;top:180px"><div class="lab">Proteína + creatina</div>'
           '<div class="h" style="font-size:200px;margin-top:18px">Arma tu</div><div class="h o" style="font-size:200px">combo.</div></div>'
         + '<div class="foot" style="left:70px;bottom:60px">Desliza</div><div class="rule" style="position:absolute;left:200px;bottom:72px;width:120px"></div>')
    return P.page(W, H, b, 'rgba(242,106,27,.10)')


def paso(n, lab, t1, t2, cols, base, glow):
    prods = ''.join(P.heroe(img, cx, base, h) for img, cx, h, _, _, _ in cols)
    datos = ''.join(
        f'<div style="position:absolute;left:{cx - 130}px;width:260px;top:{base + 100}px;text-align:center">'
        f'<div class="h o" style="font-size:130px">{cod}</div>'
        f'<div class="h" style="font-size:48px;margin-top:10px">{dato}</div>'
        f'<div class="foot" style="position:static;margin-top:10px;color:#bdb8b0;font-size:19px;letter-spacing:3px">{nom}</div></div>'
        for _, cx, _, cod, dato, nom in cols)
    linea = f'<div style="position:absolute;left:90px;right:90px;top:{base + 70}px;height:1px;background:rgba(244,241,236,.18)"></div>'
    b = P.marca(70, 64) + num(n) + titulo(lab, t1, t2) + prods + linea + datos
    return P.page(W, H, b, glow)


def proteinas():
    cols = [('p_whey.png', 210, 380, '1', '22 g', 'Whey USN 5 lb'),
            ('p_iso100.png', 540, 430, '2', '25 g', 'ISO 100 5 lb'),
            ('p_nitro.png', 870, 380, '3', '30 g', 'Nitro Tech 4 lb')]
    return paso(2, 'Paso 1', 'Elige tu', 'proteína.', cols, 860, 'rgba(60,110,170,.10)')


def creatinas():
    cols = [('p_usn_crea.png', 160, 270, 'A', '60 días', 'USN 300 g'),
            ('p_mt_sin.png', 413, 300, 'B', '80 días', 'Platinum 400 g'),
            ('p_mt_uva.png', 666, 300, 'C', '60 días', 'Platinum uva'),
            ('p_finaflex.png', 920, 330, 'D', '200 días', 'Finaflex 1 kg')]
    return paso(3, 'Paso 2', 'Elige tu', 'creatina.', cols, 860, 'rgba(242,106,27,.08)')


def regalo():
    b = (P.marca(70, 64) + num(4) + titulo('Paso 3', 'El shaker', 'va de regalo.', fs=130)
         + P.heroe('p_shaker.png', 540, 1170, 640)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:70px">Shaker C4 · Por compra de proteína + creatina</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.12)')


def ejemplo():
    b = (P.marca(70, 64) + num(5)
         + '<div style="position:absolute;left:0;right:0;top:160px;text-align:center"><div class="lab">Por ejemplo</div>'
           '<div class="h" style="font-size:300px;margin-top:6px">1<span class="o">D</span>.</div></div>'
         + P.heroe('p_whey.png', 300, 1150, 500) + P.heroe('p_shaker.png', 560, 1165, 420) + P.heroe('p_finaflex.png', 800, 1150, 420)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:70px">Whey USN <span class="o">+</span> Finaflex 1 kg <span class="o">+</span> Shaker de regalo</div>')
    return P.page(W, H, b, 'rgba(140,70,30,.12)')


def cierre():
    b = (P.marca(70, 64) + num(6)
         + '<div style="position:absolute;left:0;right:0;top:300px;text-align:center"><div class="lab">Spartans</div>'
           '<div class="h" style="font-size:170px;margin-top:20px">¿Cuál es</div><div class="h o" style="font-size:170px">el tuyo?</div>'
           '<div style="font-size:38px;color:#bdb8b0;margin-top:40px;font-weight:500;letter-spacing:1px">Responde con número y letra.</div></div>'
         + '<div class="rule" style="position:absolute;left:500px;top:900px"></div>'
         + '<div style="position:absolute;left:0;right:0;top:960px;text-align:center;font-weight:600;font-size:26px;letter-spacing:6px;'
           'text-transform:uppercase;line-height:2">Pídelo por DM<br><span style="color:#8d8880">Delivery en Caldera $1.500 · Envíos a todo Chile</span></div>')
    return P.page(W, H, b, 'rgba(242,106,27,.08)')


def h_foto():
    b = (f'<img src="{FOTO}" style="position:absolute;inset:0;width:{SW}px;height:{SH}px;object-fit:cover">'
         '<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,8,8,.9) 0%,rgba(8,8,8,.55) 20%,rgba(8,8,8,0) 34%,'
         'rgba(8,8,8,0) 62%,rgba(8,8,8,.85) 78%,rgba(8,8,8,.95) 100%)"></div>'
         + P.marca(70, 150)
         + '<div style="position:absolute;left:70px;top:260px"><div class="lab" style="color:#cfc9c0">Viernes</div>'
           '<div class="h" style="font-size:170px;margin-top:18px">Tu creatina.</div></div>'
         + '<div style="position:absolute;left:70px;right:70px;bottom:290px"><div class="rule" style="margin-bottom:26px"></div>'
           '<div class="h" style="font-size:90px">+ Tu proteína.</div><div class="h o" style="font-size:90px">Shaker de regalo.</div>'
           '<div class="foot" style="position:static;margin-top:22px;color:#bdb8b0">Pídelo por DM · Delivery en Caldera $1.500</div></div>')
    return P.page(SW, SH, b)


def h_pregunta():
    # caja de preguntas en 720–1080 (libre)
    fila = lambda items: ''.join(
        f'<span style="margin:0 18px"><span class="o">{c}</span> <span style="color:#bdb8b0">{t}</span></span>' for c, t in items)
    b = (P.marca(70, 150)
         + '<div style="position:absolute;left:0;right:0;top:330px;text-align:center"><div class="lab">Proteína + creatina</div>'
           '<div class="h" style="font-size:170px;margin-top:26px">Arma tu</div><div class="h o" style="font-size:170px">combo.</div></div>'
         + '<div style="position:absolute;left:40px;right:40px;top:1160px;text-align:center;font-family:Bebas;font-size:50px;letter-spacing:1px;line-height:1.5">'
         + fila([('1', 'Whey USN'), ('2', 'ISO 100'), ('3', 'Nitro Tech')]) + '<br>'
         + fila([('A', 'USN'), ('B', 'Platinum'), ('C', 'Uva'), ('D', 'Finaflex')]) + '</div>'
         + P.heroe('p_shaker.png', 540, 1630, 260)
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:262px">Escribe tu código · Shaker de regalo</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.10)')


if __name__ == '__main__':
    P.render([('1_arma_tu_combo', portada()), ('2_proteina', proteinas()), ('3_creatina', creatinas()),
              ('4_shaker_de_regalo', regalo()), ('5_ejemplo', ejemplo()), ('6_cual_es_el_tuyo', cierre())], FEED, W, H)
    P.render([('1_tu_creatina', h_foto()), ('2_arma_tu_combo', h_pregunta())], HIST, SW, SH)
