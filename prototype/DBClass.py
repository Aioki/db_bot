import mysql.connector
from mysql.connector import Error
import mysql.connector.locales.eng
import json


class DBClass:
    def __init__(self, path_to_config):
        with open(path_to_config, "r") as read_file:
            data = json.load(read_file)
            self.__conn = mysql.connector.connect(**data)
            self.__cursor = self.__conn.cursor()

    def __del__(self):
        self.__conn.close()

    # ========== Subject ===============================================================================================
    def getListSubject(self):
        """

        :return: [0]:id, [1]: name
        """
        self.__cursor.execute("SELECT * FROM subject ORDER BY name")
        return self.__cursor.fetchall()

    def addSubject(self, name: str):
        """

        :return: id
        """
        query = "INSERT INTO subject(name) VALUES(%s)"
        arg = (name,)
        self.__cursor.execute(query, arg)
        id = self.__cursor.getlastrowid()
        self.__conn.commit()
        return id

    def delSubject(self, name):
        query = "DELETE FROM subject WHERE name = %s"
        arg = (name,)
        self.__cursor.execute(query, arg)
        self.__conn.commit()

    def updSubject(self, old_name, new_name):
        query = "UPDATE subject SET name = %s WHERE name = %s "
        arg = (new_name, old_name)
        self.__cursor.execute(query, arg)
        self.__conn.commit()

    # ========= Couple =================================================================================================
    def addCouple(self, subject_id, type):
        query = "INSERT INTO couple(type,subject_id) VALUES(%s,%s)"
        arg = (type, subject_id)
        self.__cursor.execute(query, arg)
        self.__conn.commit()

    def getTypeCoupleById(self, subject_id: int):
        """

        :param subject_id:
        :return: [0] - id, [1] - type
        """
        self.__cursor.execute(
            "SELECT couple.id, type FROM subject JOIN couple on subject_id = subject.id WHERE subject.id = %s",
            (subject_id,))
        return self.__cursor.fetchall()

    def delCouple(self, id, type):
        query = "DELETE FROM couple WHERE subject_id = %s and type = %s"
        arg = (id, type)
        self.__cursor.execute(query, arg)
        self.__conn.commit()

    def delCouple(self, id):
        query = "DELETE FROM couple WHERE subject_id = %s"
        arg = (id,)
        self.__cursor.execute(query, arg)
        self.__conn.commit()

    # ========= Time_call ==============================================================================================
    def getListTimeCouple(self):
        """

        :return: [0] - id, [1] - time_start, [2] - time_end
        """
        self.__cursor.execute("SELECT * from time_call")
        row = self.__cursor.fetchall()
        return row

    # ========= Teacher ================================================================================================
    def getListTeacher(self):
        """

        :rtype: list
        :return: [0] - id, [1] - FIO, [2] - user_id, [3] - depart_id
        """
        self.__cursor.execute("SELECT * FROM teacher ORDER BY FIO")
        return self.__cursor.fetchall()

    # ========= Subgroup ===============================================================================================
    def getListNumCouple(self):
        self.__cursor.execute("SELECT course from subgroup group by course order by course")
        row = self.__cursor.fetchall()
        return row

    def getListGroup(self, course: str):
        self.__cursor.execute("SELECT number_group from subgroup where course = %s order by number_group", (course,))
        row = self.__cursor.fetchall()
        return row

    def getListSubgroup(self, course: str, group: str):
        """

        :param course:
        :param group:
        :return: [0] - id, [1] - number
        """
        self.__cursor.execute(
            "SELECT id, `number` from subgroup where course = %s and number_group = %s order by `number`",
            (course, group))
        row = self.__cursor.fetchall()
        return row

    # ========= Auditorium =============================================================================================
    def getListDormitory(self):
        """

        :return: [0] - dormitory
        """
        query = "SELECT dormitory FROM auditorium group by dormitory order by dormitory"
        self.__cursor.execute(query)
        row = self.__cursor.fetchall()
        return row

    def getListAuditorium(self, dormitory):
        query = "SELECT `number` FROM auditorium WHERE dormitory = %s group by `number` order by `number`"
        arg = (dormitory,)
        self.__cursor.execute(query, arg)
        return self.__cursor.fetchall()

    def getListCharacter(self, dormitory, auditorium):
        query = "SELECT id, `character` FROM auditorium WHERE dormitory = %s and number = %s order by `character`"
        arg = (dormitory, auditorium)
        self.__cursor.execute(query, arg)
        return self.__cursor.fetchall()

    # ========= istakingplace ==========================================================================================

    def addSchedule(self, date, num_couple, subgroup_id, couple_id, teacher_id, auditorium_id):
        query = "INSERT INTO istakingplace(subgroup_id,couple_id,teacher_id,auditorium_id,`date`,num_couple)" \
                " VALUES(%s,%s,%s,%s,%s,%s)"
        arg = (subgroup_id, couple_id, teacher_id, auditorium_id, date, num_couple)
        self.__cursor.execute(query, arg)
        self.__conn.commit()

    # ========== Operation =============================================================================================
    def getAllSchedule(self):
        """
        Получить всё расписание :return: массив с элементами в следующем порядке (дата, время начала, время конца,
        курс,номер групп, название предмета, тип предмета, ФИО преподавателя, корпус, аудитория и литера)
        """
        quere = """SELECT date, time_start, time_end, course, number_group , subgroup.number , subject.name, type, FIO ,dormitory, 
        auditorium.number, `character` FROM shedule.istakingplace JOIN `couple` on `istakingplace`.`couple_id` 
        =`couple`.`id` JOIN subject ON subject.id = couple.subject_id JOIN auditorium on istakingplace.auditorium_id 
        = auditorium.id JOIN `teacher` on `istakingplace`.`teacher_id` = `teacher`.`id` JOIN `time_call` on 
        `time_call`.`number` = `istakingplace`.`num_couple` JOIN subgroup on `istakingplace`.`subgroup_id` = 
        subgroup.id ORDER BY date,time_start """
        self.__cursor.execute(quere)
        return self.__cursor.fetchall()

    def calcAvgCoupleAtTeacher(self, FIO: str, date: str):
        query = """SELECT SUM(`count`)/7.0 as `avg`
        FROM (SELECT COUNT(`name`) as `count`
        FROM couple 
        JOIN `subject` ON `subject`.`id` = `couple`.`subject_id` 
        JOIN `istakingplace` on `istakingplace`.`couple_id` =`couple`.`id` 
        JOIN `teacher` on `istakingplace`.`teacher_id` = `teacher`.`id`
        WHERE ( FIO = %s AND `date` BETWEEN %s AND date_add(%s,INTERVAL 7 DAY))
        GROUP BY `date`) as `count_couple_in_day`"""
        arg = (FIO, date, date)
        self.__cursor.execute(query, arg)
        return self.__cursor.fetchall()

    def calcGetFreeAuditorium(self, date: str, time: str):
        query = """SELECT `dormitory`,`number`,`character` FROM auditorium WHERE (id NOT IN (
        SELECT auditorium_id FROM shedule.istakingplace
        JOIN `time_call` on `time_call`.`number` = `istakingplace`.`num_couple`
        WHERE (date = %s and %s between time_start and time_end)));"""
        arg = (date, time)
        self.__cursor.execute(query, arg)
        return self.__cursor.fetchall()


if __name__ == '__main__':
    database = DBClass("env.json")
    res = database.getListCharacter("В", 902)
    print(res)
