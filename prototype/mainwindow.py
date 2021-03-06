# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1356, 731)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_subject = QtWidgets.QWidget()
        self.tab_subject.setObjectName("tab_subject")
        self.listWidget_subject = QtWidgets.QListWidget(self.tab_subject)
        self.listWidget_subject.setGeometry(QtCore.QRect(390, 50, 256, 192))
        self.listWidget_subject.setObjectName("listWidget_subject")
        self.label = QtWidgets.QLabel(self.tab_subject)
        self.label.setGeometry(QtCore.QRect(390, 20, 94, 13))
        self.label.setObjectName("label")
        self.btn_save = QtWidgets.QPushButton(self.tab_subject)
        self.btn_save.setGeometry(QtCore.QRect(250, 90, 75, 23))
        self.btn_save.setObjectName("btn_save")
        self.btn_del = QtWidgets.QPushButton(self.tab_subject)
        self.btn_del.setGeometry(QtCore.QRect(480, 260, 75, 23))
        self.btn_del.setObjectName("btn_del")
        self.label_2 = QtWidgets.QLabel(self.tab_subject)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 48, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit_subject = QtWidgets.QLineEdit(self.tab_subject)
        self.lineEdit_subject.setGeometry(QtCore.QRect(30, 60, 291, 20))
        self.lineEdit_subject.setObjectName("lineEdit_subject")
        self.btn_upd = QtWidgets.QPushButton(self.tab_subject)
        self.btn_upd.setGeometry(QtCore.QRect(570, 20, 75, 23))
        self.btn_upd.setObjectName("btn_upd")
        self.groupBox_Type = QtWidgets.QGroupBox(self.tab_subject)
        self.groupBox_Type.setGeometry(QtCore.QRect(30, 90, 116, 125))
        self.groupBox_Type.setObjectName("groupBox_Type")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_Type)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_lecture = QtWidgets.QCheckBox(self.groupBox_Type)
        self.cb_lecture.setObjectName("cb_lecture")
        self.verticalLayout.addWidget(self.cb_lecture)
        self.cb_seminar = QtWidgets.QCheckBox(self.groupBox_Type)
        self.cb_seminar.setObjectName("cb_seminar")
        self.verticalLayout.addWidget(self.cb_seminar)
        self.cb_laboratory = QtWidgets.QCheckBox(self.groupBox_Type)
        self.cb_laboratory.setObjectName("cb_laboratory")
        self.verticalLayout.addWidget(self.cb_laboratory)
        self.tabWidget.addTab(self.tab_subject, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_Schedule = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_Schedule.setGeometry(QtCore.QRect(9, 9, 1271, 221))
        self.tableWidget_Schedule.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_Schedule.setObjectName("tableWidget_Schedule")
        self.tableWidget_Schedule.setColumnCount(12)
        self.tableWidget_Schedule.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Schedule.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Schedule.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Schedule.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Schedule.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Schedule.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Schedule.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Schedule.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Schedule.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Schedule.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Schedule.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Schedule.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Schedule.setHorizontalHeaderItem(11, item)
        self.tableWidget_Schedule.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Schedule.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_Schedule.verticalHeader().setDefaultSectionSize(40)
        self.btn_refreshShedule = QtWidgets.QPushButton(self.tab_3)
        self.btn_refreshShedule.setGeometry(QtCore.QRect(1200, 240, 75, 23))
        self.btn_refreshShedule.setObjectName("btn_refreshShedule")
        self.btn_addSchedule = QtWidgets.QPushButton(self.tab_3)
        self.btn_addSchedule.setGeometry(QtCore.QRect(10, 240, 75, 23))
        self.btn_addSchedule.setObjectName("btn_addSchedule")
        self.groupBox_CreateSchedule = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_CreateSchedule.setEnabled(False)
        self.groupBox_CreateSchedule.setGeometry(QtCore.QRect(10, 280, 731, 281))
        self.groupBox_CreateSchedule.setObjectName("groupBox_CreateSchedule")
        self.label_6 = QtWidgets.QLabel(self.groupBox_CreateSchedule)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 90, 13))
        self.label_6.setObjectName("label_6")
        self.cb_nameCouple = QtWidgets.QComboBox(self.groupBox_CreateSchedule)
        self.cb_nameCouple.setGeometry(QtCore.QRect(10, 170, 150, 20))
        self.cb_nameCouple.setObjectName("cb_nameCouple")
        self.cb_nameCouple.addItem("")
        self.label_10 = QtWidgets.QLabel(self.groupBox_CreateSchedule)
        self.label_10.setGeometry(QtCore.QRect(610, 40, 90, 13))
        self.label_10.setObjectName("label_10")
        self.cb_numGroup = QtWidgets.QComboBox(self.groupBox_CreateSchedule)
        self.cb_numGroup.setGeometry(QtCore.QRect(500, 70, 69, 22))
        self.cb_numGroup.setObjectName("cb_numGroup")
        self.label_7 = QtWidgets.QLabel(self.groupBox_CreateSchedule)
        self.label_7.setGeometry(QtCore.QRect(150, 40, 60, 13))
        self.label_7.setObjectName("label_7")
        self.cb_numCourse = QtWidgets.QComboBox(self.groupBox_CreateSchedule)
        self.cb_numCourse.setGeometry(QtCore.QRect(390, 70, 69, 22))
        self.cb_numCourse.setObjectName("cb_numCourse")
        self.label_endCouple = QtWidgets.QLabel(self.groupBox_CreateSchedule)
        self.label_endCouple.setGeometry(QtCore.QRect(240, 90, 101, 16))
        self.label_endCouple.setObjectName("label_endCouple")
        self.cb_numSubgroup = QtWidgets.QComboBox(self.groupBox_CreateSchedule)
        self.cb_numSubgroup.setGeometry(QtCore.QRect(610, 70, 69, 22))
        self.cb_numSubgroup.setObjectName("cb_numSubgroup")
        self.btn_saveSchedule = QtWidgets.QPushButton(self.groupBox_CreateSchedule)
        self.btn_saveSchedule.setGeometry(QtCore.QRect(640, 240, 75, 23))
        self.btn_saveSchedule.setObjectName("btn_saveSchedule")
        self.label_13 = QtWidgets.QLabel(self.groupBox_CreateSchedule)
        self.label_13.setGeometry(QtCore.QRect(10, 210, 80, 13))
        self.label_13.setObjectName("label_13")
        self.cb_typeCouple = QtWidgets.QComboBox(self.groupBox_CreateSchedule)
        self.cb_typeCouple.setGeometry(QtCore.QRect(180, 170, 91, 22))
        self.cb_typeCouple.setObjectName("cb_typeCouple")
        self.label_9 = QtWidgets.QLabel(self.groupBox_CreateSchedule)
        self.label_9.setGeometry(QtCore.QRect(500, 40, 71, 13))
        self.label_9.setObjectName("label_9")
        self.label_startCouple = QtWidgets.QLabel(self.groupBox_CreateSchedule)
        self.label_startCouple.setGeometry(QtCore.QRect(240, 50, 101, 16))
        self.label_startCouple.setObjectName("label_startCouple")
        self.cb_nameTeacher = QtWidgets.QComboBox(self.groupBox_CreateSchedule)
        self.cb_nameTeacher.setGeometry(QtCore.QRect(10, 240, 241, 22))
        self.cb_nameTeacher.setObjectName("cb_nameTeacher")
        self.dateEdit_dateCouple = QtWidgets.QDateEdit(self.groupBox_CreateSchedule)
        self.dateEdit_dateCouple.setGeometry(QtCore.QRect(10, 70, 110, 22))
        self.dateEdit_dateCouple.setObjectName("dateEdit_dateCouple")
        self.cb_timeCouple = QtWidgets.QComboBox(self.groupBox_CreateSchedule)
        self.cb_timeCouple.setGeometry(QtCore.QRect(150, 70, 69, 22))
        self.cb_timeCouple.setObjectName("cb_timeCouple")
        self.label_12 = QtWidgets.QLabel(self.groupBox_CreateSchedule)
        self.label_12.setGeometry(QtCore.QRect(180, 140, 70, 13))
        self.label_12.setObjectName("label_12")
        self.label_8 = QtWidgets.QLabel(self.groupBox_CreateSchedule)
        self.label_8.setGeometry(QtCore.QRect(390, 40, 63, 13))
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.groupBox_CreateSchedule)
        self.label_11.setGeometry(QtCore.QRect(10, 140, 100, 13))
        self.label_11.setObjectName("label_11")
        self.cb_dormitory = QtWidgets.QComboBox(self.groupBox_CreateSchedule)
        self.cb_dormitory.setGeometry(QtCore.QRect(390, 160, 69, 22))
        self.cb_dormitory.setObjectName("cb_dormitory")
        self.label_14 = QtWidgets.QLabel(self.groupBox_CreateSchedule)
        self.label_14.setGeometry(QtCore.QRect(390, 130, 47, 13))
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.groupBox_CreateSchedule)
        self.label_16.setGeometry(QtCore.QRect(590, 130, 47, 13))
        self.label_16.setObjectName("label_16")
        self.label_15 = QtWidgets.QLabel(self.groupBox_CreateSchedule)
        self.label_15.setGeometry(QtCore.QRect(490, 130, 56, 13))
        self.label_15.setObjectName("label_15")
        self.cb_characher = QtWidgets.QComboBox(self.groupBox_CreateSchedule)
        self.cb_characher.setGeometry(QtCore.QRect(590, 160, 69, 22))
        self.cb_characher.setObjectName("cb_characher")
        self.cb_auditorium = QtWidgets.QComboBox(self.groupBox_CreateSchedule)
        self.cb_auditorium.setGeometry(QtCore.QRect(490, 160, 69, 22))
        self.cb_auditorium.setObjectName("cb_auditorium")
        self.btn_cancelSchedule = QtWidgets.QPushButton(self.groupBox_CreateSchedule)
        self.btn_cancelSchedule.setGeometry(QtCore.QRect(540, 240, 75, 23))
        self.btn_cancelSchedule.setObjectName("btn_cancelSchedule")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 561, 151))
        self.groupBox.setObjectName("groupBox")
        self.cb_teacher = QtWidgets.QComboBox(self.groupBox)
        self.cb_teacher.setGeometry(QtCore.QRect(40, 50, 231, 21))
        self.cb_teacher.setObjectName("cb_teacher")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 80, 13))
        self.label_3.setObjectName("label_3")
        self.dateEdit_firstDate = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit_firstDate.setGeometry(QtCore.QRect(310, 50, 110, 22))
        self.dateEdit_firstDate.setObjectName("dateEdit_firstDate")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(310, 30, 107, 13))
        self.label_4.setObjectName("label_4")
        self.lineEdit_result1 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_result1.setGeometry(QtCore.QRect(460, 50, 71, 20))
        self.lineEdit_result1.setReadOnly(True)
        self.lineEdit_result1.setObjectName("lineEdit_result1")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(460, 30, 53, 13))
        self.label_5.setObjectName("label_5")
        self.btn_calcAvg = QtWidgets.QPushButton(self.groupBox)
        self.btn_calcAvg.setGeometry(QtCore.QRect(460, 100, 75, 23))
        self.btn_calcAvg.setObjectName("btn_calcAvg")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 210, 571, 301))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget_FreeAuditorium = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_FreeAuditorium.setGeometry(QtCore.QRect(40, 80, 501, 192))
        self.tableWidget_FreeAuditorium.setObjectName("tableWidget_FreeAuditorium")
        self.tableWidget_FreeAuditorium.setColumnCount(0)
        self.tableWidget_FreeAuditorium.setRowCount(0)
        self.dateTimeEdit_FreeAuditorium = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.dateTimeEdit_FreeAuditorium.setGeometry(QtCore.QRect(40, 40, 194, 22))
        self.dateTimeEdit_FreeAuditorium.setCalendarPopup(True)
        self.dateTimeEdit_FreeAuditorium.setObjectName("dateTimeEdit_FreeAuditorium")
        self.btn_getFreeAuditorium = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_getFreeAuditorium.setGeometry(QtCore.QRect(460, 40, 75, 23))
        self.btn_getFreeAuditorium.setObjectName("btn_getFreeAuditorium")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1356, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Список предметов"))
        self.btn_save.setText(_translate("MainWindow", "Добавить"))
        self.btn_del.setText(_translate("MainWindow", "Удалить"))
        self.label_2.setText(_translate("MainWindow", "Название"))
        self.btn_upd.setText(_translate("MainWindow", "Обновить"))
        self.groupBox_Type.setTitle(_translate("MainWindow", "Тип предмета"))
        self.cb_lecture.setText(_translate("MainWindow", "Лекция"))
        self.cb_seminar.setText(_translate("MainWindow", "Семинар"))
        self.cb_laboratory.setText(_translate("MainWindow", "Лабораторная"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_subject), _translate("MainWindow", "Предметы"))
        self.tableWidget_Schedule.setSortingEnabled(True)
        item = self.tableWidget_Schedule.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.tableWidget_Schedule.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Время начала"))
        item = self.tableWidget_Schedule.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Время окончания"))
        item = self.tableWidget_Schedule.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Курс"))
        item = self.tableWidget_Schedule.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Номер группы"))
        item = self.tableWidget_Schedule.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Номер подгруппы"))
        item = self.tableWidget_Schedule.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Название предмета"))
        item = self.tableWidget_Schedule.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Тип предмета"))
        item = self.tableWidget_Schedule.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "ФИО преподавателя"))
        item = self.tableWidget_Schedule.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Корпус"))
        item = self.tableWidget_Schedule.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Номер аудитории"))
        item = self.tableWidget_Schedule.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Литера аудитории"))
        self.btn_refreshShedule.setText(_translate("MainWindow", "Обновить"))
        self.btn_addSchedule.setText(_translate("MainWindow", "Добавить"))
        self.groupBox_CreateSchedule.setTitle(_translate("MainWindow", "Создание"))
        self.label_6.setText(_translate("MainWindow", "Дата проведения"))
        self.cb_nameCouple.setItemText(0, _translate("MainWindow", "Дискретная математика"))
        self.label_10.setText(_translate("MainWindow", "Номер подгруппы"))
        self.label_7.setText(_translate("MainWindow", "Номер пары"))
        self.label_endCouple.setText(_translate("MainWindow", "Конец: "))
        self.btn_saveSchedule.setText(_translate("MainWindow", "Применить"))
        self.label_13.setText(_translate("MainWindow", "Преподаватель"))
        self.label_9.setText(_translate("MainWindow", "Номер группы"))
        self.label_startCouple.setText(_translate("MainWindow", "Начало: "))
        self.label_12.setText(_translate("MainWindow", "Тип предмета"))
        self.label_8.setText(_translate("MainWindow", "Номер курса"))
        self.label_11.setText(_translate("MainWindow", "Название предмета"))
        self.label_14.setText(_translate("MainWindow", "Корпус"))
        self.label_16.setText(_translate("MainWindow", "Литера"))
        self.label_15.setText(_translate("MainWindow", "Аудитория"))
        self.btn_cancelSchedule.setText(_translate("MainWindow", "Отмена"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Расписание"))
        self.groupBox.setTitle(_translate("MainWindow", "Среднее количество пар у преподавателя"))
        self.label_3.setText(_translate("MainWindow", "Преподаватель"))
        self.label_4.setText(_translate("MainWindow", "Первый день недели"))
        self.label_5.setText(_translate("MainWindow", "Результат"))
        self.btn_calcAvg.setText(_translate("MainWindow", "Рассчитать"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Показать свободные аудитории"))
        self.tableWidget_FreeAuditorium.setSortingEnabled(True)
        self.btn_getFreeAuditorium.setText(_translate("MainWindow", "Показать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Аналитические запросы"))
