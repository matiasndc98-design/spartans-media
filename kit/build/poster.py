"""Póster publicitario de impacto (estilo anuncio de marca grande): producto inclinado gigante, explosión de polvo,
texto de fondo enorme y titular corto. Una sola imagen 4:5.
Uso (desde kit/build): python3 poster.py <salida.jpg>
"""
import sys, os
OUT = sys.argv[1] if len(sys.argv) > 1 else 'poster.jpg'
sys.argv = [sys.argv[0]]
import premium as P
import gen

OR = '#F26A1B'
POLVO = """<canvas id="pv" width="1080" height="1350" style="position:absolute;inset:0"></canvas><script>
const c=document.getElementById('pv').getContext('2d');let s=777;const r=()=>{s=(s*16807)%2147483647;return s/2147483647};
const cx=650,cy=520;
for(let i=0;i<14000;i++){const a=r()*Math.PI*2,d=Math.pow(r(),.7)*600,x=cx+Math.cos(a)*d*1.15,y=cy+Math.sin(a)*d*.8;
 const sz=(1-d/600)*4.5+.6,al=(1-d/600)*.75+.08;const w=r();
 c.fillStyle=w<.55?`rgba(242,${100+r()*60|0},${20+r()*30|0},${al})`:`rgba(235,225,210,${al*.8})`;c.beginPath();c.arc(x,y,sz,0,7);c.fill()}
for(let i=0;i<60;i++){const a=r()*Math.PI*2,d=300+r()*360,x=cx+Math.cos(a)*d,y=cy+Math.sin(a)*d*.8,len=40+r()*120;
 c.strokeStyle=`rgba(242,106,27,${.15+r()*.3})`;c.lineWidth=1+r()*2;c.beginPath();c.moveTo(x,y);c.lineTo(x+Math.cos(a)*len,y+Math.sin(a)*len);c.stroke()}
let g=c.createRadialGradient(cx,cy,0,cx,cy,520);g.addColorStop(0,'rgba(242,106,27,.55)');g.addColorStop(1,'rgba(0,0,0,0)');c.fillStyle=g;c.fillRect(0,0,1080,1350);
</script>"""


def poster():
    b = ('<div class="h" style="position:absolute;left:-30px;top:180px;font-size:520px;line-height:.8;color:transparent;-webkit-text-stroke:3px rgba(244,241,236,.10);white-space:nowrap">NITRO</div>'
         '<div class="h" style="position:absolute;left:-30px;top:600px;font-size:520px;line-height:.8;color:transparent;-webkit-text-stroke:3px rgba(244,241,236,.07);white-space:nowrap">TECH</div>'
         + POLVO
         + f'<img src="{P.I("p_nitro.png")}" style="position:absolute;left:390px;top:120px;height:740px;transform:rotate(-12deg);filter:drop-shadow(0 50px 60px rgba(0,0,0,.85))">'
         + P.marca(70, 64) + '<div class="foot" style="right:70px;top:74px">MuscleTech · Nitro Tech 4 lb</div>'
         + '<div style="position:absolute;left:70px;bottom:250px"><div class="h" style="font-size:150px">Un scoop.</div>'
           f'<div class="h" style="font-size:150px;color:{OR}">Doble trabajo.</div></div>'
         + '<div style="position:absolute;left:70px;right:70px;bottom:120px;display:flex;gap:60px;align-items:flex-end">'
           f'<div><div class="h" style="font-size:96px">30 G</div><div class="lab" style="color:#d8d3cb">Proteína</div></div>'
           f'<div style="width:2px;height:90px;background:{OR}"></div>'
           f'<div><div class="h" style="font-size:96px">3 G</div><div class="lab" style="color:#d8d3cb">Creatina</div></div>'
           f'<div style="width:2px;height:90px;background:{OR}"></div>'
           f'<div><div class="h" style="font-size:96px">1</div><div class="lab" style="color:#d8d3cb">Scoop</div></div></div>'
         + '<div class="foot" style="left:70px;bottom:60px;color:#d8d3cb">Pídelo por DM · Caldera, Copiapó y todo Chile</div>')
    return P.page(P.W, P.H, b, 'rgba(242,106,27,.06)')


if __name__ == '__main__':
    d = os.path.dirname(os.path.abspath(OUT)) or '.'
    P.render([(os.path.basename(OUT)[:-4], poster())], d, P.W, P.H)
