-- SELECT name FROM people JOIN stars ON people.id = stars.person_id JOIN movies on stars.movie_id = movies.id WHERE year = 2004 ORDER BY year;

SELECT name FROM people WHERE id IN (
SELECT person_id FROM  stars WHERE movie_id IN (
SELECT id FROM movies WHERE year = 2004
)
);

