__author__ = 'sabya'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb
import time
import sys
import datetime
from user import *

class user_start(QFrame):
    def __init__(self):
        super(user_start,self).__init__()
        self.initUI()

    def initUI(self):

        # while 1:
        #     try:
        #         self.db = MySQLdb.connect("10.5.18.66","12CS10042","btech12","12CS10042")
        #         break
        #     except:
        #         time.sleep(.1)
        #         continue

        # self.cursor = self.db.cursor()


        self.book = QPushButton("Book Ticket")
        self.cancel = QPushButton("Cancel Ticket")
        self.showtran = QPushButton("Show Transactions")

        self.book.setStyleSheet("color: black; background-color:gray")
        self.cancel.setStyleSheet("color: black; background-color:gray")
        self.showtran.setStyleSheet("color: black; background-color:gray")

        self.grid = QGridLayout()
        self.grid.addWidget(self.book,0,0)
        self.grid.addWidget(self.cancel,1,0)
        self.grid.addWidget(self.showtran,2,0)

        self.connect(self.book,SIGNAL("clicked()"),self.book_func)
        self.connect(self.cancel,SIGNAL("clicked()"),self.cancel_func)
        self.connect(self.showtran,SIGNAL("clicked()"),self.showtran_func)

        self.setLayout(self.grid)


    def book_func(self):
        start.close()

    def cancel_func(self):
        start.close()

    def showtran_func(self):
        start.close()



app = QApplication(sys.argv)
start = user_start()
start.show()
app.exec_()
