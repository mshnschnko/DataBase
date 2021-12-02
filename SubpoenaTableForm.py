# Form implementation generated from reading ui file 'SubpoenaTableForm.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import datetime

from PyQt6 import QtCore, QtGui, QtWidgets
import bd_main

class Ui_subpoena(object):
    def setupUi(self, subpoena, FCS, driver_ID):
        self.con = bd_main.connect()
        self.mycursor = self.con.cursor()
        subpoena.setObjectName("subpoena")
        subpoena.resize(500, 340)
        self.subpoenaLabel = QtWidgets.QLabel(subpoena)
        self.subpoenaLabel.setGeometry(QtCore.QRect(210, 30, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.subpoenaLabel.setFont(font)
        self.subpoenaLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.subpoenaLabel.setObjectName("subpoenaLabel")
        self.descriptionLabel = QtWidgets.QLabel(subpoena)
        self.descriptionLabel.setGeometry(QtCore.QRect(30, 45, 440, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setObjectName("descriptionLabel")

        self.dateLabel = QtWidgets.QLabel(subpoena)
        self.dateLabel.setGeometry(QtCore.QRect(30, 300, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateLabel.setFont(font)
        self.dateLabel.setWordWrap(True)
        self.dateLabel.setObjectName("dateLabel")

        self.summaryTable = QtWidgets.QTableWidget(subpoena)
        self.summaryTable.setGeometry(QtCore.QRect(30, 120, 440, 160))
        self.summaryTable.setObjectName("summaryTable")
        self.summaryTable.setColumnCount(4)
        self.summaryTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.summaryTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.summaryTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.summaryTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.summaryTable.setHorizontalHeaderItem(3, item)

        self.retranslateUi(subpoena, FCS)
        QtCore.QMetaObject.connectSlotsByName(subpoena)

        self.summaryTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger(False))
        self.summaryTable.verticalHeader().setVisible(False)
        self.FillTable(driver_ID)

    def retranslateUi(self, subpoena, FCS):
        _translate = QtCore.QCoreApplication.translate
        subpoena.setWindowTitle(_translate("subpoena", "Повестка"))
        self.subpoenaLabel.setText(_translate("subpoena", "Повестка"))
        self.descriptionLabel.setText(_translate("subpoena", f"Гражданин {FCS} вызывается в районный суд по месту жительства по причине систематической неуплаты штрафов за нарушение правил дорожного движения:"))
        self.dateLabel.setText(_translate("subpoena", f"{str(datetime.date.today())}"))
        item = self.summaryTable.horizontalHeaderItem(0)
        item.setText(_translate("subpoena", "ID штрафа"))
        item = self.summaryTable.horizontalHeaderItem(1)
        item.setText(_translate("subpoena", "Нарушение"))
        item = self.summaryTable.horizontalHeaderItem(2)
        item.setText(_translate("subpoena", "Дата нарушения"))
        item = self.summaryTable.horizontalHeaderItem(3)
        item.setText(_translate("subpoena", "Сумма"))

    def FillTable(self, driver_ID):
        query = f"SELECT * FROM driver_violation WHERE driver_ID = {driver_ID} AND has_the_fine_been_paid = 0;"
        self.mycursor.execute(query)
        self.con.commit()
        allInfo = self.mycursor.fetchall()
        infoLen = len(allInfo)
        for i in range(0, infoLen):
            query = f"SELECT violation FROM violation_list WHERE violation_ID = {allInfo[i][3]}"
            self.mycursor.execute(query)
            self.con.commit()
            (violation,) = self.mycursor.fetchone()
            self.AddRow(allInfo[i][0], violation, allInfo[i][5], allInfo[i][6])

    def AddRow(self, relation_ID, violation, dateOfTheFine, sum):
        rowPosition = self.summaryTable.rowCount()
        self.summaryTable.insertRow(rowPosition)

        self.summaryTable.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(relation_ID)))
        self.summaryTable.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(violation))
        self.summaryTable.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(dateOfTheFine)))
        self.summaryTable.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(sum)))