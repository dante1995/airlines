from UI.user import cancel_ticket

__author__ = 'sabya'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui,QtCore
import MySQLdb
import time
import sys
import datetime
from book_window import *
from passenger_entry import *
from cancel_ticket import *

class cancel_window(QDialog):
    def __init__(self,uid):
        super(cancel_window,self).__init__()
        self.uid = uid
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



        self.cancelTicket = QPushButton("Cancel Ticket")
        self.close_ = QPushButton("Close")

        self.connect(self.cancelTicket,SIGNAL("clicked()"),self.cancel_tick)
        self.connect(self.close_,SIGNAL("clicked()"),self.close_func)
        #

        try:
            self.cursor.execute("select booking_id,flight_id,num_seats,flight_date,arrival,departure,schedule_id from user_book natural join booking natural join schedule where user_id = \""+str(self.uid)+"\";")
            user_result = self.cursor.fetchall()
            print user_result
            #print len(user_result)
        except:
            print "Error"

        self.setGeometry(250,250,500,500)
        # self.setLayout(self.grid)
        self.table = QTableWidget()
        self.table.setRowCount(len(user_result))
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(QString("Book ID;Flight No.;#Passengers ;Date;Arrival;Departure;Schedule ID").split(";"));

        self.table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.table.resizeColumnsToContents()


        for i in range(len(user_result)):
            self.table.setItem(i,0,QTableWidgetItem(user_result[i][0]))
            self.table.setItem(i,1,QTableWidgetItem(user_result[i][1]))
            self.table.setItem(i,2,QTableWidgetItem(str(user_result[i][2])))
            self.table.setItem(i,3,QTableWidgetItem(str(user_result[i][3])))
            self.table.setItem(i,4,QTableWidgetItem(str(user_result[i][4])))
            self.table.setItem(i,5,QTableWidgetItem(str(user_result[i][5])))
            self.table.setItem(i,6,QTableWidgetItem(str(user_result[i][6])))


        self.grid.addWidget(self.table,0,0,1,-1)
        self.grid.addWidget(self.cancelTicket,1,3,1,1)
        self.grid.addWidget(self.close_,1,4,1,1)

        self.setLayout(self.grid)

    # def ok_func(self):
    #     self.id =  self.table.currentItem().text()
    #     pass_ent = passenger_entry(self.id)
    #     pass_ent.exec_()
    #     print "ticket"
    def close_func(self):
        self.close()

    def cancel_tick(self):
        row =  self.table.currentRow()
        schedule_id = self.table.item(row,6).text()
        schedule_id = str(schedule_id)
        booking_id = self.table.item(row,0).text()
        booking_id = str(booking_id)
        tick = cancel_ticket(booking_id,schedule_id)
        tick.exec_()

#
# app = QApplication(sys.argv)
# start = cancel_window()
# start.show()
# app.exec_()

