-- Write a script that lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each.
SELECT	tv_genres.name AS genre,
	COUNT(*) AS number_of_shows
FROM	tv_shows
	LEFT OUTER JOIN tv_show_genres
		ON tv_shows.id = tv_show_genres.show_id
	LEFT OUTER JOIN tv_genres
		ON tv_genres.id = tv_show_genres.genre_id
WHERE	tv_show_genres.genre_id IS NOT NULL
GROUP BY genre
ORDER BY number_of_shows DESC;