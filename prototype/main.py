from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from DBClass import DBClass
from mainwindow import Ui_MainWindow
import sys
import datetime


class mywindow(QtWidgets.QMainWindow):
    isEdit = False

    def __init__(self, database: DBClass):

        # ---------- Init ----------------------------------------------------------------------------------------------
        super(mywindow, self).__init__()
        self.__db = database
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sl_updSubjectList()
        self.loadAllSchedule()
        self.loadTeacher_Analytic()
        self.ui.dateTimeEdit_FreeAuditorium.setDateTime(datetime.datetime.now())

        # ========== Connect ===========================================================================================
        # ---------- couple --------------------------------------------------------------------------------------------
        self.ui.btn_upd.clicked.connect(self.sl_updSubjectList)
        self.ui.btn_save.clicked.connect(self.sl_saveSubject)
        self.ui.btn_del.clicked.connect(self.sl_deleteSubject)
        self.ui.listWidget_subject.itemDoubleClicked.connect(self.sl_changeSubject)
        # ---------- Schedule ------------------------------------------------------------------------------------------
        self.ui.cb_timeCouple.currentIndexChanged.connect(self.sl_changeTimeCouple)
        self.ui.cb_numCourse.currentIndexChanged.connect(self.sl_changeNumCourse)
        self.ui.cb_numGroup.currentIndexChanged.connect(self.sl_changeNumGroup)
        self.ui.cb_nameCouple.currentIndexChanged.connect(self.sl_changeNameCouple)
        self.ui.cb_dormitory.currentIndexChanged.connect(self.sl_changeDormitory)
        self.ui.cb_auditorium.currentIndexChanged.connect(self.sl_changeAuditorium)
        self.ui.btn_addSchedule.clicked.connect(self.sl_addSchedule)
        self.ui.btn_cancelSchedule.clicked.connect(self.sl_cancelSchedule)
        self.ui.btn_saveSchedule.clicked.connect(self.sl_saveSchedule)
        self.ui.btn_refreshShedule.clicked.connect(self.sl_refreshSchedule)
        # ---------- Analytic ------------------------------------------------------------------------------------------
        self.ui.btn_calcAvg.clicked.connect(self.sl_calcAvgCoupleTeacher)
        self.ui.btn_getFreeAuditorium.clicked.connect(self.sl_getFreeAuditorium)

    # ========== SLOT ==================================================================================================
    # ---------- couple ------------------------------------------------------------------------------------------------

    def sl_updSubjectList(self):
        """
        Обновляет лист виджет новыми данными из бд
        """
        self.ui.listWidget_subject.clear()
        data = self.__db.getListSubject()
        for i in data:
            item_to_add = QtWidgets.QListWidgetItem()
            item_to_add.setText(i[1])
            item_to_add.setData(QtCore.Qt.UserRole, i[0])
            self.ui.listWidget_subject.addItem(item_to_add)

    def sl_saveSubject(self):
        """
        В зависимости от состояния добавляет предмет в бд или обновляет название предмета
        Название берется из lineEdit
        """
        name = self.ui.lineEdit_subject.text()
        if self.isEdit:
            self.editSubject(name)
        else:
            self.saveSubject(name)
        self.ui.lineEdit_subject.clear()
        self.unCheckedType()
        self.sl_updSubjectList()

    def sl_deleteSubject(self):
        """
        Удаляет выделенный предмет из бд
        """
        name = self.ui.listWidget_subject.currentItem().text()
        subject_id = self.ui.listWidget_subject.currentItem().data(QtCore.Qt.UserRole)
        if len(name) != 0:
            self.__db.delCouple(subject_id)
            self.__db.delSubject(name)
            self.sl_updSubjectList()

    def sl_changeSubject(self, new_item: QtWidgets.QListWidgetItem):
        """
        Слот для смены предмета в listWidget. Вызывается при двойном нажатии на предмет
        :param new_item:
        """
        if new_item is not None:
            self.ui.lineEdit_subject.setText(new_item.text())
            self.isEdit = True
            self.ui.btn_save.setText("Применить")
            self.ui.listWidget_subject.setDisabled(True)
            self.loadType(self.ui.listWidget_subject.currentItem().data(QtCore.Qt.UserRole))

    # ---------- Schedule ----------------------------------------------------------------------------------------------
    def sl_changeTimeCouple(self, num):
        data = self.ui.cb_timeCouple.currentData(QtCore.Qt.UserRole)
        if data is not None:
            self.ui.label_startCouple.setText("Начало: " + str(data[0]))
            self.ui.label_endCouple.setText("Конец: " + str(data[1]))

    def sl_changeNumCourse(self, num):
        self.loadGroup()

    def sl_changeNumGroup(self, num):
        self.loadSubgroup()

    def sl_changeNameCouple(self, num):
        self.loadTypeCouple()

    def sl_changeDormitory(self, num):
        self.loadAuditorium()

    def sl_changeAuditorium(self, num):
        self.loadCharacter()

    def sl_addSchedule(self):
        self.ui.tableWidget_Schedule.setDisabled(True)
        self.ui.groupBox_CreateSchedule.setEnabled(True)
        self.ui.btn_addSchedule.setDisabled(True)
        self.loadTimeCouple()
        self.loadNumCourse()
        self.loadNameCouple()
        self.loadTeacher()
        self.loadDormitory()

    def sl_cancelSchedule(self):
        self.ui.tableWidget_Schedule.setDisabled(False)
        self.ui.groupBox_CreateSchedule.setEnabled(False)
        self.ui.btn_addSchedule.setDisabled(False)

    def sl_saveSchedule(self):
        self.sl_cancelSchedule()
        date = self.ui.dateEdit_dateCouple.date().toString("yyyyMMdd")
        num_couple = self.ui.cb_timeCouple.currentText()
        subgroup_id = self.ui.cb_numSubgroup.currentData(Qt.Qt.UserRole)
        couple_id = self.ui.cb_typeCouple.currentData(Qt.Qt.UserRole)
        teacher_id = self.ui.cb_nameTeacher.currentData(Qt.Qt.UserRole)
        auditorium_id = self.ui.cb_characher.currentData(Qt.Qt.UserRole)
        self.__db.addSchedule(date, num_couple, subgroup_id, couple_id, teacher_id, auditorium_id)
        self.loadAllSchedule()

    def sl_refreshSchedule(self):
        self.loadAllSchedule()

    # ---------- Analytic ----------------------------------------------------------------------------------------------

    def sl_calcAvgCoupleTeacher(self):
        FIO = self.ui.cb_teacher.currentText()
        date = self.ui.dateEdit_firstDate.date().toString("yyyyMMdd")
        res = self.__db.calcAvgCoupleAtTeacher(FIO, date)[0][0]
        if res is None:
            res = "N/A"
        self.ui.lineEdit_result1.setText(str(res))

    def sl_getFreeAuditorium(self):
        self.ui.tableWidget_FreeAuditorium.clear()
        row = 0
        date = self.ui.dateTimeEdit_FreeAuditorium.date().toString("yyyyMMdd")
        time = self.ui.dateTimeEdit_FreeAuditorium.time().toString("HHmmss")
        res = self.__db.calcGetFreeAuditorium(date, time)
        self.ui.tableWidget_FreeAuditorium.setRowCount(len(res))
        self.ui.tableWidget_FreeAuditorium.setColumnCount(3)
        self.ui.tableWidget_FreeAuditorium.setHorizontalHeaderLabels(["Корпус", "Номер аудитории", "Литера аудитории"])
        for i in res:
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i[0]))
            self.ui.tableWidget_FreeAuditorium.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i[1]))
            self.ui.tableWidget_FreeAuditorium.setItem(row, 1, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i[2]))
            self.ui.tableWidget_FreeAuditorium.setItem(row, 2, item)
            row += 1
        self.ui.tableWidget_FreeAuditorium.resizeColumnsToContents()

    # ========== Operation =============================================================================================

    def loadType(self, subject_id):
        type = self.__db.getTypeCoupleById(subject_id)

        self.unCheckedType()

        for i in type:
            if i[1] == "lecture":
                self.ui.cb_lecture.setChecked(True)
            if i[1] == "seminar":
                self.ui.cb_seminar.setChecked(True)
            if i[1] == "laboratory":
                self.ui.cb_laboratory.setChecked(True)

    def updateType(self, subject_id):
        type = [i[1] for i in self.__db.getTypeCoupleById(subject_id)]

        # seminar
        if self.ui.cb_seminar.isChecked():
            try:
                type.index("seminar")
            except ValueError:
                self.__db.addCouple(subject_id, "seminar")
        else:
            try:
                type.index("seminar")
                self.__db.delCouple(subject_id, "seminar")
            except ValueError:
                pass

        # lecture
        if self.ui.cb_lecture.isChecked():
            try:
                type.index("lecture")
            except ValueError:
                self.__db.addCouple(subject_id, "lecture")
        else:
            try:
                type.index("lecture")
                self.__db.delCouple(subject_id, "lecture")
            except ValueError:
                pass

        # laboratory
        if self.ui.cb_laboratory.isChecked():
            try:
                type.index("laboratory")
            except ValueError:
                self.__db.addCouple(subject_id, "laboratory")
        else:
            try:
                type.index("laboratory")
                self.__db.delCouple(subject_id, "laboratory")
            except ValueError:
                pass

    def saveSubject(self, name):
        find = self.ui.listWidget_subject.findItems(name, Qt.Qt.MatchCaseSensitive)
        if len(find) == 0:
            id = self.__db.addSubject(name)
            self.updateType(id)

    def editSubject(self, name):

        self.isEdit = False
        self.ui.btn_save.setText("Добавить")
        self.ui.listWidget_subject.setEnabled(True)

        self.__db.updSubject(self.ui.listWidget_subject.currentItem().text(), name)
        self.updateType(self.ui.listWidget_subject.currentItem().data(QtCore.Qt.UserRole))

    def unCheckedType(self):
        self.ui.cb_lecture.setChecked(False)
        self.ui.cb_seminar.setChecked(False)
        self.ui.cb_laboratory.setChecked(False)

    def loadAllSchedule(self):
        self.ui.tableWidget_Schedule.clear()
        row = 0
        res = database.getAllSchedule()
        self.ui.tableWidget_Schedule.setRowCount(len(res))
        self.ui.tableWidget_Schedule.setColumnCount(12)
        self.ui.tableWidget_Schedule.setHorizontalHeaderLabels(["Дата", "Время начала", "Время окончания",
                                                                "Курс", "Номер группы", "Номер подгруппы",
                                                                "Название предмета",
                                                                "Тип предмета", "ФИО преподавателя", "Корпус",
                                                                "Номер аудитории", "Литера аудитории"])
        for i in res:
            # insert data
            item = QtWidgets.QTableWidgetItem()
            item.setText(i[0].strftime("%Y-%m-%d"))
            self.ui.tableWidget_Schedule.setItem(row, 0, item)
            # insert time_start
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i[1]))  # item.setText(i[1].strftime("%X"))
            self.ui.tableWidget_Schedule.setItem(row, 1, item)
            # insert time_end
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i[2]))
            self.ui.tableWidget_Schedule.setItem(row, 2, item)
            # insert course
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i[3]))
            self.ui.tableWidget_Schedule.setItem(row, 3, item)
            # insert group
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i[4]))
            self.ui.tableWidget_Schedule.setItem(row, 4, item)
            # insert subgroup
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i[5]))
            self.ui.tableWidget_Schedule.setItem(row, 5, item)
            # insert name
            item = QtWidgets.QTableWidgetItem()
            item.setText(i[6])
            self.ui.tableWidget_Schedule.setItem(row, 6, item)
            # insert type
            item = QtWidgets.QTableWidgetItem()
            item.setText(i[7])
            self.ui.tableWidget_Schedule.setItem(row, 7, item)
            # insert FIO
            item = QtWidgets.QTableWidgetItem()
            item.setText(i[8])
            self.ui.tableWidget_Schedule.setItem(row, 8, item)
            # insert dormitory
            item = QtWidgets.QTableWidgetItem()
            item.setText(i[9])
            self.ui.tableWidget_Schedule.setItem(row, 9, item)
            # insert number auditorium
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i[10]))
            self.ui.tableWidget_Schedule.setItem(row, 10, item)
            # insert characher
            item = QtWidgets.QTableWidgetItem()
            item.setText(i[11])
            self.ui.tableWidget_Schedule.setItem(row, 11, item)
            row += 1
        self.ui.tableWidget_Schedule.resizeColumnsToContents()

    def loadTeacher_Analytic(self):
        self.ui.cb_teacher.clear()
        res = self.__db.getListTeacher()
        for i in res:
            self.ui.cb_teacher.addItem(i[1], i[0])

    def loadTimeCouple(self):
        self.ui.cb_timeCouple.clear()
        res = self.__db.getListTimeCouple()
        for i in res:
            self.ui.cb_timeCouple.addItem(str(i[0]), (i[1], i[2]))

    def loadNumCourse(self):
        self.ui.cb_numCourse.clear()
        res = self.__db.getListNumCouple()
        for i in res:
            self.ui.cb_numCourse.addItem(str(i[0]))

    def loadGroup(self):
        self.ui.cb_numGroup.clear()
        res = self.__db.getListGroup(self.ui.cb_numCourse.currentText())
        for i in res:
            self.ui.cb_numGroup.addItem(str(i[0]))

    def loadSubgroup(self):
        self.ui.cb_numSubgroup.clear()
        res = self.__db.getListSubgroup(self.ui.cb_numCourse.currentText(), self.ui.cb_numGroup.currentText())
        for i in res:
            self.ui.cb_numSubgroup.addItem(str(i[1]), i[0])

    def loadTeacher(self):
        self.ui.cb_nameTeacher.clear()
        res = self.__db.getListTeacher()
        for i in res:
            self.ui.cb_nameTeacher.addItem(i[1], i[0])

    def loadNameCouple(self):
        self.ui.cb_nameCouple.clear()
        res = self.__db.getListSubject()
        for i in res:
            self.ui.cb_nameCouple.addItem(i[1], i[0])

    def loadTypeCouple(self):
        self.ui.cb_typeCouple.clear()
        res = self.__db.getTypeCoupleById(self.ui.cb_nameCouple.currentData(Qt.Qt.UserRole))
        for i in res:
            self.ui.cb_typeCouple.addItem(i[1], i[0])

    def loadDormitory(self):
        self.ui.cb_dormitory.clear()
        res = self.__db.getListDormitory()
        for i in res:
            self.ui.cb_dormitory.addItem(i[0])

    def loadAuditorium(self):
        self.ui.cb_auditorium.clear()
        res = self.__db.getListAuditorium(self.ui.cb_dormitory.currentText())
        for i in res:
            self.ui.cb_auditorium.addItem(str(i[0]))

    def loadCharacter(self):
        self.ui.cb_characher.clear()
        res = self.__db.getListCharacter(self.ui.cb_dormitory.currentText(), self.ui.cb_auditorium.currentText())
        for i in res:
            text = i[1]
            id = i[0]
            if text is None:
                text = "-"
            self.ui.cb_characher.addItem(str(text), id)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    database = DBClass("env.json")
    application = mywindow(database)
    application.show()
    sys.exit(app.exec())
