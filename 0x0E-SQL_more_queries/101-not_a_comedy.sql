-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows. 
SELECT tv_shows.title FROM tv_shows
LEFT JOIN tv_genres
WHERE tv_genres.name != Comedy
ORDER BY tv_shows.title  ASC;
