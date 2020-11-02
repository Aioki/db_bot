USE `eatapp_db`;

ALTER TABLE `address` 
ADD COLUMN `town` NVARCHAR(45) NOT NULL AFTER `mail_index`;

ALTER TABLE invitation
CHANGE `massage` `message` NVARCHAR(90) NOT NULL;

ALTER TABLE preferences
MODIFY is_vegan TINYINT NULL,
MODIFY is_sweet_tooth TINYINT NULL,
MODIFY is_raw_food TINYINT NULL;

ALTER TABLE gender
ADD temp INT UNSIGNED NULL AFTER `value`;

ALTER TABLE gender
MODIFY temp TINYINT NOT NULL DEFAULT 0;

ALTER TABLE gender
DROP temp;

/* Не работает, видимо надо изучать подкапотку
ALTER TABLE gender
ADD temp INT UNSIGNED NULL AFTER `value`,
MODIFY temp TINYINT NOT NULL DEFAULT 0,
DROP temp;
*/