
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
class passenger_entry(QDialog):
    def __init__(self,id,no):
        super(passenger_entry,self).__init__()
        self.id = str(id)
        self.no = str(no)
        print "my id is: " + self.id
        print "no in pass_entry = " + self.no
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
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(QString("Name;Age;Gender").split(";"));
        for i in range(10):
            self.gender = QComboBox()
            self.gender.addItem("Male")
            self.gender.addItem("Female")

            self.table.setCellWidget(i,2,self.gender)


        self.table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.table.resizeColumnsToContents()


        self.grid.addWidget(self.table,0,0,1,-1)
        self.grid.addWidget(self.ok,1,3,1,1)
        self.grid.addWidget(self.cancel,1,4,1,1)

        self.setLayout(self.grid)

    def ok_func(self):
        self.names = []
        self.ages = []
        self.genders = []
        for i in range(int(self.no)):
            name = ""
            gender = ""
            age = ""
            name = self.table.item(i,0)
            gender = self.table.item(i,2)
            age = self.table.item(i,1)
            print name,age,gender
            print name.text(),age.text(),gender.text()
        # print self.names,self.ages,self.genders

    def cancel_func(self):
        self.close()
        x=3



def main():

    app = QApplication(sys.argv)
    start = passenger_entry(2,4)
    start.show()
    app.exec_()


if __name__ == '__main__':
    main()
