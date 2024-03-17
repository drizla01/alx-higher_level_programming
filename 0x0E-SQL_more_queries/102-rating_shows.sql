-- Write a script that list all show from hbtn_0d_tvshows_rate database
-- by their rating.
SELECT	title, rating
FROM	tv_shows
ORDER BY rating desc;