CREATE DATABASE  IF NOT EXISTS `shedule`;
USE `shedule`;

/* Ôàêóëüòåò */
CREATE TABLE `shedule`.`faculty` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));

/* Êàôåäğà */
CREATE TABLE `shedule`.`dapartment` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `name` NVARCHAR(45) NOT NULL,
  `faculty_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `faculty_id_idx` (`faculty_id` ASC) VISIBLE,
  CONSTRAINT `faculty_id`
    FOREIGN KEY (`faculty_id`)
    REFERENCES `shedule`.`faculty` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);

/* Ïîëüçîâàòåëü */
CREATE TABLE `shedule`.`user` (
  `id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`));

/* Çàìåòêà */
CREATE TABLE `shedule`.`note` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `context` NVARCHAR(200) NULL,
  `user_id` INT UNSIGNED NULL,
  PRIMARY KEY (`id`),
  INDEX `user_Id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `user_Id`
    FOREIGN KEY (`user_id`)
    REFERENCES `shedule`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);

/* Ãğóïïà */
CREATE TABLE `shedule`.`group` (
  `number` TINYINT(3) UNSIGNED NOT NULL,
  `course` TINYINT(1) UNSIGNED NOT NULL,
  `department_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`number`, `course`),
  INDEX `department_id_idx` (`department_id` ASC) VISIBLE,
  CONSTRAINT `department_id`
    FOREIGN KEY (`department_id`)
    REFERENCES `shedule`.`dapartment` (`id`)
    ON DELETE RESTRICT
    ON UPDATE NO ACTION);

/* Ñòóäåíò */
CREATE TABLE `shedule`.`student` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` INT UNSIGNED NOT NULL,
  `number_group` TINYINT(3) UNSIGNED NOT NULL,
  `course` TINYINT(1) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  INDEX `group_idx` (`number_group` ASC, `course` ASC) VISIBLE,
  CONSTRAINT `user_id1`
    FOREIGN KEY (`user_id`)
    REFERENCES `shedule`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `group`
    FOREIGN KEY (`number_group` , `course`)
    REFERENCES `shedule`.`group` (`number` , `course`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

/* Ïîäãğóïïà */
CREATE TABLE `shedule`.`subgroup` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `number` TINYINT(1) UNSIGNED NOT NULL,
  `number_group` TINYINT(3) UNSIGNED NOT NULL,
  `course` TINYINT(1) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `subgroup_in_group_idx` (`number_group` ASC, `course` ASC) VISIBLE,
  CONSTRAINT `subgroup_in_group`
    FOREIGN KEY (`number_group` , `course`)
    REFERENCES `shedule`.`group` (`number` , `course`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

/* Ïğåïîäàâàòåëü */
CREATE TABLE `shedule`.`teacher` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `FIO` NVARCHAR(100) NOT NULL,
  `user_id` INT UNSIGNED NOT NULL,
  `department_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `user_id2_idx` (`user_id` ASC) VISIBLE,
  INDEX `department_id1_idx` (`department_id` ASC) VISIBLE,
  CONSTRAINT `user_id2`
    FOREIGN KEY (`user_id`)
    REFERENCES `shedule`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `department_id1`
    FOREIGN KEY (`department_id`)
    REFERENCES `shedule`.`dapartment` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

/* Àóäèòîğèÿ */
CREATE TABLE `shedule`.`auditorium` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `number` SMALLINT(4) UNSIGNED NOT NULL,
  `dormitory` NVARCHAR(4) NOT NULL,
  `character` NVARCHAR(1) NULL,
  PRIMARY KEY (`id`));

/* Ïğåäìåò */
CREATE TABLE `shedule`.`subject` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));

/* Ïàğà */
CREATE TABLE `shedule`.`couple` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `time` TIME NOT NULL,
  `type` ENUM('lecture', 'seminar', 'laboratory') NOT NULL,
  `subject_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `subject_id_idx` (`subject_id` ASC) VISIBLE,
  CONSTRAINT `subject_id`
    FOREIGN KEY (`subject_id`)
    REFERENCES `shedule`.`subject` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

/* Ïğîõîäèò */
CREATE TABLE `shedule`.`istakingplace` (
  `subgroup_id` INT UNSIGNED NOT NULL,
  `couple_id` INT UNSIGNED NOT NULL,
  `teacher_id` INT UNSIGNED NOT NULL,
  `auditorium_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`subgroup_id`, `couple_id`, `teacher_id`, `auditorium_id`),
  INDEX `teacher_id_idx` (`teacher_id` ASC) VISIBLE,
  INDEX `couple_id_idx` (`couple_id` ASC) VISIBLE,
  INDEX `auditorium_id_idx` (`auditorium_id` ASC) VISIBLE,
  CONSTRAINT `subgroup_id`
    FOREIGN KEY (`subgroup_id`)
    REFERENCES `shedule`.`subgroup` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `teacher_id`
    FOREIGN KEY (`teacher_id`)
    REFERENCES `shedule`.`teacher` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `couple_id`
    FOREIGN KEY (`couple_id`)
    REFERENCES `shedule`.`couple` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `auditorium_id`
    FOREIGN KEY (`auditorium_id`)
    REFERENCES `shedule`.`auditorium` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

/*Äîáàâëåíèå àòğèáóòîâ äëÿ òàáëèöû Ïîëüçîâàòåëÿ */
ALTER TABLE `shedule`.`user` 
ADD COLUMN `delay_notify` INT UNSIGNED NOT NULL DEFAULT 60 AFTER `id`,
ADD COLUMN `need_notify` TINYINT NOT NULL DEFAULT 0 AFTER `delay_notify`;
