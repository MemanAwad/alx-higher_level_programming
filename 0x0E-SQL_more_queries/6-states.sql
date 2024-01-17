-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table if it does not exist
CREATE TABLE IF NOT EXISTS  hbtn_0d_usa, states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);

