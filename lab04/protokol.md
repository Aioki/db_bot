# Лабораторная работа 4

## Скриншот базы данных
![](pic/db.png)
## Собственные запросы

### Транзакционные
1. Добавить себя в студента/преподавателя

*Вставляем данные в таблицу*

```mysql
INSERT INTO student(user_id,subgroup_id) VALUE(95824080,6);
```

![](pic/1.png)

2. *Добавляем преподавателю* *user**_**id*

```mysql
UPDATE `teacher` SET `user_id` = '95824080' WHERE (`FIO` = 'Литовкин Дмитрий Васильевич');
```

![](pic/2.png)

3. Удалить себя из студента/преподавателя:

   *Удаляем* *user_id*

   ```mysql
   DELETE FROM `student` WHERE (`user_id` = '95824080');
   ```

   ![](pic/3.png)

   

4. Добавить заметку 

   *Добавляем в таблицу заметок значения*

   ```mysql
   INSERT INTO note(context,user_id) VALUE('это',1);
   ```

   ![](pic/4.png)

5. Удалить заметку

   *Удаляем заметку данного пользователя с этим содержимым*

   ```mysql
   DELETE FROM `note` WHERE (`user_id`=1 AND `context`= `это`); 
   ```

   ![](pic/5.png)

6. Выбрать группу и подгруппу

   *Задаем для студента подгруппу по его группе, курсу и номеру подругппы*

   ```mysql
   UPDATE student SET subgroup_id = ( SELECT id FROM subgroup WHERE(number_group = 66 and course = 3 and number = 0)) WHERE (user_id = 95824080);
   
   ```

   ![](pic/6.png)

### Справочные

7. Показать расписание на сегодня/завтра/выбранный день

   *Показать дату, время, тип и название предмета, зная* *user**_**id* *и дату*

   ```mysql
   SELECT `date`,`num_couple`,`type`,`name` as `subject`
   FROM couple 
   JOIN `subject` ON `subject`.`id` = `couple`.`subject_id` 
   JOIN `istakingplace` on `istakingplace`.`couple_id` =`couple`.`id` 
   JOIN `subgroup` on `istakingplace`.`subgroup_id` = `subgroup`.`id`
   JOIN `student` on `student`.`subgroup_id` = `subgroup`.`id`
   WHERE (`user_id`=95824080 AND `date` = "2020-11-20");
   ```

   ![](pic/7.png)

8. Показать расписание другой группы

   *Зная группу и курс, узнаем* *id* *подгруппы*

   ```mysql
   SELECT
      date,num_couple, type, name AS subject
   FROM
       subgroup
   JOIN istakingplace ON istakingplace.subgroup_id = subgroup.id
   JOIN couple ON couple.id = istakingplace.couple_id
   JOIN subject ON subject.id = couple.subject_id
   WHERE number_group = 66 AND course = 3;
   ```

   ![](pic/8.png)

9. Показать расписание преподавателя

   *Достаем по ФИО преподавателя* *id*, и ищем пары среди проводимых, выводим дату, время, тип и название пары*

   ```mysql
   SELECT `date`,`num_couple`,`type`,`name` as `subject`
   FROM couple 
   JOIN `subject` ON `subject`.`id` = `couple`.`subject_id` 
   JOIN `istakingplace` on `istakingplace`.`couple_id` =`couple`.`id` 
   JOIN `teacher` on `istakingplace`.`teacher_id` = `teacher`.`id`
   WHERE (FIO = "Литовкин Дмитрий Васильевич"  AND `date` = "2020-11-02"); 
   ```

   ![](pic/9.png)

10. Показать расписание на неделю
	
	```mysql
	SELECT;
	```

   ### Справочно-расчетные

11. Показать среднее количество пар в день

    *Получаем все пары этого преподавателя, затем считаем количество пар в неделю, складываем и делим на 7*

    ```mysql
    SELECT SUM(`count`)/7.0 as `avg`
    FROM (SELECT COUNT(`name`) as `count`
    	  FROM couple 
    	  JOIN `subject` ON `subject`.`id` = `couple`.`subject_id` 
    	  JOIN `istakingplace` on `istakingplace`.`couple_id` =`couple`.`id` 
    	  JOIN `teacher` on `istakingplace`.`teacher_id` = `teacher`.`id`
    	  WHERE ( FIO = "Литовкин Дмитрий Васильевич" AND `date` BETWEEN 20201028 AND date_add(20201028,INTERVAL 7 DAY))
          GROUP BY `date`) as `count_couple_in_day`;
    ```

    ![](pic/10.png)

