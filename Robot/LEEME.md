# Robot de publicación (gratis)

Publica en Instagram lo que está en `Robot/cola.json`, cada 15 minutos, con GitHub Actions. No usa Metricool.

## Configuración (una sola vez)
1. Instagram en modo **profesional** (empresa o creador).
2. En developers.facebook.com: crear app → caso de uso "Administrar mensajes y contenido en Instagram" → "API con inicio de sesión de Instagram" → agregar la cuenta @spartan_fitness_spa → **Generar token**.
3. En GitHub: repositorio → Settings → Secrets and variables → Actions → New repository secret:
   - `IG_TOKEN`: el token generado.
   - `IG_USER_ID`: el ID de la cuenta que muestra el panel junto al token.
   - (Opcional) `GH_PAT`: token de GitHub con permiso "Secrets: write" para que el robot renueve solo el token de Instagram cada semana.
4. Actions → "Publicar en Instagram" → Run workflow, para probar.

## Límites
- Hasta 100 publicaciones por API cada 24 horas.
- La API no agrega música de Instagram ni stickers (encuestas): esas piezas se publican a mano.
