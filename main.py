from functions import save_songs, search_title_song, search_year_songs
from classes import ManagerSongs


gerenciador = ManagerSongs()

options = [
        {"choice": "1", "action": save_songs},
        {"choice": "2", "action": search_title_song},
        {"choice": "3", "action": search_year_songs},
        {"choice": "4", "action": gerenciador.random_playlist},
]

is_finished = False

while not is_finished:
    opcoes = input(
        "Bem-vindo ao Gerenciador de Músicas. O que deseja? \n [1] - Cadastrar Música \n [2] - Buscar Música Pelo Título \n [3] - Buscar Músicas Pelo ano \n [4] - Gerar Playlist Aleatória \n [5] - Sair \n"
    )

    for option in options:
        if option["choice"] == opcoes:
            option["action"]()
        if opcoes == '5':
            is_finished = True

print("Fim do Programa!")
