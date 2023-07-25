import os
import time
from classes import ManagerSongs

is_finished = False

gerenciador = ManagerSongs()

while not is_finished:
    opcoes = input(
        "Bem-vindo ao Gerenciador de Músicas. O que deseja? \n [1] - Cadastrar Música \n [2] - Buscar Música Pelo Título \n [3] - Buscar Músicas Pelo ano \n [4] - Gerar Playlist Aleatória \n [5] - Sair \n"
    )
    if opcoes == "1":
        title = input("Digite o Nome Da Música: ")
        artist = input("Digite o Artista/Banda: ")
        year = input("Digite o Ano de Lançamento: ")

        gerenciador.register_song(title, artist, int(year))
        print("Música Cadastrada com Sucesso")
        time.sleep(1.2)
        os.system("clear")
    elif opcoes == "2":
        title = input("Digite o Nome Da Música Para realizar a Busca: ")
        print(gerenciador.search_song_by_title(title))

    elif opcoes == "3":
        year = input("Digite o Ano Para realizar a Busca: ")
        print(gerenciador.search_songs_by_year(int(year)))
    elif opcoes == "4":
        print(gerenciador.random_playlist())

    elif opcoes == "5":
        is_finished = True
    else:
        print("Digite uma opção válida")

print("Fim do Programa!")
