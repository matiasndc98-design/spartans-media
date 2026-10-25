"""Lunes 26 oct 2026 · semana de la energía, episodio 1: "Cafeína: lo que sí y lo que no" (estilo premium).
Idea nueva: RELOJ DE CAFEÍNA (línea de tiempo que muestra cuánta cafeína queda en el cuerpo horas después: 200 → 100 → 50 mg)
y CUENTA DE CAFEÍNA DEL DÍA (barra que se llena hasta 400 mg con café + shot), en formato cheat sheet para guardar.
Historias: quiz "shot a las 6 PM, ¿a qué hora queda la mitad?" → respuesta 11 PM → slider "¿con cuánta batería llegas hoy?".
Respaldo: ISSN Position Stand caffeine (Guest et al. 2021): efecto 30–60 min antes, 3–6 mg/kg; EFSA 2015: hasta 400 mg/día
en adultos sanos (no embarazadas), vida media ~5 h (rango amplio entre personas); Drake et al. 2013: cafeína 6 h antes de dormir
reduce el sueño. Taza de café ~90 mg (EFSA, aprox.).
Uso (desde kit/build): python3 lunes_cafeina.py <carpeta_feed> <carpeta_historias>
"""
import sys
import premium as P

FEED = sys.argv[1] if len(sys.argv) > 1 else 'feed'
HIST = sys.argv[2] if len(sys.argv) > 2 else 'hist'
W, H, SW, SH, OR = P.W, P.H, P.SW, P.SH, P.OR
GUA = 'Guaraná Shot: contiene cafeína (200 mg por shot). No apto para menores ni embarazadas.'
LIPO = 'Lipo 6: contiene cafeína (222 mg por cápsula). No apto para menores ni embarazadas.'


def nota(txt, bottom=58, side=70):
    return (f'<div class="foot" style="left:{side}px;right:{side}px;bottom:{bottom}px;font-size:17px;letter-spacing:2px;'
            f'line-height:1.5">{txt}</div>')


def top(n):
    return P.marca(70, 64) + f'<div class="foot" style="right:70px;top:74px">{n} / 06</div>'


def titulo(lab, a, b, top_=170, fs=130, labo=False):
    lc = f' o" style="color:{OR}' if labo else ''
    return (f'<div style="position:absolute;left:70px;right:70px;top:{top_}px"><div class="lab{lc}">{lab}</div>'
            f'<div class="h" style="font-size:{fs}px;margin-top:18px">{a}</div><div class="h o" style="font-size:{fs}px">{b}</div></div>')


def apoyo(txt, top_, w=560):
    return (f'<div style="position:absolute;left:70px;width:{w}px;top:{top_}px"><div class="rule" style="margin-bottom:26px"></div>'
            f'<div style="font-size:34px;line-height:1.3;font-weight:500;color:#bdb8b0">{txt}</div></div>')


# ---------------- CARRUSEL 4:5 ----------------
def l1():
    b = (P.marca(70, 64) + '<div class="foot" style="right:70px;top:74px">Semana de la energía · Ep. 1</div>'
         + P.heroe('p_guarana.png', 820, 1170, 640, 4)
         + '<div style="position:absolute;left:70px;top:200px"><div class="lab">Guárdalo antes de tu próximo shot</div>'
           '<div class="h" style="font-size:210px;margin-top:22px">Cafeína.</div>'
           '<div class="h o" style="font-size:110px;margin-top:10px">Lo que sí</div><div class="h" style="font-size:110px">y lo que no.</div></div>'
         + '<div class="foot" style="left:70px;top:760px">Desliza</div><div class="rule" style="position:absolute;left:200px;top:772px;width:120px"></div>'
         + nota(GUA))
    return P.page(W, H, b, 'rgba(120,170,60,.12)')


def l2():
    b = (top('02') + titulo('Lo que sí', '30 a 60 min', 'antes de entrenar.', fs=120, labo=True)
         + apoyo('Es lo que tarda en hacer efecto. Si no estás acostumbrado, parte con poco y mira cómo la toleras.', 520)
         + P.heroe('p_guarana.png', 860, 1190, 560, -3)
         + '<div class="foot" style="left:70px;bottom:58px;font-size:17px">Fuente: Sociedad Internacional de Nutrición Deportiva (ISSN)</div>')
    return P.page(W, H, b, 'rgba(242,106,27,.10)')


