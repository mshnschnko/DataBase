# Form implementation generated from reading ui file 'GoodBoyForm.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import datetime

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GoodBoyForm(object):
    def setupUi(self, GoodBoyForm, FCS):
        GoodBoyForm.setObjectName("GoodBoyForm")
        GoodBoyForm.resize(400, 220)
        self.GoodBoyLabel = QtWidgets.QLabel(GoodBoyForm)
        self.GoodBoyLabel.setGeometry(QtCore.QRect(0, 30, 400, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.GoodBoyLabel.setFont(font)
        self.GoodBoyLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.GoodBoyLabel.setObjectName("GoodBoyLabel")
        self.DescriptionLabel = QtWidgets.QLabel(GoodBoyForm)
        self.DescriptionLabel.setGeometry(QtCore.QRect(20, 60, 360, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DescriptionLabel.setFont(font)
        self.DescriptionLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.DescriptionLabel.setWordWrap(True)
        self.DescriptionLabel.setObjectName("DescriptionLabel")
        self.label = QtWidgets.QLabel(GoodBoyForm)
        self.label.setGeometry(QtCore.QRect(20, 180, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(GoodBoyForm, FCS)
        QtCore.QMetaObject.connectSlotsByName(GoodBoyForm)

    def retranslateUi(self, GoodBoyForm, FCS):
        _translate = QtCore.QCoreApplication.translate
        GoodBoyForm.setWindowTitle(_translate("GoodBoyForm", "Молодец!"))
        self.GoodBoyLabel.setText(_translate("GoodBoyForm", "Молодец!"))
        self.DescriptionLabel.setText(_translate("GoodBoyForm", f"Уважаемый {FCS}, благодарим Вас за качественное и безопасное вождение. Вы проездили год без аварий. Также с вас снимается надбавка к штрафам. Будьте аккуратны и не нарушайте правила дорожного движения!"))
        self.label.setText(_translate("GoodBoyForm", f"{str(datetime.date.today())}"))
