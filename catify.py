import os
import webbrowser
import requests
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image
import base64
import matplotlib.pyplot as plt
import sys

# Configuración de claves y constantes
SPOTIFY_CLIENT_ID = "TU_SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "TU_SPOTIFY_CLIENT_SECRET"
SPOTIFY_REDIRECT_URI = "https://example.org/callback"
SPOTIFY_SCOPE = "playlist-modify-public playlist-modify-private ugc-image-upload"
LASTFM_API_KEY = "TU_LASTFM_API_KEY"
CSV_FILENAME = "songs_recommendations.csv"
IMAGE_PATH = "michis.jpg"

# Verificación de claves
if (SPOTIFY_CLIENT_ID == "TU_SPOTIFY_CLIENT_ID" or SPOTIFY_CLIENT_SECRET == "TU_SPOTIFY_CLIENT_SECRET" or
        LASTFM_API_KEY == "TU_LASTFM_API_KEY"):
    print("❌ Error: Las claves de API no están configuradas correctamente.")
    sys.exit(1)

print("\n🔒 Iniciando autenticación en Spotify...")

# Autenticación sin abrir navegador
auth_manager = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope=SPOTIFY_SCOPE,
    open_browser=False
)

authorize_url = auth_manager.get_authorize_url()
print("\n🔎 Accediendo a URL de autorización...")

sp = spotipy.Spotify(auth_manager=auth_manager)
print("\n✅ Autenticación completada.")

# Obtener información del usuario
def get_user_info():
    user_info = sp.current_user()
    print(f"\n👤 Usuario autenticado: {user_info['display_name']} (" +
          f"{user_info['external_urls']['spotify']})")
    return user_info['id']

# Generar CSV de recomendaciones
def generate_songs_csv():
    query = input("\n🎵 Ingresa el nombre de la canción y el artista: ")

    # Buscar en Last.fm
    search_url = f"http://ws.audioscrobbler.com/2.0/?method=track.search&track={query}&api_key={LASTFM_API_KEY}&format=json"
    r = requests.get(search_url)
    if r.status_code != 200:
        print("❌ Error al obtener datos de Last.fm.")
        return
    data = r.json()
    if ("results" not in data or "trackmatches" not in data["results"] or
            "track" not in data["results"]["trackmatches"]):
        print("⚠️ No se encontró la canción en Last.fm.")
        return

    first_result = data["results"]["trackmatches"]["track"][0]
    track_name = first_result["name"]
    artist_name = first_result["artist"]
    print(f"\n✅ Encontrada en Last.fm: {track_name} - {artist_name}")

    # Buscar en Spotify
    query_spotify = f"track:{track_name} artist:{artist_name}"
    results = sp.search(q=query_spotify, type="track", limit=1)
    found_songs = []
    if results["tracks"]["items"]:
        track_sp = results["tracks"]["items"][0]
        track_info = {
            "title": track_sp["name"],
            "artist": ", ".join(a["name"] for a in track_sp["artists"]),
            "url": track_sp["external_urls"]["spotify"]
        }
        found_songs.append(track_info)
        print(f"✅ Encontrada en Spotify: {track_info['title']} - {track_info['artist']}")
        print("\n🔎 Canciones similares:\n")
    else:
        print(f"⚠️ No se encontró '{track_name}' - {artist_name} en Spotify.")

    df_songs = pd.DataFrame(found_songs)
    df_songs.to_csv(CSV_FILENAME, index=False)

    # Canciones similares
    similar_url = f"http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist={artist_name}&track={track_name}&api_key={LASTFM_API_KEY}&format=json"
    r = requests.get(similar_url)
    if r.status_code == 200:
        data = r.json()
        if "similartracks" in data and "track" in data["similartracks"]:
            for t in data["similartracks"]["track"][:49]:
                similar_artist = t["artist"]["name"]
                title = t["name"]
                q = f"track:{title} artist:{similar_artist}"
                similar_res = sp.search(q=q, type="track", limit=1)
                if similar_res["tracks"]["items"]:
                    track_sp = similar_res["tracks"]["items"][0]
                    track_info = {
                        "title": track_sp["name"],
                        "artist": ", ".join(a["name"] for a in track_sp["artists"]),
                        "url": track_sp["external_urls"]["spotify"]
                    }
                    found_songs.append(track_info)
                    print(f"{track_info['title']} - {track_info['artist']} ({track_info['url']})")

    df_songs = pd.DataFrame(found_songs)
    df_songs.to_csv(CSV_FILENAME, index=False)
    print(f"\n📁 CSV generado en: {CSV_FILENAME}")

# Crear playlist
def create_playlist(user_id):
    playlist_name = input("\n📋 Nombre de la nueva playlist: ")
    playlist = sp.user_playlist_create(
        user=user_id,
        name=playlist_name,
        public=True,
        description="Playlist de recomendados con mininos :D"
    )
    print(f"\n✅ Playlist creada: {playlist['name']} (" +
          f"{playlist['external_urls']['spotify']})")
    return playlist['id']

# Añadir canciones
def add_songs_to_playlist(playlist_id):
    df_songs = pd.read_csv(CSV_FILENAME)
    uris = df_songs["url"].tolist()
    if uris:
        sp.playlist_add_items(playlist_id, uris)
        print("\n🎶 Canciones añadidas correctamente.")
    else:
        print("⚠️ No se encontraron canciones en el CSV.")

# Generar portada con CATAAS
def generate_cover_image():
    print("\n🔄 Escogiendo al minino indicado con CATAAS...")
    cover_url = "https://cataas.com/cat?width=300&height=300"
    r = requests.get(cover_url)
    if r.status_code == 200:
        with open(IMAGE_PATH, "wb") as f:
            f.write(r.content)
        print(f"✅ Portada generada en: {IMAGE_PATH}")
    else:
        print("Error: No se pudo obtener imagen de cataas.com.")

# Subir portada
def upload_playlist_cover(playlist_id):
    with open(IMAGE_PATH, "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode("utf-8")
    token = sp.auth_manager.get_access_token(as_dict=False)
    resp = requests.put(
        f"https://api.spotify.com/v1/playlists/{playlist_id}/images",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "image/jpeg"},
        data=encoded_image
    )
    if resp.status_code == 202:
        print("\n✅ Portada actualizada correctamente.")

# Flujo principal
def main():
    user_id = get_user_info()
    generate_songs_csv()
    playlist_id = create_playlist(user_id)
    add_songs_to_playlist(playlist_id)
    generate_cover_image()
    upload_playlist_cover(playlist_id)
    print("\n🎉 Proceso completado.")

if __name__ == "__main__":
    main()
