USE `eatapp_db`;

INSERT INTO gender(value)
VALUES('male'),
	  ('female'),
	  ('neutral');

INSERT INTO role
VALUES(NULL, 'slave'),
      (NULL, 'master');

INSERT INTO `user`(name,gender,role,login,password)
VALUES('Van',1,2,'leather_man', 'fck!!u'),
	  ('Billy', 1, 1, 'gch','mch');

INSERT INTO interior(value)
VALUES('modern'),
	  ('talking'),
	  ('old');
	  
RENAME TABLE place TO gym;
RENAME TABLE message TO egassem;