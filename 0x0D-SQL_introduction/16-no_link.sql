-- list all tables in the database and more
-- also does some cool stuff
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
