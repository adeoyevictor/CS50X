SELECT title FROM movies JOIN stars ON movies.id = stars.movie_id WHERE person_id = (SELECT id FROM people WHERE name = "Johnny Depp") AND title IN (SELECT title FROM movies JOIN stars ON movies.id = stars.movie_id WHERE person_id = (SELECT id FROM people WHERE name = "Helena Bonham Carter")
);
