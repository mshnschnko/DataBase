import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QWidget

import pymysql.cursors
import bd_main
import AddDriverWidget
import MainMenu
import LetterToGoodBoy
#from MainMenu import Ui_MainWindow

#import mysql.connector
#from mysql.connector import Error

def application(connection):
    app = QApplication(sys.argv)
    Mainwindow = QMainWindow()
    ui = MainMenu.Ui_MainWindow()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    connection = bd_main.connect()
    #LetterToGoodBoy.CheckForGoodBoys()
    application(connection)
    connection.close()