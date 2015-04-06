__author__ = 'sabya'


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb
import time
import sys
import datetime


class Flight_Add(QFrame):
    def __init__(self):
        super(Flight_Add,self).__init__()
        self.initUI()

    def initUI(self):

        # while 1:
        #     try:
        #         self.db = MySQLdb.connect("10.5.18.66","12CS10042","btech12","12CS10042")
        #         break
        #     except:
        #         time.sleep(.1)
        #         continue
        #
        # self.cursor = self.db.cursor()

        self.fid = QLabel("Flight ID")
        self.ifid = QLineEdit()
        self.ifid.setPlaceholderText("Enter Flight ID")
        self.fname = QLabel("Flight Name")
        self.ifname = QLineEdit()
        self.ifname.setPlaceholderText("Enter Flight Name")
        self.aline = QLabel("Airline")
        self.ialine = QLineEdit()
        self.ialine.setPlaceholderText("Enter Airline Name")
        self.cap = QLabel("Capacity")
        self.icap = QLineEdit()
        self.icap.setPlaceholderText("Enter Capacity")
        self.temp = QLabel("")

        self.ifid.setFixedWidth(200)
        self.ifname.setFixedWidth(200)
        self.ialine.setFixedWidth(200)
        self.icap.setFixedWidth(200)

        self.fid.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.fname.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.aline.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.cap.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.grid = QGridLayout()
        self.grid.addWidget(self.fid,0,0)
        self.grid.addWidget(self.ifid,0,1)
        self.grid.addWidget(self.fname,1,0)
        self.grid.addWidget(self.ifname,1,1)
        self.grid.addWidget(self.aline,2,0)
        self.grid.addWidget(self.ialine,2,1)
        self.grid.addWidget(self.cap,3,0)
        self.grid.addWidget(self.icap,3,1)
        self.grid.addWidget(self.temp,3,2)

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
        start.close()

    def entry(self):
        room = str(self.iroomno.text())
        building = str(self.ibuilding.text())
        dept = str(self.idept.text())
        prps = str(self.iprps.currentText())

        if(len(room)) == 0 or len(building)==0:
            message = QMessageBox(QMessageBox.Warning,"Error Message","Please enter Full details. Try Again",buttons = QMessageBox.Close)
            message.exec_()
            return

        if(room.isdigit() == 0):
            message = QMessageBox(QMessageBox.Warning,"Error Message","Room must be an integer. Try Again",buttons = QMessageBox.Close)
            message.exec_()
            return
        if(prps == "select"):
            message = QMessageBox(QMessageBox.Warning,"Error Message","Please select Purpose of this room. Try Again",buttons = QMessageBox.Close)
            message.exec_()
            return
        if len(dept) == 0:
            dept = "NULL"

        self.cursor.execute("select RoomNo,Building from Room")
        result = self.cursor.fetchall()
        for i in range(len(result)):
            if str(result[i][0]) == room and str(result[i][1]) == building:
                message = QMessageBox(QMessageBox.Warning,"Error Message","This room in already entered. Try Again",buttons = QMessageBox.Close)
                message.exec_()
                return

        try:
            self.cursor.execute("insert into Room(RoomNo,Building,Department,Purpose) values('%s','%s','%s','%s')"%(room,building,dept,prps))
            self.db.commit()
            self.reset_all()
        except:
            self.db.rollback()
            message = QMessageBox(QMessageBox.Warning,"Prescribe Message","Some error occured. Try Again",buttons = QMessageBox.Close)
            message.exec_()





    def reset_all(self):
        self.iroomno.clear()
        self.ibuilding.clear()
        self.iprps.setCurrentIndex(0)
        self.idept.clear()



app = QApplication(sys.argv)
start = Flight_Add()
start.show()
app.exec_()
