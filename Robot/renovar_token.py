"""Renueva el token de Instagram (dura 60 días) y lo guarda de nuevo como secreto del repositorio.
Lo ejecuta GitHub Actions cada semana. Necesita el secreto GH_PAT (token de GitHub con permiso para escribir secretos)."""
import json, os, subprocess, urllib.request, urllib.parse
tok = os.environ['IG_TOKEN']
q = urllib.parse.urlencode({'grant_type': 'ig_refresh_token', 'access_token': tok})
nuevo = json.loads(urllib.request.urlopen(f'https://graph.instagram.com/refresh_access_token?{q}', timeout=60).read())['access_token']
if os.environ.get('GH_TOKEN'):
    subprocess.run(['gh', 'secret', 'set', 'IG_TOKEN', '--body', nuevo, '--repo', os.environ['GITHUB_REPOSITORY']], check=True)
    print('Token renovado y guardado.')
else:
    print('Token renovado, pero falta GH_PAT para guardarlo: renuévalo a mano antes de 60 días.')
