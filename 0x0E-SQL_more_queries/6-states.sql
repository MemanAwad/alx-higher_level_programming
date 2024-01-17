-- Create hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table states if it does not exist
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
	PRIMARY KEY(`id`),
	`id`   INT          NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(256) NOT NULL
);
