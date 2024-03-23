-- creates procedure AddBonus that adds new correction for a student
DELIMITER $$
CREATE PROCEDURE AddBonus(IN userid INT, IN projectname VARCHAR(30), IN pscore FLOAT)
BEGIN
	DECLARE available_project INT;
	SELECT COUNT(*) INTO available_project  FROM projects WHERE name = projectname;
	IF available_project = 0 THEN
		INSERT INTO projects (name) VALUES(projectname);
	END IF;
	INSERT INTO corrections (user_id, project_id, score) VALUES(userid, (SELECT id FROM projects WHERE name = projectname), pscore);
END
$$
