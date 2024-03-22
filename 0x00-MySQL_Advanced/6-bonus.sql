-- creates procedure AddBonus that adds new correction for a student
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(30), IN score INT)
BEGIN
	DECLARE available_project INT;
	DECLARE projectId INT;
	SELECT COUNT(*) INTO available_project  FROM projects WHERE name = project_name;
	IF available_project > 0 THEN
		SELECT id INTO projectId FROM projects WHERE name = project_name;
		UPDATE corrections SET score = score WHERE user_id = user_id AND project_id = projectId;
	ELSE
		INSERT INTO projects (name) VALUES(project_name);
		SET @project_id = LAST_INSERT_ID();
		INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, @project_id, score);
	END IF;
END
$$