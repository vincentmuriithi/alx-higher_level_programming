-- Script hat uses the hbtn_0d_tvshows database
-- to list all genres not linked to the show DexterSELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
    -- Subquery to get the genre IDs linked to Dexter
    SELECT DISTINCT tv_genres.id
    FROM tv_shows
    JOIN tv_genres
    ON tv_shows.id = tv_genres.show_id
    WHERE tv_shows.title = 'Dexter'
) AS DexterGenres
ON tv_genres.id = DexterGenres.id
WHERE DexterGenres.id IS NULL
ORDER BY tv_genres.name;
