# Catify 🐱

![Logo de Catify](logo.jpg)

## Índice

1. [Descripción](#descripción)
2. [Características](#características)
3. [Requisitos](#requisitos)
4. [Configuración](#configuración)
5. [Uso en Google Colab](#uso-en-google-colab)
6. [Instalación en local](#instalación-en-local)
7. [Contribución](#contribución)
8. [Licencia](#licencia)
9. [Contacto](#contacto)

## Descripción

Catify es una aplicación en Python que permite generar listas de reproducción en Spotify con recomendaciones musicales. Además, Catify agrega una imagen de portada de michis a la playlist, utilizando imágenes obtenidas de CATAAS y convertida a Base64 para cumplir con las especificaciones de la API de Spotify. 

Dado que desde el 27 de noviembre de 2024 Spotify ha restringido el acceso a varios endpoints de su Web API para nuevas aplicaciones y aquellas en desarrollo que aún no han sido lanzadas, la búsqueda de recomendaciones de canciones y artistas relacionados se realiza como puente a través de la API de Last.fm. (Se han perdido años de vida lanzando pruebas a la API de Spotify...)

Repositorio oficial: [GitHub - kzon94/catify](https://github.com/kzon94/catify)

## Características

- Autenticación en Spotify mediante OAuth2.
- Búsqueda de canciones y artistas en Last.fm.
- Generación de un archivo CSV con recomendaciones musicales.
- Creación de una playlist en Spotify con las canciones recomendadas.
- Generación y subida automática de una imagen de portada con mininos.

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
SPOTIFY_CLIENT_ID = "TU_SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "TU_SPOTIFY_CLIENT_SECRET"
SPOTIFY_REDIRECT_URI = "https://example.org/callback"
LASTFM_API_KEY = "TU_LASTFM_API_KEY"
```

**Nota:** En la API de Spotify, la URL de redirección (`SPOTIFY_REDIRECT_URI`) debe configurarse en `https://example.org/callback` si se ejecuta en Google Colab, ya que esta plataforma no permite el uso de `localhost`. Si se ejecuta en un entorno local, se puede utilizar `http://localhost:8888/callback`.

## Uso en Google Colab

Catify está diseñado para ejecutarse en Google Colab sin necesidad de configuración adicional. Para ejecutarlo en Colab, puedes clonar el repositorio directamente en Colab usando:

```python
!git clone https://github.com/kzon94/catify.git
%cd catify
!pip install -r requirements.txt
```

## Instalación en local

Si prefieres ejecutar Catify en tu entorno local (por ejemplo, en Visual Studio Code), sigue estos pasos:

1. Clona o descarga el repositorio:
   ```bash
   git clone https://github.com/kzon94/catify.git
   cd catify
   ```
2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En macOS/Linux
   venv\Scripts\activate  # En Windows
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta el script principal:
   ```bash
   python catify.py
   ```

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

