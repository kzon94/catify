# Generador de Playlists de Spotify con Portadas de Gatos

Este proyecto automatiza la creación de playlists en Spotify basándose en una canción de referencia. Además, genera recomendaciones musicales similares y asigna una divertida portada aleatoria de la API de [CATAAS](https://cataas.com).

## Tabla de Contenidos
1. [Descripción](#descripción)  
2. [Características](#características)  
3. [Requisitos](#requisitos)  
4. [Instalación y Configuración](#instalación-y-configuración)  
5. [Uso](#uso)  
6. [Contribuciones](#contribuciones)  
7. [Licencia](#licencia)  
8. [Autor](#autor)

---

## Descripción
Este repositorio contiene un script en Python que integra múltiples APIs y librerías para:
- **Buscar canciones** usando [Last.fm](https://www.last.fm/api) y [Spotipy (Spotify API)](https://spotipy.readthedocs.io/).
- **Generar recomendaciones** de canciones similares.
- **Crear y actualizar playlists** en tu cuenta de Spotify.
- **Asignar portadas aleatorias** de gatos gracias a la API de [CATAAS](https://cataas.com).

---

## Características
- **Autenticación automática** en Spotify mediante OAuth.
- **Búsqueda en Last.fm** para identificar título y artista correctos.
- **Capa de recomendaciones** con hasta 49 canciones similares.
- **Almacenamiento en CSV** usando [pandas](https://pandas.pydata.org/).
- **Creación de playlists** pública o privada.
- **Subida de portada** a Spotify codificada en Base64.
- **Mensajes descriptivos** en consola para guiar el proceso.

---

## Requisitos
1. **Cuenta de Spotify** y una aplicación creada en [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) para obtener:
   - Client ID  
   - Client Secret  
   - Redirect URI (que coincida con la registrada en la aplicación de Spotify)  
2. **API Key de Last.fm**: crear una cuenta de desarrollador y obtener tu clave [aquí](https://www.last.fm/api).
3. **Python 3** y las librerías necesarias:
   - `spotipy`
   - `requests`
   - `pandas`
   - `Pillow` (para manejar la imagen de portada)
   - `base64`
   - `matplotlib` (opcional, incluida en el script)
4. **Entorno de ejecución**:  
   - [Google Colab](https://colab.research.google.com/)  
   - O localmente con un entorno virtual (ej. `venv` o `conda`).

---

## Instalación y Configuración
1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo
