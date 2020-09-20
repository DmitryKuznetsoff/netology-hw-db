create table if not exists Genre(
	id serial primary key,
	name varchar(50) not null unique
);

create table if not exists Artist(
	id serial primary key,
	name varchar(50) not null unique
);

create table if not exists xArtistGenre(
	id serial primary key,
	artist_id integer not null references Artist(id),
	genre_id integer not null references Genre(id)
);

create table if not exists Album(
	id serial primary key,
	name varchar(50) not null unique,
	year integer not null
);

create table if not exists xArtistAlbum(
	id serial primary key,
	artist_id integer not null references Artist(id),
	album_id integer not null references Album(id)
);

create table if not exists Track(
	id serial primary key,
	album_id integer not null references Album(id),
	name varchar(150) not null,
	duration integer not null
);

create table if not exists Collection(
	id serial primary key,
	name varchar(150) not null unique,
	year integer not null
);

create table if not exists xTrackCollection(
	id serial primary key,
	track_id integer not null references Track(id),
	collection_id integer not null references Collection(id)
);
