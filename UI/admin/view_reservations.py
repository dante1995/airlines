__author__ = 'inzamam'


from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui,QtCore
import MySQLdb
import time
import sys
import datetime
#from book_window import *
#from passenger_entry import *


class View_Reservations(QDialog):
    def __init__(self):
        super(View_Reservations,self).__init__()
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

        self.cursor.execute("select user_id,num_seats,flight_id,schedule_id from user natural join user_book natural join booking natural join schedule")
        res=self.cursor.fetchall()
        size=len(res)

        self.grid = QGridLayout()

        self.ok = QPushButton("Back")
        self.cancel = QPushButton("Close")

        self.connect(self.ok,SIGNAL("clicked()"),self.ok_func)
        self.connect(self.cancel,SIGNAL("clicked()"),self.cancel_func)
        #
        self.setGeometry(250,250,500,500)
        # self.setLayout(self.grid)
        self.table = QTableWidget()
        self.table.setRowCount(size)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(QString("User ID;No_Passengers;Flight ID;Schedule ID").split(";"));

        self.table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.table.resizeColumnsToContents()

        for i in range(size):
            self.table.setItem(i,0,QTableWidgetItem(res[i][0]))
            self.table.setItem(i,1,QTableWidgetItem(str(res[i][1])))
            self.table.setItem(i,2,QTableWidgetItem(res[i][2]))
            self.table.setItem(i,3,QTableWidgetItem(res[i][3]))


        self.grid.addWidget(self.table,0,0,1,-1)
        self.grid.addWidget(self.ok,1,3,1,1)
        self.grid.addWidget(self.cancel,1,4,1,1)

        self.setLayout(self.grid)

    def ok_func(self):
        self.id =  self.table.currentItem().text()
        #pass_ent = passenger_entry(self.id)
        #pass_ent.exec_()
        print "ticket"
    def cancel_func(self):
        self.close()
#
#
# app = QApplication(sys.argv)
# start = View_Reservations()
# start.show()
# app.exec_()