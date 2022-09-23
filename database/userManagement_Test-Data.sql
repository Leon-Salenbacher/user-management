-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Drop Schema usermanagement
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `usermanagement`;  

-- -----------------------------------------------------
-- Schema usermanagement
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `usermanagement` DEFAULT CHARACTER SET utf8 ;
USE `usermanagement` ;

-- -----------------------------------------------------
-- Table `usermanagement`.`tblUsers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usermanagement`.`tblUsers`;
CREATE TABLE IF NOT EXISTS `usermanagement`.`tblUsers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `profilePicture` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Insert Data to tblUsers
-- -----------------------------------------------------
INSERT INTO tblUsers (id, username, email, password, profilePicture) 
VALUES
	(1, 'Leon', 'leon@gmail.com', 'LeonPW', 'default'),
	(2, 'Rolf', 'Rolf@gmail.com', 'RolfPW', 'default'),
	(3, 'Max', 'max@gmail.com', 'MaxPW', 'default');

-- -----------------------------------------------------
-- Table `usermanagement`.`tblsignInUsers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `usermanagement`.`tblsignInUsers`;
CREATE TABLE IF NOT EXISTS `usermanagement`.`tblsignInUsers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `sessionKey` VARCHAR(45) NOT NULL,
  `userID` INT NOT NULL,
  `created` DATETIME NOT NULL,
  `lastUpdate` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_tblsignInUsers_tblUsers`
    FOREIGN KEY (`userID`)
    REFERENCES `usermanagement`.`tblUsers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Insert Data to tblsignInUsers YYYY-MM-DD hh:mm:ss
-- -----------------------------------------------------
INSERT INTO tblsignInUsers (id, sessionKey, userID, created, lastUpdate) 
VALUES
	(1, '9480275908', '1', '2022-09-16 22:06:02', '2022-09-16 22:06:02'),
	(2, '420857324', '2', '2022-09-16 10:06:02', '2022-09-16 13:06:02'),
	(3, '824579802', '3', '2022-09-16 07:06:02', '2022-09-16 20:06:02');

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
