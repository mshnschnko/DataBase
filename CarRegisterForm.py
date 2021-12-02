# Form implementation generated from reading ui file 'CarRegisterForm.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import datetime

from PyQt6.QtWidgets import QMessageBox

import bd_main
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CarRegisterForm(object):
    def setupUi(self, CarRegisterForm):
        self.con = bd_main.connect()
        self.mycursor = self.con.cursor()
        CarRegisterForm.setObjectName("CarRegisterForm")
        CarRegisterForm.resize(500, 270)
        self.carIDlabel = QtWidgets.QLabel(CarRegisterForm)
        self.carIDlabel.setGeometry(QtCore.QRect(25, 70, 65, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.carIDlabel.setFont(font)
        self.carIDlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.carIDlabel.setObjectName("carIDlabel")

        self.modelLabel = QtWidgets.QLabel(CarRegisterForm)
        self.modelLabel.setGeometry(QtCore.QRect(25, 170, 65, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.modelLabel.setFont(font)
        self.modelLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.modelLabel.setObjectName("carIDlabel")

        self.modelEdit = QtWidgets.QPlainTextEdit(CarRegisterForm)
        self.modelEdit.setGeometry(QtCore.QRect(100, 169, 120, 27))
        self.modelEdit.setObjectName("modelEdit")
        self.modelEdit.setEnabled(False)

        self.CarRegisterLabel = QtWidgets.QLabel(CarRegisterForm)
        self.CarRegisterLabel.setEnabled(True)
        self.CarRegisterLabel.setGeometry(QtCore.QRect(110, 30, 280, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CarRegisterLabel.setFont(font)
        self.CarRegisterLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.CarRegisterLabel.setAutoFillBackground(False)
        self.CarRegisterLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.CarRegisterLabel.setWordWrap(False)
        self.CarRegisterLabel.setObjectName("CarRegisterLabel")
        self.reasonLabel = QtWidgets.QLabel(CarRegisterForm)
        self.reasonLabel.setGeometry(QtCore.QRect(25, 200, 142, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reasonLabel.setFont(font)
        self.reasonLabel.setObjectName("reasonLabel")
        self.regRadioBtn = QtWidgets.QRadioButton(CarRegisterForm)
        self.regRadioBtn.setGeometry(QtCore.QRect(25, 100, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.regRadioBtn.setFont(font)
        self.regRadioBtn.setEnabled(False)
        self.regRadioBtn.setObjectName("regRadioBtn")
        self.deregRadioBtn = QtWidgets.QRadioButton(CarRegisterForm)
        self.deregRadioBtn.setGeometry(QtCore.QRect(130, 100, 65, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deregRadioBtn.setFont(font)
        self.deregRadioBtn.setEnabled(False)
        self.deregRadioBtn.setObjectName("deregRadioBtn")
        self.carIDEdit = QtWidgets.QPlainTextEdit(CarRegisterForm)
        self.carIDEdit.setGeometry(QtCore.QRect(100, 69, 120, 27))
        self.carIDEdit.setObjectName("carIDEdit")
        self.driverLabel = QtWidgets.QLabel(CarRegisterForm)
        self.driverLabel.setGeometry(QtCore.QRect(25, 130, 65, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.driverLabel.setFont(font)
        self.driverLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.driverLabel.setObjectName("driverLabel")
        #self.comboBoxDriver = QtWidgets.QComboBox(CarRegisterForm)
        #self.comboBoxDriver.setEnabled(False)
        #self.comboBoxDriver.setGeometry(QtCore.QRect(100, 130, 380, 25))
        #self.comboBoxDriver.setObjectName("comboBoxDriver")

        self.driverPlainText = QtWidgets.QPlainTextEdit(CarRegisterForm)
        self.driverPlainText.setEnabled(False)
        self.driverPlainText.setGeometry(QtCore.QRect(100, 130, 380, 25))
        self.driverPlainText.setObjectName("driverPlainText")
        self.ClearName = QtWidgets.QPushButton(CarRegisterForm)
        self.ClearName.setGeometry(QtCore.QRect(456, 129, 27, 27))
        self.ClearName.setObjectName("ClearName")
        self.ClearName.setEnabled(False)

        self.reasonComboBox = QtWidgets.QComboBox(CarRegisterForm)
        self.reasonComboBox.setEnabled(False)
        self.reasonComboBox.setGeometry(QtCore.QRect(180, 200, 75, 22))
        self.reasonComboBox.setObjectName("reasonComboBox")
        self.applyButton = QtWidgets.QPushButton(CarRegisterForm)
        self.applyButton.setGeometry(QtCore.QRect(405, 230, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.applyButton.setFont(font)
        self.applyButton.setEnabled(False)
        self.applyButton.setObjectName("applyButton")
        self.FCSlistWidget = QtWidgets.QListWidget(CarRegisterForm)
        self.FCSlistWidget.setGeometry(QtCore.QRect(100, 155, 356, 90))
        self.FCSlistWidget.setSelectionRectVisible(False)
        self.FCSlistWidget.setObjectName("FCSlistWidget")
        self.FCSlistWidget.setVisible(False)

        self.retranslateUi(CarRegisterForm)
        QtCore.QMetaObject.connectSlotsByName(CarRegisterForm)

        self.reasonComboBox.addItem("Продажа")
        self.reasonComboBox.addItem("Утиль")

        #self.FillComboBox()
        self.CarRegistrationRadioBtns()
        self.driverPlainText.textChanged.connect(lambda: self.FillFCSListWidget())
        self.carIDEdit.textChanged.connect(lambda: self.CarIDEdit_slot())
        self.modelEdit.textChanged.connect(lambda: self.ModelEdit_slot())
        self.FCSlistWidget.itemActivated.connect(lambda: self.SetFCSPlainText(self.FCSlistWidget.currentItem()))
        self.applyButton.clicked.connect(lambda: self.ApplyRegister())
        self.ClearName.clicked.connect(lambda: self.ClearEnterName())

    def retranslateUi(self, CarRegisterForm):
        _translate = QtCore.QCoreApplication.translate
        CarRegisterForm.setWindowTitle(_translate("CarRegisterForm", "Управление учетом автомобилей"))
        self.carIDlabel.setText(_translate("CarRegisterForm", "Гос. номер"))
        self.modelLabel.setText(_translate("CarRegisterForm", "Модель"))
        self.CarRegisterLabel.setText(_translate("CarRegisterForm", "Управление учетом автомобилей"))
        self.reasonLabel.setText(_translate("CarRegisterForm", "Причина снятия с учета"))
        self.regRadioBtn.setText(_translate("CarRegisterForm", "Постановка"))
        self.deregRadioBtn.setText(_translate("CarRegisterForm", "Снятие"))
        self.carIDEdit.setPlaceholderText(_translate("CarRegisterForm", "А111АА 198"))
        self.driverLabel.setText(_translate("CarRegisterForm", "Водитель"))
        self.applyButton.setText(_translate("CarRegisterForm", "Принять"))
        self.ClearName.setText(_translate("Form", "✕"))

    def ModelEdit_slot(self):
        self.model = self.modelEdit.toPlainText()

    def SetFCSPlainText(self, item):
        self.driverPlainText.setPlainText(str(item.text()))
        self.FCSlistWidget.setVisible(False)

    def ClearEnterName(self):
        self.driverPlainText.clear()

    def ApplyRegister(self):
        self.driver = str(self.FCStext)
        print(self.driver)
        symbol = self.driver[2]
        i = 1
        while symbol != ')':
            i += 1
            symbol = self.driver[i + 1]
        self.driver_ID = self.driver[1:i + 1]
        self.driver = self.driver[i + 3:]
        date_str = str(datetime.date.today())
        status_Search_query = f"SELECT status FROM car WHERE car_ID = '{self.carIDtext}';"
        self.mycursor.execute(status_Search_query)
        self.con.commit()
        status = self.mycursor.fetchone()
        if (self.driverPlainText.isEnabled() == True):
            if (status != None):
                if (status[0] == 'Стоит на учете'):
                    Error = QMessageBox()
                    Error.setWindowTitle("Ошибка!")
                    Error.setText("Данный автомобиль уже зарегестрирован")
                    Error.setIcon(QMessageBox.Icon.Warning)
                    Error.exec()
                else:
                    query = f"UPDATE car SET driver_ID = {self.driver_ID}, model = '{self.model}', registration_date = '{date_str}', status = 'Стоит на учете', `reason` = NULL WHERE car_ID = '{self.carIDtext}';"
                    self.mycursor.execute(query)
                    self.con.commit()
                    Success = QMessageBox()
                    Success.setWindowTitle("Выполнено")
                    Success.setText("Информация об автомобиле обновлена")
                    Success.setIcon(QMessageBox.Icon.Information)
                    Success.exec()
                    #query = f"INSERT INTO car (car_ID, driver_ID, model, registration_date, status) VALUES ('{self.carIDtext}', {self.driver_ID}, '{self.model}', '{date_str}', 'стоит на учете');"
                    #print(self.carIDtext, "---", query)
            else:
                query = f"INSERT INTO car (car_ID, driver_ID, model, registration_date, status) VALUES ('{self.carIDtext}', {self.driver_ID}, '{self.model}', '{date_str}', 'Стоит на учете');"

                self.mycursor.execute(query)
                self.con.commit()
                Success = QMessageBox()
                Success.setWindowTitle("Выполнено")
                Success.setText("Автомобиль зарегестрирован")
                Success.setIcon(QMessageBox.Icon.Information)
                Success.exec()
        if (self.reasonComboBox.isEnabled() == True):
            if (status != None):
                if (status[0] == 'Стоит на учете'):
                    reason = str(self.reasonComboBox.currentText())
                    query = f"UPDATE `car` SET registration_date = '{date_str}', `status` = 'Снят с учета', `reason` = '{reason}'  WHERE car_ID = '{self.carIDtext}';"
                    self.mycursor.execute(query)
                    self.con.commit()
                    Success = QMessageBox()
                    Success.setWindowTitle("Выполнено")
                    Success.setText("Автомобиль успешно снят с учета")
                    Success.setIcon(QMessageBox.Icon.Information)
                    Success.exec()
                else:
                    Error = QMessageBox()
                    Error.setWindowTitle("Ошибка!")
                    Error.setText("Данный автомобиль уже снят с учета")
                    Error.setIcon(QMessageBox.Icon.Warning)
                    Error.exec()
            else:
                Error = QMessageBox()
                Error.setWindowTitle("Ошибка!")
                Error.setText("Автомобиль с таким госю номером не зарегестрирован")
                Error.setIcon(QMessageBox.Icon.Warning)
                Error.exec()
        self.modelEdit.clear()
        self.carIDEdit.clear()
        self.driverPlainText.clear()

    def CarIDEdit_slot(self):
        self.carIDtext = self.carIDEdit.toPlainText()
        if (len(self.carIDtext) > 0):
            self.regRadioBtn.setEnabled(True)
            self.deregRadioBtn.setEnabled(True)
            self.applyButton.setEnabled(True)
        else:
            self.regRadioBtn.setEnabled(False)
            self.deregRadioBtn.setEnabled(False)
            self.applyButton.setEnabled(False)

    def CarRegistrationRadioBtns(self):
        self.regRadioBtn.clicked.connect(lambda: self.Registration())
        self.deregRadioBtn.clicked.connect(lambda: self.Deregistration())

    def FillFCSListWidget(self):
        self.FCStext = self.driverPlainText.toPlainText()
        self.FCSlistWidget.clear()
        if (len(self.FCStext) == 0):
            self.FCSlistWidget.setVisible(False)
        else:
            self.FCSlistWidget.setVisible(True)
            query = f"SELECT driver_ID, FCS FROM driver_list WHERE FCS LIKE '%{(self.FCStext)}%'"
            self.mycursor.execute(query)
            self.con.commit()
            allIDandNames = self.mycursor.fetchall()
            countOfNames = len(allIDandNames)
            for i in range(0, countOfNames):
                self.addItemDriver(allIDandNames[i][0], allIDandNames[i][1])

    def Registration(self):
        self.driverPlainText.setEnabled(True)
        self.modelEdit.setEnabled(True)
        self.reasonComboBox.setEnabled(False)
        self.ClearName.setEnabled(True)

    def Deregistration(self):
        self.driverPlainText.setEnabled(False)
        self.modelEdit.setEnabled(False)
        self.reasonComboBox.setEnabled(True)
        self.ClearName.setEnabled(False)

    def addItemDriver(self, driverID, FCS):
        self.FCSlistWidget.addItem(f"({str(driverID)}) {FCS}")

    def FillComboBox(self):
        query = "SELECT driver_ID, FCS FROM driver_list"
        self.mycursor.execute(query)
        self.con.commit()
        allIDandNames = self.mycursor.fetchall()
        countOfNames = len(allIDandNames)
        for i in range(0, countOfNames):
            self.AddItemDriver(allIDandNames[i][0], allIDandNames[i][1])