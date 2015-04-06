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

        while 1:
            try:
                self.db = MySQLdb.connect("10.5.18.66","12CS10042","btech12","12CS10042")
                break
            except:
                time.sleep(.1)
                continue

        self.cursor = self.db.cursor()

        self.fro = QLabel("From")
        self.ifro = QLineEdit()
        self.ifro.setPlaceholderText("Enter Start Airport")

        self.dest = QLabel("To")
        self.idest = QLineEdit()
        self.idest.setPlaceholderText("Enter Destination Airport")

        self.date = QLabel("Date")
        self.idate = QLineEdit()

        self.no_passengers = QLabel("No of passengers")
        self.ino_passengers = QLineEdit()

        self.temp = QLabel("")


        self.ifro.setFixedWidth(200)
        self.idest.setFixedWidth(200)
        self.idate.setFixedWidth(200)
        self.ino_passengers.setFixedWidth(50)

        self.fro.setAlignment(Qt.AlignRight |  Qt.AlignCenter)
        self.dest.setAlignment(Qt.AlignRight |  Qt.AlignCenter)
        self.date.setAlignment(Qt.AlignRight |  Qt.AlignCenter)
        self.no_passengers.setAlignment(Qt.AlignRight |  Qt.AlignCenter)

        self.grid = QGridLayout()
        self.grid.addWidget(self.fro,0,0)
        self.grid.addWidget(self.ifro,0,1)
        self.grid.addWidget(self.dest,1,0)
        self.grid.addWidget(self.idest,1,1)
        self.grid.addWidget(self.date,2,0)
        self.grid.addWidget(self.idate,2,1)
        self.grid.addWidget(self.no_passengers,3,0)
        self.grid.addWidget(self.ino_passengers,3,1)
        self.grid.addWidget(self.temp,3,2)

        self.hbox = QHBoxLayout()
        self.book = QPushButton("Book")
        self.reset = QPushButton("Reset")
        self.book.setStyleSheet("color: black; background-color:gray")
        self.reset.setStyleSheet("color: black; background-color:gray")

        self.hbox.addStretch(1)
        self.hbox.addWidget(self.book)
        self.hbox.addWidget(self.reset)
        self.hbox.addStretch(1)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.grid)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)


        self.connect(self.book,SIGNAL("clicked()"),self.book_func)
        self.connect(self.reset,SIGNAL("clicked()"),self.reset_func)

    def book_func (self):
        self.db.close()
        start.close()

    def reset_func(self):
        self.ifro.clear()
        self.idest.clear()
        self.idate.clear()
        self.ino_passengers.clear()


app = QApplication(sys.argv)
start = user_start()
start.show()
app.exec_()
