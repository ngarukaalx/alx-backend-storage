-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN userid INT)
BEGIN
	DECLARE total_score_weight INT;
	DECLARE total_weight INT;
	DECLARE avarage_weighted FLOAT;
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
END$$
