__author__ = 'sabya'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb
import time
import sys
import datetime
from book_window import *

class after_log(QDialog):
    def __init__(self,uid):
        super(after_log,self).__init__()
        self.uid = uid
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
        self.temp = QLabel("")

        self.book.setStyleSheet("color: black; background-color:gray")
        self.cancel.setStyleSheet("color: black; background-color:gray")
        self.showtran.setStyleSheet("color: black; background-color:gray")

        self.grid = QGridLayout()
        self.grid.addWidget(self.temp,0,1)
        self.grid.addWidget(self.temp,3,1)

        self.grid.addWidget(self.book,1,1)
        self.grid.addWidget(self.cancel,2,1)
        self.grid.addWidget(self.showtran,3,1)
        self.grid.addWidget(self.temp,4,0)
        self.grid.addWidget(self.temp,4,2)

        self.connect(self.book,SIGNAL("clicked()"),self.book_func)
        self.connect(self.cancel,SIGNAL("clicked()"),self.cancel_func)
        self.connect(self.showtran,SIGNAL("clicked()"),self.showtran_func)

        self.setLayout(self.grid)


    def book_func(self):
        book = book_window(self.uid)
        book.exec_()


    def cancel_func(self):
        x = 5

    def showtran_func(self):
        x = 5
