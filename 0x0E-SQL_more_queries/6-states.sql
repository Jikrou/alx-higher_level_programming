-- script that creates the database hbtn_0d_usa i
-- and the table states (in the database hbtn_0d_usa).
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
	name VARCHAR(256) NOT NULL
	);
