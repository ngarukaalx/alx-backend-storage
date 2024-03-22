-- updates item table based on activities in table order using trigger
DELIMITER $$
CREATE
TRIGGER purchase_made
AFTER INSERT
ON orders FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END;
$$
