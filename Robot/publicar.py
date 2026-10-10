"""Robot de publicación de Suplementos Spartans.
Lee Robot/cola.json y publica en Instagram lo que ya tocó, usando la API oficial
(Instagram API con inicio de sesión de Instagram). Lo ejecuta GitHub Actions cada 15 minutos.

Formato de cada elemento de cola.json:
  {"id": "2026-10-12-historia-1", "cuando": "2026-10-12T10:00:00-03:00",
   "tipo": "HISTORIA" | "POST" | "CARRUSEL" | "REEL",
   "archivos": ["Historias/2026-10-12/h1.jpg"], "texto": "caption (POST, CARRUSEL y REEL)",
   "estado": "pendiente" | "publicado" | "error", "detalle": ""}
Secretos del repositorio: IG_TOKEN (token de larga duración) e IG_USER_ID.
Modo prueba: DRY_RUN=1 (no publica, solo muestra lo que haría).
"""
import json, os, sys, time, datetime, urllib.request, urllib.parse

API = 'https://graph.instagram.com/v21.0'
RAW = 'https://raw.githubusercontent.com/{repo}/main/{path}'
COLA = os.path.join(os.path.dirname(__file__), 'cola.json')
TOKEN = os.environ.get('IG_TOKEN', '')
USER = os.environ.get('IG_USER_ID', '')
REPO = os.environ.get('GITHUB_REPOSITORY', 'matiasndc98-design/spartans-media')
DRY = os.environ.get('DRY_RUN') == '1'


def api(method, path, **params):
    params['access_token'] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    url = f'{API}/{path}'
    req = urllib.request.Request(url + ('?' + data.decode() if method == 'GET' else ''), data=None if method == 'GET' else data, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f'{e.code}: {e.read().decode()[:400]}')


def url(path):
    return RAW.format(repo=REPO, path=urllib.parse.quote(path)) + f'?v={int(time.time())}'


def esperar(cid, minutos=8):
    for _ in range(minutos * 6):
        st = api('GET', cid, fields='status_code,status').get('status_code')
        if st == 'FINISHED':
            return
        if st in ('ERROR', 'EXPIRED'):
            raise RuntimeError(f'contenedor {cid} en estado {st}')
        time.sleep(10)
    raise RuntimeError(f'contenedor {cid} no terminó de procesar')


def contenedor(path, **extra):
    es_video = path.lower().endswith(('.mp4', '.mov'))
    p = dict(extra)
    p['video_url' if es_video else 'image_url'] = url(path)
    cid = api('POST', f'{USER}/media', **p)['id']
    esperar(cid, 8 if es_video else 2)
    return cid


def publicar(item):
    tipo, archivos, texto = item['tipo'], item['archivos'], item.get('texto', '')
    if tipo == 'HISTORIA':
        cid = contenedor(archivos[0], media_type='STORIES')
    elif tipo == 'REEL':
        cid = contenedor(archivos[0], media_type='REELS', caption=texto, share_to_feed='true')
    elif tipo == 'POST':
        cid = contenedor(archivos[0], caption=texto)
    elif tipo == 'CARRUSEL':
        hijos = [contenedor(a, is_carousel_item='true') for a in archivos[:10]]
        cid = api('POST', f'{USER}/media', media_type='CAROUSEL', children=','.join(hijos), caption=texto)['id']
        esperar(cid, 3)
    else:
        raise RuntimeError(f'tipo desconocido: {tipo}')
    return api('POST', f'{USER}/media_publish', creation_id=cid)['id']


def main():
    cola = json.load(open(COLA, encoding='utf-8'))
    ahora = datetime.datetime.now(datetime.timezone.utc)
    vencidos = [i for i in cola if i.get('estado', 'pendiente') == 'pendiente'
                and datetime.datetime.fromisoformat(i['cuando']) <= ahora]
    vencidos.sort(key=lambda i: i['cuando'])
    if not vencidos:
        print('Nada que publicar.'); return
    if not DRY and not (TOKEN and USER):
        sys.exit('Faltan los secretos IG_TOKEN e IG_USER_ID.')
    for item in vencidos:
        print(f"→ {item['id']} ({item['tipo']}) {item['archivos']}")
        if DRY:
            continue
        try:
            item['detalle'] = publicar(item)
            item['estado'] = 'publicado'
            print('  publicado', item['detalle'])
        except Exception as e:
            item['estado'] = 'error'
            item['detalle'] = str(e)[:500]
            print('  ERROR', item['detalle'])
        json.dump(cola, open(COLA, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        time.sleep(5)


if __name__ == '__main__':
    main()
