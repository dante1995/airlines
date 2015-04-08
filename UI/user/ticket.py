
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
class ticket(QDialog):
    def __init__(self):
        super(ticket,self).__init__()
        self.initUI()

    def initUI(self):

        # while 1:
        # try:
        #         self.db = MySQLdb.connect("10.5.18.66","12CS10042","btech12","12CS10042")
        #         break
        #     except:
        #         time.sleep(.1)
        #         continue

        # self.cursor = self.db.cursor()
        # flights = ['dasd','fdgvdf ','dfewrf']
        # source = ['dsv','fv','fv']
        # dest = ['vcfsd','vd','dsvc']


        self.grid = QGridLayout()
        size = 6

        #
        # self.ok = QPushButton("Book Now")
        # self.cancel = QPushButton("Cancel")
        #
        # self.connect(self.ok,SIGNAL("clicked()"),self.ok_func)
        # self.connect(self.cancel,SIGNAL("clicked()"),self.cancel_func)
        # #
        self.setGeometry(250,250,500,500)
        self.setLayout(self.grid)
        self.table = QTableWidget()
        self.table.setRowCount(size)
        self.table.setColumnCount(1)
        #self.table.setHorizontalHeaderLabels(QString("Flight ID;From;To ;Availability;Time").split(";"));
        self.table.setVerticalHeaderLabels(QString("Book ID;Flight No.;Date;From;To;Time").split(";"))
        self.table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        #self.table.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.table.resizeColumnsToContents()
        #
        # for i in range(size):
        #     self.table.setItem(i,0,QTableWidgetItem(flights[i]))
        #     self.table.setItem(i,1,QTableWidgetItem(source[i]))
        #     self.table.setItem(i,2,QTableWidgetItem(dest[i]))
        #     self.table.setItem(i,3,QTableWidgetItem("100"))
        #     self.table.setItem(i,4,QTableWidgetItem("10:00"))

        self.table1 = QTableWidget()
        self.table1.setRowCount(5)
        self.table1.setColumnCount(3)
        self.table1.setHorizontalHeaderLabels(QString("Name;Age;Gender").split(";"));
        #self.table1.setVerticalHeaderLabels(QString("Book ID;Flight No.;Date;From;To;Time").split(";"))
        self.table1.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        #self.table.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.table1.resizeColumnsToContents()
        #
        # for i in range(size):
        #     self.table.setItem(i,0,QTableWidgetItem(flights[i]))
        #     self.table.setItem(i,1,QTableWidgetItem(source[i]))
        #     self.table.setItem(i,2,QTableWidgetItem(dest[i]))
        #     self.table.setItem(i,3,QTableWidgetItem("100"))
        #     self.table.setItem(i,4,QTableWidgetItem("10:00"))



        self.grid.addWidget(self.table,0,0,1,-1)
        self.grid.addWidget(self.table1,1,0)
        # self.grid.addWidget(self.ok,1,3,1,1)
        # self.grid.addWidget(self.cancel,1,4,1,1)

        self.setLayout(self.grid)
    #
    # def ok_func(self):
    #     self.id =  self.table.currentItem().text()
    #     pass_ent = passenger_entry(self.id)
    #     pass_ent.exec_()
    #     print "ticket"
    # def cancel_func(self):
    #     self.close()
    #     x=3


app = QApplication(sys.argv)
start = ticket()
start.show()
app.exec_()


if __name__ == '__main__':
    main()