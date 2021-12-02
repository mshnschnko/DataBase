# Form implementation generated from reading ui file 'SubPoenaNonPay.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import datetime

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QHeaderView
import bd_main


class Ui_SubPoenaNonPay(object):
    def setupUi(self, SubPoenaNonPay, driver_ID):
        self.con = bd_main.connect()
        self.mycursor = self.con.cursor()
        SubPoenaNonPay.setObjectName("SubPoenaNonPay")
        SubPoenaNonPay.resize(500, 335)
        self.subpoenaLabel = QtWidgets.QLabel(SubPoenaNonPay)
        self.subpoenaLabel.setGeometry(QtCore.QRect(0, 30, 500, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.subpoenaLabel.setFont(font)
        self.subpoenaLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.subpoenaLabel.setObjectName("subpoenaLabel")
        self.descriptionLabel = QtWidgets.QLabel(SubPoenaNonPay)
        self.descriptionLabel.setGeometry(QtCore.QRect(30, 45, 440, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.summaryTable = QtWidgets.QTableWidget(SubPoenaNonPay)
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
        self.summaryTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.summaryTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)

        self.summaryTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger(False))
        self.summaryTable.verticalHeader().setVisible(False)
        self.DateLabel = QtWidgets.QLabel(SubPoenaNonPay)
        self.DateLabel.setGeometry(QtCore.QRect(30, 300, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DateLabel.setFont(font)
        self.DateLabel.setObjectName("DateLabel")

        self.retranslateUi(SubPoenaNonPay)
        QtCore.QMetaObject.connectSlotsByName(SubPoenaNonPay)

        self.SetSubpoena(driver_ID)
        self.FillTable(driver_ID)

    def retranslateUi(self, SubPoenaNonPay):
        _translate = QtCore.QCoreApplication.translate
        SubPoenaNonPay.setWindowTitle(_translate("SubPoenaNonPay", "Повестка"))
        self.subpoenaLabel.setText(_translate("SubPoenaNonPay", "Повестка"))
        self.descriptionLabel.setText(_translate("SubPoenaNonPay", "Гражданин вызывается в районный суд по месту жительства по причине неуплаты штрафов за нарушение правил дорожного движения в срок:"))
        item = self.summaryTable.horizontalHeaderItem(0)
        item.setText(_translate("SubPoenaNonPay", "ID штрафа"))
        item = self.summaryTable.horizontalHeaderItem(1)
        item.setText(_translate("SubPoenaNonPay", "Нарушение"))
        item = self.summaryTable.horizontalHeaderItem(2)
        item.setText(_translate("SubPoenaNonPay", "Дата нарушения"))
        item = self.summaryTable.horizontalHeaderItem(3)
        item.setText(_translate("SubPoenaNonPay", "Сумма"))
        self.DateLabel.setText(_translate("SubPoenaNonPay", f"{str(datetime.date.today())}"))

    def SetSubpoena(self, driver_ID):
        query = f"SELECT FCS FROM driver_list WHERE driver_ID = {driver_ID}"
        self.mycursor.execute(query)
        self.con.commit()
        (FCS,) = self.mycursor.fetchone()
        self.descriptionLabel.setText(f"Гражданин {FCS} вызывается в районный суд по месту жительства по причине неуплаты штрафов за нарушение правил дорожного движения в срок:")

    def FillTable(self, driver_ID):
        query = f"SELECT relation_ID, violation_ID, sum FROM driver_violation WHERE driver_ID = {driver_ID} AND date_of_the_fine = '{str(datetime.date.today() + datetime.timedelta(days=-30))}' AND has_the_fine_been_paid = 0;"
        self.mycursor.execute(query)
        self.con.commit()
        allInfo = self.mycursor.fetchall()
        for i in range(0, len(allInfo)):
            query = f"SELECT violation FROM violation_list WHERE violation_ID = {allInfo[i][1]};"
            self.mycursor.execute(query)
            self.con.commit()
            (violation,) = self.mycursor.fetchone()
            self.AddRow(allInfo[i][0], violation, str(datetime.date.today() + datetime.timedelta(days=-30)), allInfo[i][2])

    def AddRow(self, relation_ID, violation, dateOfTheFine, sum):
        rowPosition = self.summaryTable.rowCount()
        self.summaryTable.insertRow(rowPosition)

        self.summaryTable.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(relation_ID)))
        self.summaryTable.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(violation))
        self.summaryTable.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(dateOfTheFine))
        self.summaryTable.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(sum)))