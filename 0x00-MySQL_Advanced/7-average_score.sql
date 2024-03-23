-- calculates average score and store it on the user table
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN userid INT)
BEGIN
	DECLARE total_projects INT;
	DECLARE total_scores FLOAT;
	DECLARE average FLOAT;
	SELECT COUNT(score) INTO total_projects FROM corrections WHERE user_id = userid;
	SELECT SUM(score) INTO total_scores FROM corrections WHERE user_id = userid;
	SET average = total_scores / total_projects;
	UPDATE users SET average_score = average WHERE id = userid;
END;
$$