def l3():  # reloj de cafeína
    pts = [('6 PM', 200, 'Te tomas el shot'), ('11 PM', 100, 'Todavía la mitad'), ('4 AM', 50, 'Aún queda')]
    bars = ''
    for i, (hr, mg, t) in enumerate(pts):
        x = 70 + i * 330
        hgt = int(mg * 1.9)
        col = OR if i == 0 else ('#c95a1a' if i == 1 else '#7a3a14')
        bars += (f'<div style="position:absolute;left:{x}px;width:280px;top:{1050 - hgt}px;height:{hgt}px;background:{col};border-radius:6px 6px 0 0"></div>'
                 f'<div class="h" style="position:absolute;left:{x}px;top:{1050 - hgt - 90}px;font-size:80px">{mg} <span style="font-size:40px">mg</span></div>'
                 f'<div class="h" style="position:absolute;left:{x}px;top:1080px;font-size:64px">{hr}</div>'
                 f'<div class="lab" style="position:absolute;left:{x}px;top:1150px;font-size:19px;letter-spacing:4px">{t}</div>')
    b = (top('03') + titulo('Lo que no', 'Creer que se va', 'en una hora.', fs=120, labo=True)
         + '<div style="position:absolute;left:70px;right:70px;top:440px;font-size:32px;line-height:1.3;font-weight:500;color:#bdb8b0">'
           'Unas 5 horas después, la mitad sigue en tu cuerpo (varía mucho entre personas). Si entrenas de noche, ojo con el sueño.</div>'
         + '<div style="position:absolute;left:70px;right:70px;top:1050px;height:2px;background:rgba(244,241,236,.25)"></div>'
         + bars
         + '<div class="foot" style="left:70px;bottom:58px;font-size:17px">Referencia aproximada: vida media de unas 5 h (EFSA)</div>')
    return P.page(W, H, b, 'rgba(200,40,30,.10)')


def l4():  # cuenta de cafeína del día
    seg = [('Café', 90, '#8a6a4a'), ('Shot', 200, OR)]
    x, bar, labs = 0, '', ''
    for n, mg, c in seg:
        w = int(mg / 400 * 940)
        bar += f'<div style="position:absolute;left:{x}px;top:0;width:{w}px;height:100%;background:{c}"></div>'
        labs += (f'<div style="position:absolute;left:{70 + x}px;top:1010px;width:{w}px"><div class="h" style="font-size:56px">{mg} mg</div>'
                 f'<div class="lab" style="font-size:18px;letter-spacing:4px">{n}</div></div>')
        x += w
    b = (top('04') + titulo('Lo que no', 'Olvidar sumar', 'el café.', fs=130, labo=True)
         + apoyo('Un adulto sano puede tomar hasta 400 mg al día. Cuenta todo: café, bebidas energéticas, preentreno y shot.', 470, 900)
         + '<div style="position:absolute;left:70px;top:850px;font-family:Bebas;font-size:40px;color:#9a958e;letter-spacing:2px">TU DÍA</div>'
         + '<div style="position:absolute;right:70px;top:850px;font-family:Bebas;font-size:40px;color:#f4f1ec;letter-spacing:2px">TOPE 400 MG</div>'
         + f'<div style="position:absolute;left:70px;width:940px;top:910px;height:70px;background:rgba(244,241,236,.08);border-radius:6px;overflow:hidden">{bar}</div>'
         + labs
         + '<div class="foot" style="left:70px;bottom:58px;font-size:17px">Fuente: EFSA. Taza de café aprox. Embarazadas y menores: no.</div>')
    return P.page(W, H, b, 'rgba(140,100,60,.10)')


def l5():
    b = (top('05') + titulo('Lo que sí', 'Dormir primero.', 'Cafeína después.', fs=120, labo=True)
         + apoyo('Si dormiste 5 horas, ningún shot te salva. Sueño, comida y agua son la base; la cafeína suma encima.', 520, 900)
         + '<div class="h" style="position:absolute;left:56px;top:860px;font-size:340px;color:transparent;-webkit-text-stroke:2px rgba(244,241,236,.18)">7–9 H</div>'
         + '<div class="lab" style="position:absolute;left:70px;top:1190px">Lo que recomiendan dormir a un adulto</div>')
    return P.page(W, H, b, 'rgba(40,80,200,.12)')


