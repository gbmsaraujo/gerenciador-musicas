def filter_songs(list_songs:list, key:str, value):
    for song in list_songs: 
        if song[key] == value:
            return song

def filter_songs_by_year(list_songs:list, year):
    songs_by_year = []
    for song in list_songs:
        if song['year'] == year:
            songs_by_year.append(song)
    return songs_by_year

