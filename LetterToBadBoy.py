import bd_main
import datetime
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication
import SubPoenaNonPay

def CheckForBadBoys():
    con = bd_main.connect()
    mycursor = con.cursor()
    query = f"SELECT driver_ID FROM driver_violation WHERE date_of_the_fine = '{str(datetime.date.today() + datetime.timedelta(days=-30))}' AND has_the_fine_been_paid = 0;"
    mycursor.execute(query)
    con.commit()
    all = mycursor.fetchall()
    drivers = []
    for i in range(0, len(all)):
        if (not (all[i][0] in drivers)):
            drivers.append(all[i][0])
    for i in range(0, len(drivers)):
        OpenBadBoyForm(drivers[i])

def OpenBadBoyForm(driver_ID):
    BadBoy = QtWidgets.QDialog()
    ui = SubPoenaNonPay.Ui_SubPoenaNonPay()
    ui.setupUi(BadBoy, driver_ID)
    BadBoy.exec()