def l6():
    b = (top('06')
         + '<div style="position:absolute;left:0;right:0;top:160px;text-align:center"><div class="lab">Para tu energía al entrenar</div>'
           '<div class="h" style="font-size:150px;margin-top:16px">Elige uno.</div><div class="h o" style="font-size:150px">No los combines.</div></div>'
         + P.heroe('p_guarana.png', 330, 1030, 430) + P.heroe('p_lipo.png', 750, 1030, 400)
         + '<div class="lab" style="position:absolute;left:130px;width:400px;top:1060px;text-align:center;color:#f4f1ec">Guaraná Shot<br><span style="color:#9a958e">Al paso · 200 mg</span></div>'
         + '<div class="lab" style="position:absolute;left:550px;width:400px;top:1060px;text-align:center;color:#f4f1ec">Lipo 6 Black<br><span style="color:#9a958e">Cápsula · 222 mg</span></div>'
         + '<div style="position:absolute;left:0;right:0;bottom:120px;text-align:center;font-weight:600;font-size:26px;letter-spacing:6px;text-transform:uppercase">'
           'Pídelo por DM <span class="o">·</span> Delivery en Caldera $1.500</div>'
         + nota(GUA + '<br>' + LIPO, 40))
    return P.page(W, H, b, 'rgba(242,106,27,.10)')


# ---------------- HISTORIAS 9:16 ----------------
def h1():  # quiz, sticker en 1080–1400 (sin la respuesta a la vista)
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:160px">Semana de la energía · Ep. 1</div>'
         + '<div style="position:absolute;left:80px;right:80px;top:340px"><div class="lab o" style="color:#F26A1B">Quiz</div>'
           '<div class="h" style="font-size:120px;margin-top:26px">Te tomas un shot</div><div class="h" style="font-size:120px">a las 6 PM.</div>'
           '<div class="h o" style="font-size:120px;margin-top:20px">¿A qué hora queda la mitad?</div></div>'
         + P.heroe('p_guarana.png', 900, 1500, 330, 6)
         + '<div class="foot" style="left:80px;right:80px;bottom:260px;font-size:19px;letter-spacing:2px">' + GUA + '</div>')
    return P.page(SW, SH, b, 'rgba(120,170,60,.10)')


def h2():  # respuesta
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:160px">La respuesta</div>'
         + '<div style="position:absolute;left:80px;top:360px"><div class="lab">A eso de las</div>'
           '<div class="h o" style="font-size:380px;margin-top:10px">11 PM.</div></div>'
         + '<div style="position:absolute;left:80px;width:560px;top:880px"><div class="rule" style="margin-bottom:28px"></div>'
           '<div style="font-size:44px;line-height:1.25;font-weight:500;color:#e8e4dd">Unas 5 horas después todavía tienes la mitad. Varía según la persona.</div>'
           '<div class="foot" style="position:static;margin-top:40px">Lo que sí y lo que no, en el post de hoy</div></div>'
         + P.heroe('p_guarana.png', 850, 1490, 480, -4)
         + '<div class="foot" style="left:80px;right:80px;bottom:260px;font-size:19px;letter-spacing:2px;text-align:center">' + GUA + '</div>')
    return P.page(SW, SH, b, 'rgba(200,40,30,.12)')


def h3():  # slider: ¿con cuánta batería llegas hoy? (sticker en 1150–1450)
    bat = ('<div style="position:absolute;left:340px;top:820px;width:360px;height:180px;border:8px solid #f4f1ec;border-radius:26px">'
           '<div style="position:absolute;left:14px;top:14px;bottom:14px;width:90px;background:#F26A1B;border-radius:10px"></div></div>'
           '<div style="position:absolute;left:708px;top:870px;width:26px;height:80px;background:#f4f1ec;border-radius:0 10px 10px 0"></div>')
    b = (P.marca(70, 150) + '<div class="foot" style="right:70px;top:160px">Semana de la energía</div>'
         + '<div style="position:absolute;left:0;right:0;top:360px;text-align:center"><div class="lab o" style="color:#F26A1B">Desliza</div>'
           '<div class="h" style="font-size:170px;margin-top:30px">¿Con cuánta</div><div class="h o" style="font-size:170px">batería llegas?</div></div>'
         + bat
         + '<div class="foot" style="left:0;right:0;text-align:center;bottom:300px">Hoy al gym</div>')
    return P.page(SW, SH, b, 'rgba(242,106,27,.10)')


if __name__ == '__main__':
    P.render([('1_portada', l1()), ('2_30_a_60_min', l2()), ('3_reloj_cafeina', l3()), ('4_suma_el_cafe', l4()),
              ('5_dormir_primero', l5()), ('6_elige_uno', l6())], FEED, W, H)
    P.render([('1_quiz_6pm', h1()), ('2_respuesta_11pm', h2()), ('3_slider_bateria', h3())], HIST, SW, SH)