12. Показать количество пройденных пар сегодня

    *Из преподавателя достает айди, ищет пары, которые должен вести преподаватель, проверяется дата и время и считается их количество* 

    ```mysql
    SELECT COUNT(*)
    FROM couple 
    JOIN `subject` ON `subject`.`id` = `couple`.`subject_id` 
    JOIN `istakingplace` on `istakingplace`.`couple_id` =`couple`.`id` 
    JOIN `teacher` on `istakingplace`.`teacher_id` = `teacher`.`id`
    JOIN `time_call` on `time_call`.`number` = `istakingplace`.`num_couple`
    WHERE ( FIO = "Литовкин Дмитрий Васильевич"  AND `date`=20201102 /*current_date()*/ AND `time_end`<= 100000 /*current_time()*/);
    ```
    
    ![](pic/11.png)
    
13. Показать количество студентов в группе/кафедре/факультете

    *Получаем группу и курс и считаем количество* 

    ```mysql
    SELECT COUNT(*) as `count` FROM shedule.group WHERE ( (course,number) = (3,63) );
    ```

    ![](pic/12.png)
    
14. Показать все пары по предмету

    *Выбираем предметы, которые совпадают по названию*

    ```mysql
    SELECT date,num_couple,type FROM shedule.couple 
    JOIN subject ON subject.id = couple.subject_id
    JOIN `istakingplace` on `istakingplace`.`couple_id` =`couple`.`id`
    WHERE (`name` = "Базы данных"); 
    ```

    ![](pic/13.png)

15. Показать аудитории, в которых отсутствует пары в заданное время

     *Узнаем, какие пары есть в текущую дату и время, узнаем какие аудитории занимают и исключаем при отображении всех аудиторий*

    ```mysql
    SELECT `number`,`dormitory`,`character` FROM auditorium WHERE (id NOT IN (
    SELECT auditorium_id FROM shedule.istakingplace
    JOIN `time_call` on `time_call`.`number` = `istakingplace`.`num_couple`
    WHERE (date = 20201102 and 090000 between time_start and time_end)));
    ```

    ![](pic/14.png)

## INSERTы для своей БД или БД одногруппника из предыдущей лабораторной работы (10 шт.+)

