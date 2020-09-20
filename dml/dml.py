import csv
import sqlalchemy
import os

PATH_TO_CSV = os.path.join(os.getcwd(), 'csv' + os.sep)
db = 'postgresql://netology:netology@localhost:5432/netology_hw'


def get_list_for_insert(file):
    """
    получает вложенный список строк для последующей записи в БД
    """
    csv_file = PATH_TO_CSV + file
    with open(csv_file, 'r', encoding='utf-8') as f:
        result = list(csv.reader(f, delimiter=','))
        # исключаем из списка строку с заголовками:
        return result[1:]


engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# заполнение таблиц БД из CSV:

# genre = get_list_for_insert('Genre.csv')
# for id, name in genre:
#     connection.execute(f"""INSERT INTO Genre(id, name)
#     VALUES({id}, '{name}');""")
#
# artist = get_list_for_insert('Artist.csv')
# for id, name in artist:
#     connection.execute(f"""INSERT INTO Artist(id, name)
#     VALUES({id}, '{name}');""")
#
# album = get_list_for_insert('Album.csv')
# for id, name, year in album:
#     connection.execute(f"""INSERT INTO Album(id, name, year)
#     VALUES({id}, '{name}', '{year}');""")
#
# track = get_list_for_insert('Track.csv')
# for id, album_id, name, duration in track:
#     connection.execute(f"""INSERT INTO Track(id, album_id, name, duration)
#     VALUES({id}, {album_id}, '{name}', {duration});""")
#
# collection = get_list_for_insert('Collection.csv')
# for id, name, year in collection:
#     connection.execute(f"""INSERT INTO Collection(id, name, year)
#     VALUES({id}, '{name}', {year});""")
#
# xartistalbum = get_list_for_insert('xArtistAlbum.csv')
# for id, artist_id, album_id in xartistalbum:
#     connection.execute(f"""INSERT INTO xArtistAlbum(id, artist_id, album_id)
#     VALUES({id}, {artist_id}, {album_id});""")
#
# xartistgenre = get_list_for_insert('xArtistGenre.csv')
# for id, artist_id, genre_id in xartistgenre:
#     connection.execute(f"""INSERT INTO xArtistGenre(id, artist_id, genre_id)
#     VALUES({id}, {artist_id}, {genre_id});""")
#
#
# xtrackcollection = get_list_for_insert('xTrackCollection.csv')
# for id, track_id, collection_id in xtrackcollection:
#     connection.execute(f"""INSERT INTO xTrackCollection(id, track_id, collection_id)
#     VALUES({id}, {track_id}, {collection_id});""")

# название и год выхода альбомов, вышедших в 2018 году:
select1 = connection.execute("""SELECT name, year FROM Album WHERE year=2018;""").fetchall()
print(*select1, sep='\n')
# название и продолжительность самого длительного трека
select2 = connection.execute("""SELECT name, duration FROM Track ORDER BY duration DESC LIMIT 1;""").fetchone()
print('---------------------------------')
print(*select2, sep='\n')
# название треков, продолжительность которых не менее 3,5 минуты
select3 = connection.execute("""SELECT name FROM Track WHERE duration >= 210;""").fetchall()
print('---------------------------------')
print(*select3, sep='\n')
# названия сборников, вышедших в период с 2018 по 2020 год включительно
print('---------------------------------')
select4 = connection.execute("""SELECT name FROM Collection WHERE year BETWEEN 2018 and 2020;""").fetchall()
print(*select4, sep='\n')
# исполнители, чье имя состоит из 1 слова
print('---------------------------------')
select5 = connection.execute("""SELECT name FROM Artist WHERE name not LIKE '%% %%';""").fetchall()
print(*select5, sep='\n')
# название треков, которые содержат слово "мой"/"my"
print('---------------------------------')
select6 = connection.execute("""SELECT name FROM Track WHERE name LIKE '%%My%%';""").fetchall()
print(*select6, sep='\n')

