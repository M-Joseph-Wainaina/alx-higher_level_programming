-- create database in the current database in your MYSQL server
-- database will be passed as argument in the mysql command
-- if table exists script should not raise any error
CREATE TABLE IF NOT EXISTS first_table(
	id INT,
	name VARCHAR(256)
);
