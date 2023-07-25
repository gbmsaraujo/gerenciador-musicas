from classes import ManagerSongs
import os
import time

gerenciador = ManagerSongs()

def save_songs():
    title = input("Digite o Nome Da Música: ")
    artist = input("Digite o Artista/Banda: ")
    year = input("Digite o Ano de Lançamento: ")

    gerenciador.register_song(title, artist, int(year))
    print("Música Cadastrada com Sucesso")
    time.sleep(1.2)
    os.system("clear")


def search_title_song():
    title = input("Digite o Nome Da Música Para realizar a Busca: ")
    print(gerenciador.search_song_by_title(title))


def search_year_songs():
    year = input("Digite o Ano Para realizar a Busca: ")
    print(gerenciador.search_songs_by_year(int(year)))

