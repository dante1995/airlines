
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

class book_history(QDialog):
    def __init__(self,uid):
        super(book_history,self).__init__()
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

        #self.ok = QPushButton("Book Now")
        self.cancel = QPushButton("Cancel")

        #self.connect(self.ok,SIGNAL("clicked()"),self.ok_func)
        self.connect(self.cancel,SIGNAL("clicked()"),self.cancel_func)
        #

        try:
            self.cursor.execute("select user_id,flight_id,num_seats,flight_date,arrival,departure from user_book natural join booking natural join schedule where user_id = \""+str(self.uid)+"\";")
            user_result = self.cursor.fetchall()
            #print user_result
            #print len(user_result)
        except:
            print "hii"

        self.setGeometry(250,250,500,500)
        self.grid = QGridLayout()
        # self.setLayout(self.grid)
        self.table = QTableWidget()
        self.table.setRowCount(len(user_result))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(QString("Book ID;Flight No.;#Passengers ;Date;Arrival;Departure").split(";"));

        self.table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.table.resizeColumnsToContents()


        for i in range(len(user_result)):
            self.table.setItem(i,0,QTableWidgetItem(user_result[i][0]))
            self.table.setItem(i,1,QTableWidgetItem(user_result[i][1]))
            self.table.setItem(i,2,QTableWidgetItem(str(user_result[i][2])))
            self.table.setItem(i,3,QTableWidgetItem(str(user_result[i][3])))
            self.table.setItem(i,4,QTableWidgetItem(str(user_result[i][4])))
            self.table.setItem(i,5,QTableWidgetItem(str(user_result[i][5])))


        self.grid.addWidget(self.table,0,0,1,-1)
        # self.grid.addWidget(self.ok,1,3,1,1)
        self.grid.addWidget(self.cancel,1,4,1,1)

        self.setLayout(self.grid)

    # def ok_func(self):
    #     self.id =  self.table.currentItem().text()
    #     pass_ent = passenger_entry(self.id)
    #     pass_ent.exec_()
    #     print "ticket"
    def cancel_func(self):
        self.close()

#
#
# app = QApplication(sys.argv)
# start = book_history()
# start.show()
# app.exec_()
#
#
# if __name__ == '__main__':
#     main()