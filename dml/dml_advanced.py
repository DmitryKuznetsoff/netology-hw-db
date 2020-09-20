import sqlalchemy

db = 'postgresql://netology:netology@localhost:5432/netology_hw'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# количество исполнителей в каждом жанре:
select2_1 = connection.execute("""SELECT name, COUNT(name) FROM Genre
                                JOIN xArtistGenre ON genre.id = xArtistGenre.genre_id
                                GROUP BY name
                                ORDER BY name;""").fetchall()
print(*select2_1, sep='\n')

# количество треков, вошедших в альбомы 2019-2020 годов:
select2_2 = connection.execute("""SELECT Album.name, COUNT(Album.name) from Album
                                JOIN Track on Album.id = Track.album_id
                                WHERE Album.year BETWEEN 2019 AND 2020
                                GROUP BY Album.name;""").fetchall()
print(*select2_2, sep='\n')

# средняя продолжительность треков по каждому альбому:
select2_3 = connection.execute("""SELECT Album.name, AVG(track.duration) FROM album
                                JOIN Track ON Album.id = Track.album_id
                                GROUP BY Album.name
                                ORDER BY Album.name;""").fetchall()
print(*select2_3, sep='\n')

# все исполнители, которые не выпустили альбомы в 2020 году:
select2_4 = connection.execute("""SELECT name FROM Artist
                                WHERE name NOT IN (SELECT Artist.name FROM Artist
                                JOIN xArtistAlbum as x ON Artist.id = x.artist_id
                                JOIN Album ON x.album_id = Album.id
                                WHERE Album.year = 2020);""").fetchall()
print(*select2_4, sep='\n')

# названия сборников, в которых присутствует конкретный исполнитель(Pantera):
select2_5 = connection.execute("""SELECT Collection.name from Collection
                                JOIN xTrackCollection ON Collection.id = xTrackCollection.collection_id
                                JOIN Track ON xTrackCollection.track_id = Track.id
                                JOIN Album ON Track.album_id = Album.id
                                JOIN xArtistAlbum ON Album.id = xArtistAlbum.album_id
                                JOIN Artist ON xArtistAlbum.artist_id = Artist.id
                                WHERE Artist.name = 'Pantera'
                                GROUP BY Collection.name;""").fetchall()
print(*select2_5, sep='\n')

# название альбомов, в которых присутствуют исполнители более 1 жанра:
select2_6 = connection.execute("""SELECT name FROM Album
                                WHERE name IN (SELECT Album.name FROM Album
                                JOIN xArtistAlbum as xAA ON Album.id = xAA.album_id
                                JOIN Artist ON xAA.artist_id = Artist.id
                                JOIN xArtistGenre as xAG ON Artist.id = xAG.artist_id
                                GROUP BY Album.name
                                HAVING(COUNT(Album.name)>1));""").fetchall()
print(*select2_6, sep='\n')

# наименование треков, которые не входят в сборники:
select2_7 = connection.execute("""SELECT t.name FROM Track as t
                                LEFT JOIN xTrackCollection as x ON t.id = x.track_id
                                WHERE x.track_id IS NULL;""").fetchall()
print(*select2_7, sep='\n')

# исполнитель(-и), написавшие самый короткий по продолжительности трек:
select2_8 = connection.execute("""SELECT Artist.name, Track.name, Track.duration FROM Artist
                                JOIN xArtistAlbum ON Artist.id = xArtistAlbum.Artist_id
                                JOIN Album ON xArtistAlbum.album_id = Album.id
                                JOIN Track ON Album.id = Track.album_id
                                WHERE Track.duration = (SELECT MIN(duration) FROM Track);""").fetchall()
print(*select2_8, sep='\n')

# название альбомов, содержащих наименьшее количество треков:
select2_9 = connection.execute("""SELECT Album.name, COUNT(Track.id) FROM Album
                                JOIN Track ON Album.id = Track.album_id
                                GROUP BY album_id, Album.name
                                HAVING COUNT(Track.id) = (
                                    SELECT MIN(c) FROM (SELECT COUNT(id) as c FROM Track
                                    GROUP BY album_id) as subq);""").fetchall()
print(*select2_9, sep='\n')
