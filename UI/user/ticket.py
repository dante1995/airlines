
__author__ = 'sabya'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui,QtCore
import MySQLdb
import time
import sys
import datetime

class ticket(QDialog):
    def __init__(self,booking_id,schedule_id):
        super(ticket,self).__init__()
        self.booking_id = booking_id
        self.schedule_id = schedule_id
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
        self.grid = QGridLayout()

        self.setGeometry(250,250,500,500)
        self.setLayout(self.grid)
        self.table = QTableWidget()
        self.table.setRowCount(6)
        self.table.setColumnCount(1)
        self.table.setVerticalHeaderLabels(QString("Book ID;Flight No.;Date;From;To;Time").split(";"))
        self.table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.table.resizeColumnsToContents()

        self.table1 = QTableWidget()

        self.table1.setColumnCount(5)
        self.table1.setHorizontalHeaderLabels(QString("Name;Age;Gender;Seat;Senior Citizen").split(";"));
        self.table1.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.table1.resizeColumnsToContents()

        sql = "select flight_id, flight_date, departure, route_id from schedule where schedule_id = \""+str(self.schedule_id)+"\";"
        self.cursor.execute(sql)
        schedule = self.cursor.fetchall()
        fid = str(schedule[0][0])
        date = str(schedule[0][1])
        tim = str(schedule[0][2])
        route = str(schedule[0][3])

        sql = "select source,destination from route where route_id = \""+str(route)+"\";"
        self.cursor.execute(sql)
        route_vals = self.cursor.fetchall()
        sid = str(route_vals[0][0])
        did = str(route_vals[0][1])

        sql = "select city from airport where airport_id = \""+str(sid)+"\";"
        self.cursor.execute(sql)
        fro = str(self.cursor.fetchall()[0][0])
        sql = "select city from airport where airport_id = \""+str(did)+"\";"
        self.cursor.execute(sql)
        to = str(self.cursor.fetchall()[0][0])

        self.table.setItem(0,0,QTableWidgetItem(str(self.booking_id)))
        self.table.setItem(1,0,QTableWidgetItem(str(fid)))
        self.table.setItem(2,0,QTableWidgetItem(str(date)))
        self.table.setItem(3,0,QTableWidgetItem(str(fro)))
        self.table.setItem(4,0,QTableWidgetItem(str(to)))
        self.table.setItem(5,0,QTableWidgetItem(str(tim)))

        sql = "select passenger_id from passenger_book where booking_id = \""+str(self.booking_id)+"\";"
        self.cursor.execute(sql)
        passengers = self.cursor.fetchall()
        passenger_list = []
        for passenger in passengers:
            passenger_list.append(passenger[0])

        self.table1.setRowCount(len(passenger_list))
        i = 0
        for x in passenger_list:
            sql = "select name, age, gender, seat, disabled from passenger where passenger_id = \""+str(x)+"\";"
            self.cursor.execute(sql)
            pass_detail = self.cursor.fetchall()
            name = str(pass_detail[0][0])
            age = str(pass_detail[0][1])
            gender = str(pass_detail[0][2])
            seat = str(pass_detail[0][3])
            senior = str(pass_detail[0][4])
            self.table1.setItem(i,0,QTableWidgetItem(str(name)))
            self.table1.setItem(i,1,QTableWidgetItem(str(age)))
            self.table1.setItem(i,2,QTableWidgetItem(str(gender)))
            self.table1.setItem(i,3,QTableWidgetItem(str(seat)))
            self.table1.setItem(i,4,QTableWidgetItem(str(senior)))
            i+=1

        self.grid.addWidget(self.table,0,0,1,-1)
        self.grid.addWidget(self.table1,1,0)


        self.setLayout(self.grid)

#
# app = QApplication(sys.argv)
# start = ticket(11,"QE356201")
# start.show()
# app.exec_()
