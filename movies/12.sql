SELECT title FROM movies JOIN stars ON movies.id = stars.movie_id WHERE person_id = (SELECT id FROM people WHERE name = "Johnny Depp") AND title IN (SELECT title FROM movies JOIN stars ON movies.id = stars.movie_id WHERE person_id = (SELECT id FROM people WHERE name = "Helena Bonham Carter")
);




-- JOIN people ON stars.person_id = people.id WHERE person_id IN (
-- );

-- SELECT id FROM people WHERE name = "Johnny Depp"; --OR name = "Helena Bonham Carter"

-- SELECT title FROM movies WHERE