[Скрипт](https://github.com/Aioki/db_bot/blob/main/add_temp_value.sql)

Скриншоты результатов см предыдущую работу

## UPDATE (с WHERE) (7 шт.), можно условно, например, изменить заранее созданные некорректные данные

1. ```mysql
   UPDATE `teacher` SET `user_id` = NULL WHERE (`id` = '1');
   ```

   ![](pic/upd1.png)

2. 


## DELETE с WHERE (5 шт.), можно условно, например, удалить заранее созданные некорректные данные

## SELECT, DISTINCT, WHERE, AND/OR/NOT, IN, BETWEEN, IS NULL, AS (25 шт.)
1. ```mysql
   select * from time_call;
   ```
   
   ![](pic/select-1.png)

2. ```mysql
   select * from time_call where (090000 between time_start and time_end);
   ```
   
   ![](pic/select-2.png)

3. ```mysql
   select name from department;
   ```
   
   ![](pic/select-3.png)

4. ```mysql
   select * from `group` where (number between 60 and 67);
   ```
   
   ![](pic/select-4.png)

5. ```mysql
   select distinct date from istakingplace;select distinct delay_notify from user;
   ```
   
   ![](pic/select-5.png)

6. ```mysql
   select distinct delay_notify from user;
   ```
   
   ![](pic/select-6.png)

7. ```mysql
   select number,course from `group` where(course >= 3);
   ```
   
   ![](pic/select-7.png)

8. ```mysql
   select dormitory,number,`character` from auditorium where (dormitory = "В");
   ```
   
   ![](pic/select-8.png)

9. ```mysql
   select * from `group` where (number = 66 and course = 3);
   ```
   
   ![](pic/select-9.png)

10. ```mysql
    select id from user where (need_notify = 1 and delay_notify = 60);
    ```
    
    ![](pic/select-10.png)

11. ```mysql
    select id from department where (faculty_id = 6 or faculty_id = 1);
    ```
    
    ![](pic/select-11.png)

12. ```mysql
    select number from time_call where(time_start = 114000 or time_start =115000);
    ```
    
    ![](pic/select-12.png)

13. ```mysql
    select dormitory,number,`character` from auditorium where not dormitory = "В";
    ```
    
    ![](pic/select-13.png)

14. ```mysql
    select * from `group` where not (number = 66 and course = 3);
    ```
    
    ![](pic/select-14.png)

15. ```mysql
    select * from teacher where(user_id is null);
    ```
    
    ![](pic/select-15.png)

16. ```mysql
    select number,dormitory from auditorium where(`character` is null);
    ```
    
    ![](pic/select-16.png)

17. ```mysql
    SELECT `department`.`name` as `depart_name`, `faculty`.`name` as `faculty_name` FROM department 
    JOIN faculty on department.faculty_id = faculty.id;
    ```
    

![](pic/select-17.png)
    
18. ```mysql
    select id as vk_id from user;
    ```
    
    ![](pic/select-18.png)

19. ```mysql
    select FIO from teacher where(department_id in (6,8,9));
    ```
    
    ![](pic/select-19.png)

20. ```mysql
    select id from user where (delay_notify in (60,10,120));
    ```
    
    ![](pic/select-20.png)



## LIKE (5-7 шт.)

## COUNT, MAX, MIN, SUM, AVG (10 шт.)

## GROUP BY, HAVING (7 шт.)

## ORDER BY, ASC|DESC (7 шт. +)


1. ```mysql
   SELECT * FROM `group` ORDER BY `course`;
   ```

   ![](pic/ob1.png)

2. ```mysql
   SELECT * FROM `group` ORDER BY `number` DESC;
   ```

   ![](pic/ob2.png)

3. ```mysql
   SELECT * FROM `auditorium`  ORDER BY `dormitory`,`number`,`character`;
   ```

   ![](pic/ob3.png)

4. ```mysql
   SELECT * FROM department ORDER BY faculty_id;
   ```

   ![](pic/ob4.png)

5. ```mysql
   SELECT * FROM couple ORDER BY `type`;
   ```

   ![](pic/ob5.png)

6. ```mysql
   SELECT * FROM subject ORDER BY `name` DESC;
   ```

   ![](pic/ob6.png)

7. ```mysql
   SELECT * FROM user ORDER BY `delay_notify` DESC;
   ```

   ![](pic/ob7.png)
   
## Вложенные SELECTы (3 шт. +)

1. ```mysql
   SELECT delay_notify FROM user WHERE ( id IN (SELECT `user_id` FROM shedule.student ) AND need_notify = 1);
   ```

   ![](pic/select1.png)

2. ```mysql
   SELECT `type` FROM couple WHERE (subject_id IN (SELECT id FROM subject WHERE(`name` = "Химия")));
   ```

   ![](pic/select2.png)
   
3. ```mysql
   SELECT name FROM department WHERE ( faculty_id in (
       SELECT id FROM faculty WHERE(name = "Электроники и Вычислительной техники")) );
   ```
   
   ![](pic/select3.png)

## SELECT INTO (1-2 шт.), можно в какую-то тестовую, специально созданную таблицу


## INSERT SELECT (1-2 шт.), можно в какую-то тестовую, специально созданную таблицу

## UNION (ALL), EXCEPT, INTERCEPT какой-то из них на выбор (2-3 шт.)

## JOIN (20 шт.): INNER, OUTTER (LEFT, RIGHT, FULL), CROSS, NATURAL, в общем, разных

1. ```mysql
   SELECT;
   ```
   
   ![](pic/join1.png)

2. ```mysql
   SELECT
   ```
   
   ![](pic/join2.png)

3. ```mysql
   SELECT
   ```
   
   ![](pic/join3.png)

4. ```mysql
   SELECT
   ```
   
   ![](pic/join4.png)

5. ```mysql
   SELECT
   ```
   
   ![](pic/join5.png)

6. ```mysql
   SELECT
   ```
   
   ![](pic/join6.png)

7. ```mysql
   SELECT
   ```
   
   ![](pic/join7.png)

8. ```mysql
   SELECT
   ```
   
   ![](pic/join8.png)

9. ```mysql
   SELECT
   ```
   
   ![](pic/join9.png)

10. ```mysql
    SELECT
    ```
    
    ![](pic/join10.png)

11. ```mysql
    SELECT
    ```
    
    ![](pic/join11.png)

12. ```mysql
    SELECT
    ```
    
    ![](pic/join12.png)

13. ```mysql
    SELECT
    ```
    
    ![](pic/join13.png)

14. ```mysql
    SELECT
    ```
    
    ![](pic/join14.png)

15. ```mysql
    SELECT
    ```
    
    ![](pic/join15.png)

16. ```mysql
    SELECT
    ```
    
    ![](pic/join16.png)

17. ```mysql
    SELECT
    ```
    
    ![](pic/join17.png)

18. ```mysql
    SELECT
    ```
    
    ![](pic/join18.png)

19. ```mysql
    SELECT
    ```
    
    ![](pic/join19.png)

20. ```mysql
    SELECT
    ```
    
    ![](pic/join20.png)



## LIMIT (5 шт. +)

1. ```mysql
   SELECT * FROM `group` ORDER BY `course` LIMIT 2;
   ```

   ![](pic/limit1.png)

2. ```mysql
   SELECT * FROM `note` LIMIT 5;
   ```

   ![](pic/limit2.png)

3. ```mysql
   SELECT * FROM `teacher` LIMIT 8;
   ```

   ![](pic/limit3.png)

4. ```mysql
   SELECT * FROM `auditorium`  ORDER BY `dormitory`,`number`,`character` LIMIT 3;
   ```

   ![](pic/limit4.png)

5. ```mysql
   SELECT * FROM couple LIMIT 1;
   ```

   ![](pic/limit5.png)
