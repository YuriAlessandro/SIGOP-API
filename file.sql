-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema sigopdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sigopdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sigopdb` DEFAULT CHARACTER SET utf8 ;
USE `sigopdb` ;

-- -----------------------------------------------------
-- Table `sigopdb`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sigopdb`.`User` ;

CREATE TABLE IF NOT EXISTS `sigopdb`.`User` (
  `idUser` INT NOT NULL,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `status` INT NULL,
  `login` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `type` VARCHAR(45) NULL,
  `unity` VARCHAR(45) NULL,
  PRIMARY KEY (`idUser`),
  UNIQUE INDEX `login_UNIQUE` (`login` ASC),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sigopdb`.`Offer`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sigopdb`.`Offer` ;

CREATE TABLE IF NOT EXISTS `sigopdb`.`Offer` (
  `idOffer` INT NOT NULL,
  `title` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `userId` INT NULL,
  `endOffer` DATETIME(6) NULL,
  PRIMARY KEY (`idOffer`),
  INDEX `Register_idx` (`userId` ASC),
  CONSTRAINT `Register_OFFER`
    FOREIGN KEY (`userId`)
    REFERENCES `sigopdb`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sigopdb`.`Avaliation`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sigopdb`.`Avaliation` ;

CREATE TABLE IF NOT EXISTS `sigopdb`.`Avaliation` (
  `idAvaliation` INT NOT NULL,
  `date` DATETIME NULL,
  `idOffer` INT NULL,
  `userId` INT NULL,
  PRIMARY KEY (`idAvaliation`),
  INDEX `Belongs To_idx` (`idOffer` ASC),
  INDEX `Write_idx` (`userId` ASC),
  CONSTRAINT `Belongs To_AVALIATION`
    FOREIGN KEY (`idOffer`)
    REFERENCES `sigopdb`.`Offer` (`idOffer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Write_AVALIATION`
    FOREIGN KEY (`userId`)
    REFERENCES `sigopdb`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sigopdb`.`Interest`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sigopdb`.`Interest` ;

CREATE TABLE IF NOT EXISTS `sigopdb`.`Interest` (
  `idInterest` INT NOT NULL,
  `value` FLOAT NULL,
  `idUser` INT NULL,
  `location` VARCHAR(45) NULL,
  `unity` VARCHAR(45) NULL,
  PRIMARY KEY (`idInterest`),
  INDEX `idUser_idx` (`idUser` ASC),
  CONSTRAINT `Indicate_INTEREST`
    FOREIGN KEY (`idUser`)
    REFERENCES `sigopdb`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sigopdb`.`Notification`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sigopdb`.`Notification` ;

CREATE TABLE IF NOT EXISTS `sigopdb`.`Notification` (
  `idNotification` INT NOT NULL,
  `userId` INT NULL,
  `idOffer` INT NULL,
  `read` TINYINT NULL,
  `text` VARCHAR(45) NULL,
  PRIMARY KEY (`idNotification`),
  INDEX `belongsTouser_idx` (`userId` ASC),
  INDEX `Generate_idx` (`idOffer` ASC),
  CONSTRAINT `Notify_NOTIFICATION`
    FOREIGN KEY (`userId`)
    REFERENCES `sigopdb`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Generate_NOTIFICATION`
    FOREIGN KEY (`idOffer`)
    REFERENCES `sigopdb`.`Offer` (`idOffer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sigopdb`.`Favorite`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sigopdb`.`Favorite` ;

CREATE TABLE IF NOT EXISTS `sigopdb`.`Favorite` (
  `user_id` INT NOT NULL,
  `idOffer` INT NOT NULL,
  PRIMARY KEY (`user_id`, `idOffer`),
  INDEX `FavoriteOffer_idx` (`idOffer` ASC),
  CONSTRAINT `FavoriteUser_FAVORITE`
    FOREIGN KEY (`user_id`)
    REFERENCES `sigopdb`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FavoriteOffer_FAVORITE`
    FOREIGN KEY (`idOffer`)
    REFERENCES `sigopdb`.`Offer` (`idOffer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sigopdb`.`Report`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sigopdb`.`Report` ;

CREATE TABLE IF NOT EXISTS `sigopdb`.`Report` (
  `userId` INT NOT NULL,
  `idOffer` INT NOT NULL,
  `reason` VARCHAR(45) NULL,
  PRIMARY KEY (`userId`, `idOffer`),
  INDEX `ReportOffer_idx` (`idOffer` ASC),
  CONSTRAINT `ReportUser_REPORT`
    FOREIGN KEY (`userId`)
    REFERENCES `sigopdb`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ReportOffer_REPORT`
    FOREIGN KEY (`idOffer`)
    REFERENCES `sigopdb`.`Offer` (`idOffer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sigopdb`.`Generate`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sigopdb`.`Generate` ;

CREATE TABLE IF NOT EXISTS `sigopdb`.`Generate` (
  `idInterest` INT NOT NULL,
  `idNotification` INT NOT NULL,
  PRIMARY KEY (`idInterest`, `idNotification`),
  INDEX `Notification_idx` (`idNotification` ASC),
  CONSTRAINT `Interest_GENERATE`
    FOREIGN KEY (`idInterest`)
    REFERENCES `sigopdb`.`Interest` (`idInterest`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Notification_GENERATE`
    FOREIGN KEY (`idNotification`)
    REFERENCES `sigopdb`.`Notification` (`idNotification`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sigopdb`.`Offer_Vacancies`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sigopdb`.`Offer_Vacancies` ;

CREATE TABLE IF NOT EXISTS `sigopdb`.`Offer_Vacancies` (
  `type` VARCHAR(45) NULL,
  `salary_aids` FLOAT NULL,
  `salary_total` FLOAT NULL,
  `idOffer` INT NULL,
  INDEX `Offer_idx` (`idOffer` ASC),
  CONSTRAINT `Offer_VACANCIES`
    FOREIGN KEY (`idOffer`)
    REFERENCES `sigopdb`.`Offer` (`idOffer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sigopdb`.`Offer_Contact`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sigopdb`.`Offer_Contact` ;

CREATE TABLE IF NOT EXISTS `sigopdb`.`Offer_Contact` (
  `email` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  `idOffer` INT NOT NULL,
  INDEX `Offer_idx` (`idOffer` ASC),
  CONSTRAINT `Offer_CONTACT`
    FOREIGN KEY (`idOffer`)
    REFERENCES `sigopdb`.`Offer` (`idOffer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sigopdb`.`Offer_Location`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sigopdb`.`Offer_Location` ;

CREATE TABLE IF NOT EXISTS `sigopdb`.`Offer_Location` (
  `location` VARCHAR(45) NOT NULL,
  `idOffer` INT NULL,
  `latitude` VARCHAR(45) NULL,
  `longitude` VARCHAR(45) NULL,
  PRIMARY KEY (`location`),
  INDEX `Offer_idx` (`idOffer` ASC),
  CONSTRAINT `Offer_LOCATION`
    FOREIGN KEY (`idOffer`)
    REFERENCES `sigopdb`.`Offer` (`idOffer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sigopdb`.`Interest_Keyword`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sigopdb`.`Interest_Keyword` ;

CREATE TABLE IF NOT EXISTS `sigopdb`.`Interest_Keyword` (
  `keyword` VARCHAR(45) NOT NULL,
  `interestId` INT NULL,
  PRIMARY KEY (`keyword`),
  INDEX `Interest_idx` (`interestId` ASC),
  CONSTRAINT `Interest_KEYWORD`
    FOREIGN KEY (`interestId`)
    REFERENCES `sigopdb`.`Interest` (`idInterest`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sigopdb`.`Rate`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sigopdb`.`Rate` ;

CREATE TABLE IF NOT EXISTS `sigopdb`.`Rate` (
  `value` VARCHAR(45) NULL,
  `avaliationId` INT NOT NULL,
  INDEX `Avaliation_idx` (`avaliationId` ASC),
  PRIMARY KEY (`avaliationId`),
  CONSTRAINT `Avaliation_RATE`
    FOREIGN KEY (`avaliationId`)
    REFERENCES `sigopdb`.`Avaliation` (`idAvaliation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sigopdb`.`Comment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sigopdb`.`Comment` ;

CREATE TABLE IF NOT EXISTS `sigopdb`.`Comment` (
  `text` VARCHAR(45) NULL,
  `avaliationId` INT NOT NULL,
  PRIMARY KEY (`avaliationId`),
  CONSTRAINT `Avaliation_COMMENT`
    FOREIGN KEY (`avaliationId`)
    REFERENCES `sigopdb`.`Avaliation` (`idAvaliation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
