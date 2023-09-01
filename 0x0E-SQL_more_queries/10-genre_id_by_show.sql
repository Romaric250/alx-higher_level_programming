-- show tv by tv_shows.title and tv_show_genres.genre_id
-- we are allowd only to use the select call
-- opps

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;