-- creates a stored procedure ComputeAverageWeightedScoreForUsers
--  that computes and store the average weighted score for all students.
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
DECLARE done INT DEFAULT FALSE;
DECLARE userid INT;
DECLARE total_score_weight INT;
DECLARE total_weight INT;
DECLARE avarage_weighted FLOAT;
-- Declare cursor to iterate on user ids
DECLARE user_cursor CURSOR for
SELECT id FROM users;
-- Declare handlers for cursor
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
-- OPEN CURSOR
OPEN user_cursor;
-- loop through users ids
user_loop: LOOP
-- variables in each loop
SET total_score_weight = 0;
SET total_weight = 0;
SET avarage_weighted = 0;
-- FETCH NEXT ID FROM CURSOR
FETCH user_cursor INTO userid;
IF done THEN
LEAVE user_loop;
END IF;
-- perform operation in each row to get average weighted for each student
SELECT SUM(score * weight) INTO total_score_weight
FROM
corrections
JOIN
projects ON corrections.project_id = projects.id
WHERE
corrections.user_id = userid;
SELECT SUM(weight) INTO total_weight
FROM
projects;
SET avarage_weighted = total_score_weight / total_weight;
UPDATE users SET average_score = avarage_weighted WHERE id = userid;
END LOOP;
-- Close cursor to
CLOSE user_cursor;
END;
$$
