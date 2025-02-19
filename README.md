# Catify

## Índice

1. [Descripción](#descripción)
2. [Características](#características)
3. [Requisitos](#requisitos)
4. [Configuración](#configuración)
5. [Uso](#uso)
6. [Contribución](#contribución)
7. [Licencia](#licencia)
8. [Contacto](#contacto)

## Descripción

Catify es una aplicación en Python que permite generar listas de reproducción en Spotify con recomendaciones musicales basadas en Last.fm. Además, agrega una imagen de portada temática de gatos a la playlist, utilizando imágenes obtenidas de CATAAS.

## Características

- Autenticación en Spotify mediante OAuth2.
- Búsqueda de canciones y artistas en Last.fm.
- Generación de un archivo CSV con recomendaciones musicales.
- Creación de una playlist en Spotify con las canciones recomendadas.
- Generación y subida automática de una imagen de portada.

## Requisitos

Para ejecutar Catify, es necesario instalar las siguientes dependencias:

```bash
pip install spotipy requests pandas pillow matplotlib
```

Además, se deben configurar credenciales en Spotify y Last.fm:

- [Crear una aplicación en Spotify Developer](https://developer.spotify.com/dashboard/applications)
- [Obtener una API Key en Last.fm](https://www.last.fm/api/account/create)

## Configuración

Antes de ejecutar el script, se deben definir las siguientes variables de entorno:

```python
SPOTIFY_CLIENT_ID = "TU_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "TU_CLIENT_SECRET"
SPOTIFY_REDIRECT_URI = "https://example.org/callback"
LASTFM_API_KEY = "TU_LASTFM_API_KEY"
```

## Uso

Ejecutar el script principal con:

```bash
python catify.py
```

### Flujo de ejecución

1. Autenticación en Spotify.
2. Búsqueda de una canción y obtención de recomendaciones.
3. Generación de un archivo CSV con las recomendaciones.
4. Creación de una nueva playlist en Spotify.
5. Adición de las canciones recomendadas a la playlist.
6. Generación de una imagen de portada con CATAAS.
7. Subida de la imagen como portada de la playlist.

## Contribución

Las contribuciones son bienvenidas. Para colaborar, seguir estos pasos:

1. Hacer un fork del repositorio.
2. Crear una rama con la nueva funcionalidad (`git checkout -b feature-nueva-funcionalidad`).
3. Realizar los cambios y hacer commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Subir la rama (`git push origin feature-nueva-funcionalidad`).
5. Abrir un Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Consultar el archivo `LICENSE` para más detalles.

## Contacto

Para dudas o sugerencias, abrir un issue o contactar al desarrollador.

