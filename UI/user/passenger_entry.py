
__author__ = 'sabya'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui,QtCore
import MySQLdb
import time
import sys
import datetime
from book_window import *
from show_flights import *
from ticket import *

class passenger_entry(QDialog):
    def __init__(self,uid,id,no):
        super(passenger_entry,self).__init__()
        self.uid = uid
        self.id = str(id)
        self.no = str(no)
        print "my id is: " + self.id
        print "no in pass_entry = " + self.no
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


        # print "efvfdvfdgvdv"
        # print self.id
        self.grid = QGridLayout()


        self.ok = QPushButton("Book Now")
        self.cancel = QPushButton("Cancel")

        self.connect(self.ok,SIGNAL("clicked()"),self.ok_func)
        self.connect(self.cancel,SIGNAL("clicked()"),self.cancel_func)
        #
        self.setGeometry(250,250,500,500)
        # self.setLayout(self.grid)
        self.table = QTableWidget()
        self.table.setRowCount(int(self.no))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(QString("Name;Age;Gender;Senior Citizen").split(";"));
        for i in range(int(self.no)):
            self.gender = QComboBox()
            self.gender.addItem("Male")
            self.gender.addItem("Female")
            self.dis = QComboBox()
            self.dis.addItem("Yes")
            self.dis.addItem("No")
            self.table.setCellWidget(i,2,self.gender)
            self.table.setCellWidget(i,3,self.dis)

        self.table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.table.resizeColumnsToContents()


        self.grid.addWidget(self.table,0,0,1,-1)
        self.grid.addWidget(self.ok,1,3,1,1)
        self.grid.addWidget(self.cancel,1,4,1,1)

        self.setLayout(self.grid)

    def ok_func(self):
        names = []
        ages = []
        genders = []
        seniors = []
        allRows = self.table.rowCount()
        for row in xrange(0, allRows):
            name = self.table.item(row,0).text()
            age = self.table.item(row,1).text()
            gender = self.table.cellWidget(row,2).currentText()
            senior = self.table.cellWidget(row,3).currentText()
            names.append(str(name))
            ages.append(str(age))
            genders.append(str(gender))
            seniors.append(str(senior))
        sql = "select available from schedule where schedule_id = \"" +str(self.id)+ "\";"
        print sql
        self.cursor.execute(sql)
        available = self.cursor.fetchall()
        available = (int(available[0][0]))

        sql = "select seat from passenger natural join passenger_book natural join booking natural join schedule where schedule_id = \"" +str(self.id) +"\";"
        self.cursor.execute(sql)
        passengers = self.cursor.fetchall()
        size = len(passengers)

        tmp = []
        for i in passengers:
            tmp.append(int(i[0]))
        print tmp
        sql = "select booking_id from booking;"
        self.cursor.execute(sql)
        bookings = self.cursor.fetchall()
        booking_id = len(bookings) + 1

        sql = "insert into booking values(%s,%s,%s);"%("\"" + str(booking_id) + "\"","\"" + str(self.no) + "\"","\"" + str(self.id) + "\"")
        self.cursor.execute(sql)

        sql = "insert into user_book values (%s,%s);"%("\"" + str(self.uid) + "\"","\"" + str(booking_id) + "\"")
        self.cursor.execute(sql)
        seat = -1
        sql = "select passenger_id from passenger;"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        size = len(res)
        id = int(size)+1
        for i in range(int(self.no)):
            for yu in range(1,1000):
                if yu not in tmp:
                    seat = yu
                    tmp.append(yu)
                    break

            sql = "insert into passenger values (%s,%s,%s,%s,%s,%s);"%("\""+str(id+i)+"\"","\""+str(names[i])+"\"","\""+str(ages[i])+"\"","\""+str(genders[i])+"\"","\""+str(seniors[i])+"\"","\""+str(seat)+"\"")
            print sql
            self.cursor.execute(sql)
            sql = "insert into passenger_book values (%s,%s);"%("\"" + str(booking_id) + "\"","\"" + str(id+i) + "\"")
            self.cursor.execute(sql)

        sql = "update schedule set available = "+(str(available - int(self.no)))+" where schedule_id = \"" + str(self.id)+"\";"
        self.cursor.execute(sql)
        self.db.commit()
        tick = ticket(booking_id,self.id)
        tick.exec_()
        self.close()

    def cancel_func(self):
        self.close()

# app = QApplication(sys.argv)
# start = passenger_entry("ab12","QE356201","2")
# start.show()
# app.exec_()
