# Form implementation generated from reading ui file 'AddDriverWidget.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import re
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QWidget
import bd_main


class Ui_Form(object):
    def setupUi(self, Form):
        self.con = bd_main.connect()
        Form.setObjectName("Form")
        Form.resize(500, 170)
        self.AddDriverLabel = QtWidgets.QLabel(Form)
        self.AddDriverLabel.setGeometry(QtCore.QRect(0, 30, 500, 25))
        self.AddDriverLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AddDriverLabel.setFont(font)
        self.AddDriverLabel.setObjectName("FCS")
        self.FCSedit = QtWidgets.QPlainTextEdit(Form)
        self.FCSedit.setPlaceholderText("Введите имя...")
        self.FCSedit.setGeometry(QtCore.QRect(80, 70, 400, 30))
        self.FCSedit.setObjectName("FCSedit")
        self.FCS = QtWidgets.QLabel(Form)
        self.FCS.setGeometry(QtCore.QRect(35, 70, 35, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FCS.setFont(font)
        self.FCS.setObjectName("FCS")
        self.ApplyBut = QtWidgets.QPushButton(Form)
        self.ApplyBut.setGeometry(QtCore.QRect(405, 130, 75, 23))
        self.ApplyBut.setEnabled(False)
        self.ApplyBut.setObjectName("ApplyBut")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.FCSedit.textChanged.connect(lambda: self.plainText_slot())
        self.ApplyBut.clicked.connect(lambda: self.AddDriverQuery())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление водителя"))
        self.AddDriverLabel.setText(_translate("Form", "Добавление водителя"))
        self.FCS.setText(_translate("Form", "ФИО"))
        self.ApplyBut.setText(_translate("Form", "Принять"))

    def plainText_slot(self):
        self.text = self.FCSedit.toPlainText()
        if (len(self.text) > 0):
            self.ApplyBut.setEnabled(True)
        else:
            self.ApplyBut.setEnabled(False)

    def AddDriverQuery(self):
        matchFCS = re.findall(r"[а-я,А-Я]+\s[а-я,А-Я]+\s?[а-я,А-Я]*", self.text)
        if (len(matchFCS) == 1):
            self.AddDriver()
            Success = QMessageBox()
            Success.setWindowTitle("Выполнено")
            Success.setText("Водитель успешно добавлен в реестр")
            Success.setIcon(QMessageBox.Icon.Information)
            Success.exec()
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Введены некорректные данные")
            error.setIcon(QMessageBox.Icon.Warning)
            error.exec()

    def AddDriver(self):
        mycursor = self.con.cursor()
        query = f"INSERT INTO driver_list (FCS, fine_count) VALUES ('{self.text}', 0)"
        bd_main.execute(self.con, mycursor, query)
        self.con.commit()
        self.FCSedit.clear()