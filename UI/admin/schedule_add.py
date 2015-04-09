__author__ = 'inzamam'


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb
import time
import sys
import datetime


class Schedule_Add(QDialog):
    def __init__(self):
        super(Schedule_Add,self).__init__()
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

        self.sid = QLabel("Schedule ID")
        self.isid = QLineEdit()
        self.isid.setPlaceholderText("Enter Schedule ID")
        self.fdate = QLabel("Flight Date")
        self.ifdate = QLineEdit()
        self.ifdate.setPlaceholderText("Enter Flight Date")
        self.arr = QLabel("Arrival")
        self.iarr = QLineEdit()
        self.iarr.setPlaceholderText("Enter Arrival Time")
        self.dep = QLabel("Departure")
        self.idep = QLineEdit()
        self.idep.setPlaceholderText("Enter Departure Time")
        self.fid = QLabel("Flight ID")
        self.ifid = QLineEdit()
        self.ifid.setPlaceholderText("Enter Flight ID")
        self.rid = QLabel("Route ID")
        self.irid = QLineEdit()
        self.irid.setPlaceholderText("Enter Route ID")
        self.temp = QLabel("")

        self.setGeometry(250,250,500,500)

        self.isid.setFixedWidth(200)
        self.ifdate.setFixedWidth(200)
        self.iarr.setFixedWidth(200)
        self.idep.setFixedWidth(200)
        self.ifid.setFixedWidth(200)
        self.irid.setFixedWidth(200)

        self.sid.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.fdate.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.arr.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.dep.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.fid.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.rid.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.grid = QGridLayout()
        self.grid.addWidget(self.sid,0,0)
        self.grid.addWidget(self.isid,0,1)
        self.grid.addWidget(self.fdate,1,0)
        self.grid.addWidget(self.ifdate,1,1)
        self.grid.addWidget(self.arr,2,0)
        self.grid.addWidget(self.iarr,2,1)
        self.grid.addWidget(self.dep,3,0)
        self.grid.addWidget(self.idep,3,1)
        self.grid.addWidget(self.fid,4,0)
        self.grid.addWidget(self.ifid,4,1)
        self.grid.addWidget(self.rid,5,0)
        self.grid.addWidget(self.irid,5,1)
        self.grid.addWidget(self.temp,5,2)

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
        schedule_id = str(self.isid.text())
        flight_date = str(self.ifdate.text())
        arr_time = str(self.iarr.text())
        dep_time = str(self.idep.text())
        flight_id = str(self.ifid.text())
        route_id = str(self.irid.text())

        avail=0
        self.cursor.execute("select flight_id,capacity from flight")
        res=self.cursor.fetchall()
        for j in range(len(res)):
            if str(res[j][0])==flight_id:
                avail=int(res[j][1])

        self.cursor.execute("select schedule_id from schedule")
        result = self.cursor.fetchall()
        for i in range(len(result)):
            if str(result[i][0]) == schedule_id:
                message = QMessageBox(QMessageBox.Warning,"Error Message","This schedule id is already entered. Try Again",buttons = QMessageBox.Close)
                message.exec_()
                return

        flag=0
        self.cursor.execute("select route_id from route")
        result1 = self.cursor.fetchall()
        for i in range(len(result1)):
            if str(result1[i][0]) == route_id:
                flag=1
                break
        if(flag==0):
            message = QMessageBox(QMessageBox.Warning,"Error Message","This route id is not present in the database. Try Again",buttons = QMessageBox.Close)
            message.exec_()
            return

        flag1=0
        self.cursor.execute("select flight_id from flight")
        result2 = self.cursor.fetchall()
        for i in range(len(result2)):
            if str(result2[i][0]) == flight_id:
                flag1=1
                break
        if(flag1==0):
            message = QMessageBox(QMessageBox.Warning,"Error Message","This flight id is not present in the database. Try Again",buttons = QMessageBox.Close)
            message.exec_()
            return

        try:
            self.cursor.execute("insert into schedule(schedule_id,flight_date,arrival,departure,flight_id,route_id,available) values('%s','%s','%s','%s','%s','%s','%s')"%(schedule_id,flight_date,arr_time,dep_time,flight_id,route_id,avail))
            self.db.commit()
            self.reset_all()
        except:
            self.db.rollback()
            message = QMessageBox(QMessageBox.Warning,"Prescribe Message","Some error occured. Try Again",buttons = QMessageBox.Close)
            message.exec_()





    def reset_all(self):
        self.isid.clear()
        self.ifdate.clear()
        self.iarr.clear()
        self.idep.clear()
        self.ifid.clear()
        self.irid.clear()


#
# app = QApplication(sys.argv)
# start = Schedule_Add()
# start.show()
# app.exec_()
