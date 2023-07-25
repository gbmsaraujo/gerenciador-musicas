from utils import filter_songs, filter_songs_by_year
import random

class ManagerSongs:
    def __init__(self):
        self.songs = []

    def register_song(self, title: str, artist: str, year: int):
        song = {}
        song["title"] = title.lower()
        song["artist"] = artist.lower()
        song["year"] = year

        self.songs.append(song)

    def search_song_by_title(self, title):
        filtered_song = filter_songs(self.songs, "title", title)

        if not filtered_song:
            return "Nenhum Resultado para sua Busca"

        return filtered_song

    def search_songs_by_year(self, year):
        filtered_songs = filter_songs_by_year(self.songs, year)
        if not filtered_songs:
            return "Nenhum Resultado para sua Busca"

        return filtered_songs

    def random_playlist(self):
        songs_title = [song['title'] for song in self.songs]
        return random.choices(songs_title, k=len(self.songs))
