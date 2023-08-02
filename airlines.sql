-- Q1. Airlines
/* 
For each passenger, report their passenger ID, full name, and the number of 
different airlines on which they took a fight. 
*/

-- You must not change the next 2 lines or the table definition.
SET SEARCH_PATH TO air_travel;
DROP TABLE IF EXISTS q1 CASCADE;

CREATE TABLE q1 (
    pass_id INT,
    name VARCHAR(100),
    airlines INT
);

-- Do this for each of the views that define your intermediate steps.  
-- (But give them better names!) The IF EXISTS avoids generating an error 
-- the first time this file is imported.
DROP VIEW IF EXISTS intermediate_step CASCADE;


-- Define views for your intermediate steps here:


-- Your query that answers the question goes below the "insert into" line:
INSERT INTO q1
SELECT p.id, CONCAT(firstname, ' ', surname), count(airline)
FROM passenger p
LEFT JOIN booking b 
ON p.id = b.pass_id 
LEFT JOIN flight f
ON f.id = b.flight_id
GROUP BY p.id
ORDER BY p.id ASC
;