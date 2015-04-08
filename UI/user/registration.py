__author__ = 'sabya'


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb
import time
import sys
import datetime


class registration(QDialog):
    def __init__(self):
        super(registration,self).__init__()
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

        self.name = QLabel("Name")
        self.iname = QLineEdit()
        self.iname.setPlaceholderText("Enter name")
        
        self.address = QLabel("Address")
        self.iaddress = QLineEdit()
        self.iaddress.setPlaceholderText("Enter Address")

        self.mob = QLabel("Mobile no")
        self.imob = QLineEdit()
        self.imob.setPlaceholderText("Enter 10 digit mobile no")

        self.uname = QLabel("Username")
        self.iuname = QLineEdit()
        self.iuname.setPlaceholderText("Enter username")

        self.passwd = QLabel("Password")
        self.ipasswd = QLineEdit()

        self.email = QLabel("Email")
        self.iemail = QLineEdit()
        self.iemail.setPlaceholderText("Enter email id")

        self.gender = QLabel("Gender")
        self.igender = QComboBox()
        self.igender.addItem("Male")
        self.igender.addItem("Female")

        self.temp = QLabel("")

        self.iname.setFixedWidth(200)
        self.iaddress.setFixedWidth(400)
        self.imob.setFixedWidth(200)
        self.iuname.setFixedWidth(200)
        self.ipasswd.setFixedWidth(200)
        self.iemail.setFixedWidth(200)
        self.igender.setFixedWidth(100)

        self.name.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.address.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.mob.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.uname.setAlignment(Qt.AlignRight|Qt.AlignCenter)
        self.passwd.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.email.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.grid = QGridLayout()
        self.grid.addWidget(self.name,0,0)
        self.grid.addWidget(self.iname,0,1)
        self.grid.addWidget(self.address,1,0)
        self.grid.addWidget(self.iaddress,1,1)
        self.grid.addWidget(self.mob,2,0)
        self.grid.addWidget(self.imob,2,1)
        self.grid.addWidget(self.uname,3,0)
        self.grid.addWidget(self.iuname,3,1)
        self.grid.addWidget(self.passwd,4,0)
        self.grid.addWidget(self.ipasswd,4,1)
        self.grid.addWidget(self.email,5,0)
        self.grid.addWidget(self.iemail,5,1)
        self.grid.addWidget(self.temp,6,2)
        self.grid.addWidget(self.gender,6,0)
        self.grid.addWidget(self.igender,6,1)
        self.hbox = QHBoxLayout()
        self.reset = QPushButton("Reset")
        self.enter = QPushButton("Enter")
        self.enter.setStyleSheet("color: black; background-color:gray")
        self.reset.setStyleSheet("color: black; background-color:gray")

        self.hbox.addStretch(1)
        self.hbox.addWidget(self.reset)
        self.hbox.addWidget(self.enter)
        self.hbox.addStretch(1)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.grid)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)


        self.connect(self.enter,SIGNAL("clicked()"),self.entry)
        self.connect(self.reset,SIGNAL("clicked()"),self.reset_all)


    def entry(self):
        name = str(self.iname.text())
        addr = str(self.iaddress.text())
        mob = str(self.imob.text())
        uname = str(self.iuname.text())
        pwd = str(self.ipasswd.text())
        email = str(self.iemail.text())
        gender = str(self.igender.currentText())
        dob = " "
        try:
            self.cursor.execute("insert into user (user_id,password,name,phone,email_id,gender,dob)values('%s','%s','%s','%s','%s','%s','%s')"%(uname,pwd,name,mob,email,gender,dob))
            self.db.commit()
            message = QMessageBox(QMessageBox.Warning,"Success","User added",buttons = QMessageBox.Close)
            self.reset_all()
        except:
            self.db.rollback()
            message = QMessageBox(QMessageBox.Warning,"Prescribe Message","Some error occured. Try Again",buttons = QMessageBox.Close)
            message.exec_()

        self.close()


    def reset_all(self):
        self.iname.clear()
        self.iaddress.clear()
        self.imob.clear()
        self.close()




