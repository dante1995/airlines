__author__ = 'inzamam'


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb
import time
import sys
import datetime


class Flight_Add(QDialog):
    def __init__(self):
        super(Flight_Add,self).__init__()
        self.initUI()

    def initUI(self):

        while 1:
            try:
                self.db = MySQLdb.connect("10.5.18.66","12CS10041","btech12","12CS10041")
                break
            except:
                time.sleep(.1)
                continue

        self.cursor = self.db.cursor()

        self.fid = QLabel("Flight ID")
        self.ifid = QLineEdit()
        self.ifid.setPlaceholderText("Enter Flight ID")
        # self.fname = QLabel("Flight Name")
        # self.ifname = QLineEdit()
        # self.ifname.setPlaceholderText("Enter Flight Name")
        self.aline = QLabel("Airline")
        self.ialine = QLineEdit()
        self.ialine.setPlaceholderText("Enter Airline Name")
        self.cap = QLabel("Capacity")
        self.icap = QLineEdit()
        self.icap.setPlaceholderText("Enter Capacity")
        self.temp = QLabel("")

        self.setGeometry(250,250,500,500)

        self.ifid.setFixedWidth(200)
        #self.ifname.setFixedWidth(200)
        self.ialine.setFixedWidth(200)
        self.icap.setFixedWidth(200)

        self.fid.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        #self.fname.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.aline.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.cap.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.grid = QGridLayout()
        self.grid.addWidget(self.fid,0,0)
        self.grid.addWidget(self.ifid,0,1)
        #self.grid.addWidget(self.fname,1,0)
        #self.grid.addWidget(self.ifname,1,1)
        self.grid.addWidget(self.aline,1,0)
        self.grid.addWidget(self.ialine,1,1)
        self.grid.addWidget(self.cap,2,0)
        self.grid.addWidget(self.icap,2,1)
        self.grid.addWidget(self.temp,2,2)

        self.hbox = QHBoxLayout()
        self.reset = QPushButton("Reset")
        self.update = QPushButton("Update")
        self.update.setStyleSheet("color: black; background-color:gray")
        self.reset.setStyleSheet("color: black; background-color:gray")
        self.cancel = QPushButton("Cancel")
        self.cancel.setStyleSheet("color: balck; background-color:gray")

        self.hbox.addStretch(1)
        self.hbox.addWidget(self.reset)
        self.hbox.addWidget(self.update)
        self.hbox.addWidget(self.cancel)
        self.hbox.addStretch(1)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.grid)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)


        self.connect(self.update,SIGNAL("clicked()"),self.entry)
        self.connect(self.reset,SIGNAL("clicked()"),self.reset_all)
        self.connect(self.cancel,SIGNAL("clicked()"),self.canceli)


    def canceli(self):
        self.db.close()
        self.close()

    def entry(self):
        id_flight = str(self.ifid.text())
        #flight_name = str(self.ifname.text())
        airline = str(self.ialine.text())
        capacity = str(self.icap.text())

        if( len(airline))==0:
            message = QMessageBox(QMessageBox.Warning,"Error Message","Please enter Full details. Try Again",buttons = QMessageBox.Close)
            message.exec_()
            return

        if(capacity.isdigit() == 0):
            message = QMessageBox(QMessageBox.Warning,"Error Message","Capacity must be an integer. Try Again",buttons = QMessageBox.Close)
            message.exec_()
            return

        self.cursor.execute("select flight_id from flight")
        result = self.cursor.fetchall()
        for i in range(len(result)):
            if str(result[i][0]) == id_flight:
                message = QMessageBox(QMessageBox.Warning,"Error Message","This Flight id in already entered. Try Again",buttons = QMessageBox.Close)
                message.exec_()
                return

        try:
            self.cursor.execute("insert into flight(flight_id,airline,capacity) values('%s','%s','%s')"%(id_flight,airline,capacity))
            self.db.commit()
            self.reset_all()
        except:
            self.db.rollback()
            message = QMessageBox(QMessageBox.Warning,"Prescribe Message","Some error occured. Try Again",buttons = QMessageBox.Close)
            message.exec_()





    def reset_all(self):
        self.ifid.clear()
        #self.ifname.clear()
        self.ialine.clear()
        self.icap.clear()


#
# app = QApplication(sys.argv)
# start = Flight_Add()
# start.show()
# app.exec_()
