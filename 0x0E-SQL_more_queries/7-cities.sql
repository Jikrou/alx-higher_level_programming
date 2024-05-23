-- a script that creates the database hbtn_0d_usa and
-- the table cities (in the database hbtn_0d_usa) 
USE hbtn_0d_usa;
CREATE TABLE cities (
	id INT PRIMARY KEY auto_increment UNIQUE,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
	);
