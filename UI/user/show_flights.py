
__author__ = 'sabya'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui,QtCore
import MySQLdb
import time
import sys
import datetime
from passenger_entry import *
class show_flights(QDialog):
    def __init__(self,no,dest,source,date):
        super(show_flights,self).__init__()
        self.no = str(no)
        self.dest = str(dest)
        self.source = str(source)
        self.date = str(date)
        # print "no in show flights = " + self.no
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

        sql = "select airport_id from airport where name like \"%"+self.source+"%\";"
        # print sql
        self.cursor.execute(sql)
        sid = self.cursor.fetchall()

        sql = "select airport_id from airport where name like \"%"+self.dest+"%\";"
        self.cursor.execute(sql)
        did = self.cursor.fetchall()
        print did[0][0]
        # print (did[0][0]).split('\'')
        sql = "select flight_id, available, arrival, departure from schedule,route,airport as A,airport as B where flight_date = \""+ self.date + "\" and available >= "+ str(self.no) +" and A.city = \"" + str(self.source) +"\" and B.city = \""+str(self.dest)+ "\" and route.source = A.airport_id and route.destination = B.airport_id and schedule.route_id = route.route_id;"
        print sql
        self.cursor.execute(sql)
        results = self.cursor.fetchall()


        flights = ['dasd','fdgvdf ','dfewrf']
        source = ['dsv','fv','fv']
        dest = ['vcfsd','vd','dsvc']


        self.grid = QGridLayout()
        size = len(flights)


        self.ok = QPushButton("Book Now")
        self.cancel = QPushButton("Cancel")

        self.connect(self.ok,SIGNAL("clicked()"),self.ok_func)
        self.connect(self.cancel,SIGNAL("clicked()"),self.cancel_func)
        #
        self.setGeometry(250,250,500,500)
        # self.setLayout(self.grid)
        self.table = QTableWidget()
        self.table.setRowCount(size)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(QString("Flight ID;From;To ;Availability;Arrival;Departure").split(";"));

        self.table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.table.resizeColumnsToContents()

        for i in range(size):
            self.table.setItem(i,0,QTableWidgetItem(results[i][0]))
            self.table.setItem(i,1,QTableWidgetItem(self.source))
            self.table.setItem(i,2,QTableWidgetItem(self.dest))
            self.table.setItem(i,3,QTableWidgetItem(results[i][1]))
            self.table.setItem(i,4,QTableWidgetItem(results[i][2]))
            self.table.setItem(i,4,QTableWidgetItem(results[i][3]))


        self.grid.addWidget(self.table,0,0,1,-1)
        self.grid.addWidget(self.ok,1,3,1,1)
        self.grid.addWidget(self.cancel,1,4,1,1)

        self.setLayout(self.grid)

    def ok_func(self):
        self.id =  self.table.currentItem().text()
        pass_ent = passenger_entry(self.id, self.no)
        pass_ent.exec_()
        print "ticket"
    def cancel_func(self):
        self.close()


# def main():
#     app = QApplication(sys.argv)
#     start = show_flights()
#     start.show()
#     app.exec_()

#
#
# if __name__ == '__main__':
#     main()