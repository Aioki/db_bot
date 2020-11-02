CREATE SCHEMA IF NOT EXISTS `eatapp_db` ;
USE `eatapp_db`;

CREATE TABLE `eatapp_db`.`dish_type` (
  `id` 	 INT  UNSIGNED NOT NULL AUTO_INCREMENT,
  `type` NVARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`));


CREATE TABLE IF NOT EXISTS `eatapp_db`.`cuisine_nationality` (
  `id` 	  INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `value` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE IF NOT EXISTS `eatapp_db`.`dish` (
  `id` 				   INT 			UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` 			   NVARCHAR(100) NOT NULL,
  `photo` 			   NVARCHAR(80)  NULL,
  `food_type`   	   INT 			UNSIGNED NULL,
  `recipe`			   NVARCHAR(500) NULL,
  `cuisin_nationality` INT 			UNSIGNED NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`food_type`) REFERENCES `eatapp_db`.`dish_type` (`id`),
  FOREIGN KEY (`cuisin_nationality`) REFERENCES `eatapp_db`.`cuisine_nationality` (`id`)
);

CREATE TABLE IF NOT EXISTS `eatapp_db`.`interior` (
  `id`    INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `value` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE IF NOT EXISTS `eatapp_db`.`preferences` (
  `id` 					INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `cuisine_nationality` INT UNSIGNED NULL,
  `interior` 		 	INT UNSIGNED NULL,
  `tips_percentage`  	FLOAT NULL,
  `is_vegan` 		 	INT NULL,
  `is_sweet_tooth`   	INT NULL,
  `is_raw_food`      	INT NULL,
  `best_drink`       	INT UNSIGNED NULL,
  `best_first_meal`  	INT UNSIGNED NULL,
  `best_second_meal` 	INT UNSIGNED NULL,
  `best_dessert`     	INT UNSIGNED NULL,
  `other`            	NVARCHAR(200) NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`cuisine_nationality`) REFERENCES `eatapp_db`.`cuisine_nationality` (`id`),
  FOREIGN KEY (`interior`)			  REFERENCES `eatapp_db`.`interior` (`id`),
  FOREIGN KEY (`best_drink`) 		  REFERENCES `eatapp_db`.`dish` (`id`),
  FOREIGN KEY (`best_first_meal`)	  REFERENCES `eatapp_db`.`dish` (`id`),
  FOREIGN KEY (`best_second_meal`)	  REFERENCES `eatapp_db`.`dish` (`id`),
  FOREIGN KEY (`best_dessert`)		  REFERENCES `eatapp_db`.`dish` (`id`)
);

CREATE TABLE IF NOT EXISTS `eatapp_db`.`gender` (
  `id`    INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `value` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE IF NOT EXISTS `eatapp_db`.`role` (
  `id`    INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `value` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE IF NOT EXISTS `eatapp_db`.`user` (
  `id` 			INT 		  UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` 		NVARCHAR(45)  NOT NULL,
  `age` 		INT 		  UNSIGNED NULL,
  `gender` 		INT 		  UNSIGNED NOT NULL,
  `avatar`	 	NVARCHAR(100) NULL,
  `preferences` INT 		  UNSIGNED NULL,
  `status` 		NVARCHAR(100) NULL,
  `role` 		INT 		  UNSIGNED NOT NULL,
  `login` 		NVARCHAR(45)  NOT NULL,
  `password` 	NVARCHAR(45)  NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`gender`) REFERENCES `eatapp_db`.`gender` (`id`),
  FOREIGN KEY (`preferences`) REFERENCES `eatapp_db`.`preferences` (`id`),
  FOREIGN KEY (`role`) REFERENCES `eatapp_db`.`role` (`id`)
);

CREATE TABLE IF NOT EXISTS `eatapp_db`.`place` (
  `id` 					INT 		  UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` 				NVARCHAR(45)  NOT NULL,
  `photo` 				NVARCHAR(45)  NULL,
  `cuisine_nationality` INT 		  UNSIGNED NULL,
  `interior` 			INT 		  UNSIGNED NULL,
  `tagline` 			NVARCHAR(100) NULL,
  `other` 				NVARCHAR(700) NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`cuisine_nationality`) REFERENCES `eatapp_db`.`cuisine_nationality` (`id`),
  FOREIGN KEY (`interior`) REFERENCES `eatapp_db`.`interior` (`id`)
);

CREATE TABLE IF NOT EXISTS `eatapp_db`.`address` (
  `id` 		   INT 			UNSIGNED NOT NULL AUTO_INCREMENT,
  `country`    NVARCHAR(45) NOT NULL,
  `region` 	   NVARCHAR(45) NOT NULL,
  `mail_index` NVARCHAR(45) NULL,
  `street`	   NVARCHAR(45) NOT NULL,
  `house` 	   NVARCHAR(45) NOT NULL,
  `apartment`  NVARCHAR(45) NULL,
  `place`      INT 			UNSIGNED NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`place`) REFERENCES `eatapp_db`.`place` (`id`)
);

CREATE TABLE IF NOT EXISTS `eatapp_db`.`message` (
  `id` 		  INT 		   UNSIGNED NOT NULL AUTO_INCREMENT,
  `datetime`  DATETIME 	   NOT NULL,
  `content`   NVARCHAR(45) NOT NULL,
  `sender`    INT 		   UNSIGNED NOT NULL,
  `recipient` INT 		   UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`sender`) 	REFERENCES `eatapp_db`.`user` (`id`),
  FOREIGN KEY (`recipient`) REFERENCES `eatapp_db`.`user` (`id`)
);

CREATE TABLE IF NOT EXISTS `eatapp_db`.`invitation` (
  `id` 				INT 	 UNSIGNED NOT NULL AUTO_INCREMENT,
  `datetime` 		DATETIME NOT NULL,
  `place` 			INT 	 UNSIGNED NOT NULL,
  `who_will_pay` 	TINYINT  NULL,
  `massage` 		INT 	 NOT NULL,
  `inviting_person` INT 	 UNSIGNED NOT NULL,
  `pecipient` 		INT 	 UNSIGNED NULL,
  `accepted` 		INT 	 NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`place`) 		  REFERENCES `eatapp_db`.`address` (`id`),
  FOREIGN KEY (`inviting_person`) REFERENCES `eatapp_db`.`user` (`id`),
  FOREIGN KEY (`pecipient`) 	  REFERENCES `eatapp_db`.`user` (`id`)
);


CREATE TABLE IF NOT EXISTS `eatapp_db`.`food_assortment` (
  `id`    INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `place` INT UNSIGNED NOT NULL,
  `dish`  INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`place`) REFERENCES `eatapp_db`.`place` (`id`),
  FOREIGN KEY (`dish`)  REFERENCES `eatapp_db`.`dish` (`id`)
);


CREATE TABLE IF NOT EXISTS `eatapp_db`.`favorite_places` (
  `id`   	INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `user` 	INT UNSIGNED NOT NULL ,
  `address` INT UNSIGNED NOT NULL ,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user`)    REFERENCES `eatapp_db`.`user` (`id`),
  FOREIGN KEY (`address`) REFERENCES `eatapp_db`.`address` (`id`)
);

/* 	invitation*/
/* 	massage to message
	message to nvarchar
	
*/

/*	address
	
	add town nvarchar(45) after mail_index
*/

/* is to boolean
*/