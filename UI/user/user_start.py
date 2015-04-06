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

        self.id = QLabel("Username ")
        self.iid = QLineEdit()
        self.iid.setPlaceholderText("Enter Username")

        self.password = QLabel("Password")
        self.ipassword = QLineEdit()
        self.temp = QLabel("")


        self.iid.setFixedWidth(200)
        self.ipassword.setFixedWidth(200)

        self.id.setAlignment(  Qt.AlignCenter)
        self.password.setAlignment( Qt.AlignCenter)
        self.grid = QGridLayout()
        self.grid.addWidget(self.id,0,0)
        self.grid.addWidget(self.iid,0,1)
        self.grid.addWidget(self.password,1,0)
        self.grid.addWidget(self.ipassword,1,1)

        self.hbox = QHBoxLayout()
        self.login = QPushButton("Login")
        self.signup = QPushButton("Signup")
        self.login.setStyleSheet("color: black; background-color:gray")
        self.signup.setStyleSheet("color: black; background-color:gray")

        self.hbox.addStretch(1)
        self.hbox.addWidget(self.login)
        self.hbox.addWidget(self.signup)
        self.hbox.addStretch(1)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.grid)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)


        self.connect(self.login,SIGNAL("clicked()"),self.login_func)
        self.connect(self.signup,SIGNAL("clicked()"),self.signup_func)

    def login_func (self):
        self.db.close()
        start.close()

    def signup_func(self):
        start.close()



app = QApplication(sys.argv)
start = user_start()
start.show()
app.exec_()
