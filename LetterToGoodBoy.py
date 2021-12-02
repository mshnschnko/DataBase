import bd_main
import datetime
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication
import GoodBoyForm

def CheckForGoodBoys():
    con = bd_main.connect()
    mycursor = con.cursor()
    query = f"SELECT driver_ID FROM driver_violation;"
    mycursor.execute(query)
    con.commit()
    all = mycursor.fetchall()
    drivers = []
    for i in range(0, len(all)):
        if (not (all[i][0] in drivers)):
            drivers.append(all[i][0])
    for i in range(0, len(drivers)):
        query = f"SELECT date_of_the_fine, FCS FROM driver_violation WHERE driver_ID = {drivers[i]}"
        mycursor.execute(query)
        con.commit()
        allFines = mycursor.fetchall()
        maximum = max(allFines)
        maxDate = maximum[0]

        query = f"SELECT has_the_fine_been_paid FROM driver_violation WHERE date_of_the_fine = '{str(maxDate)}';"
        mycursor.execute(query)
        con.commit()
        (payFact,) = mycursor.fetchone()
        if (payFact == 1 and maxDate + datetime.timedelta(days=365) == datetime.date.today()):
            OpenGoodBoyForm(maximum[1])

def OpenGoodBoyForm(FCS):
    GoodBoy = QtWidgets.QDialog()
    ui = GoodBoyForm.Ui_GoodBoyForm()
    ui.setupUi(GoodBoy, FCS)
    GoodBoy.exec()