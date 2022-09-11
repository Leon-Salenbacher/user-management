-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema usermanagement
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema usermanagement
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `usermanagement` DEFAULT CHARACTER SET utf8 ;
USE `usermanagement` ;

-- -----------------------------------------------------
-- Table `mydb`.`tblUsers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `usermanagement`.`tblUsers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `profilePicture` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `usermanagement`.`tblsignInUsers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `usermanagement`.`tblsignInUsers` (
  `sessionKey` INT NOT NULL,
  `userID` INT NOT NULL,
  `created` DATETIME NOT NULL,
  `lastUpdate` DATETIME NOT NULL,
  PRIMARY KEY (`sessionKey`),
  CONSTRAINT `fk_tblsignInUsers_tblUsers`
    FOREIGN KEY (`userID`)
    REFERENCES `mydb`.`tblUsers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
