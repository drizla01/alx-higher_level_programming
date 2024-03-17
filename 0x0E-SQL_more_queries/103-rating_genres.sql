-- Write a script that list all show from hbtn_0d_tvshows_rate database
-- by their rating.
SELECT	name, sum(rating)
FROM	tv_genres
GROUP by name
ORDER BY rating desc;