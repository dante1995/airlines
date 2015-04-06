__author__ = 'sabya'


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb
import time
import sys
import datetime


class Airport_Add(QFrame):
    def __init__(self):
        super(Airport_Add,self).__init__()
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

        self.aid = QLabel("Airport ID")
        self.iaid = QLineEdit()
        self.iaid.setPlaceholderText("Enter Airport ID")
        self.aname = QLabel("Airport Name")
        self.ianame = QLineEdit()
        self.ianame.setPlaceholderText("Enter Airport Name")
        self.city = QLabel("City")
        self.icity = QLineEdit()
        self.icity.setPlaceholderText("Enter City Name")
        self.state = QLabel("State")
        self.istate = QLineEdit()
        self.istate.setPlaceholderText("Enter State Name")
        self.temp = QLabel("")

        self.iaid.setFixedWidth(200)
        self.ianame.setFixedWidth(200)
        self.icity.setFixedWidth(200)
        self.istate.setFixedWidth(200)

        self.aid.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.aname.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.city.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.state.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.grid = QGridLayout()
        self.grid.addWidget(self.aid,0,0)
        self.grid.addWidget(self.iaid,0,1)
        self.grid.addWidget(self.aname,1,0)
        self.grid.addWidget(self.ianame,1,1)
        self.grid.addWidget(self.city,2,0)
        self.grid.addWidget(self.icity,2,1)
        self.grid.addWidget(self.state,3,0)
        self.grid.addWidget(self.istate,3,1)
        self.grid.addWidget(self.temp,3,2)

        self.hbox = QHBoxLayout()
        self.reset = QPushButton("Reset")
        self.update = QPushButton("Update")
        self.update.setStyleSheet("color: black; background-color:gray")
        self.reset.setStyleSheet("color: black; background-color:gray")
        self.cancel = QPushButton("Cancel")
        self.cancel.setStyleSheet("color: balck; background-color:gray")

        self.hbox.addStretch(1)
        self.hbox.addWidget(self.reset)
        self.hbox.addWidget(self.update)
        self.hbox.addWidget(self.cancel)
        self.hbox.addStretch(1)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.grid)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)


        self.connect(self.update,SIGNAL("clicked()"),self.entry)
        self.connect(self.reset,SIGNAL("clicked()"),self.reset_all)
        self.connect(self.cancel,SIGNAL("clicked()"),self.canceli)


    def canceli(self):
        self.db.close()
        start.close()

    def entry(self):
        airport_id = str(self.iaid.text())
        airport_name = str(self.ianame.text())
        city = str(self.icity.text())
        state = str(self.istate.text())

        if(len(airport_name) == 0 or len(city)==0 or len(state)==0):
            message = QMessageBox(QMessageBox.Warning,"Error Message","Please enter Full details. Try Again",buttons = QMessageBox.Close)
            message.exec_()
            return


        self.cursor.execute("select airport_id from airport")
        result = self.cursor.fetchall()
        for i in range(len(result)):
            if str(result[i]) == airport_id:
                message = QMessageBox(QMessageBox.Warning,"Error Message","This room in airport id entered. Try Again",buttons = QMessageBox.Close)
                message.exec_()
                return

        try:
            self.cursor.execute("insert into airport(airport_id,name,city,state) values('%s','%s','%s','%s')"%(airport_id,airport_name,city,state))
            self.db.commit()
            self.reset_all()
        except:
            self.db.rollback()
            message = QMessageBox(QMessageBox.Warning,"Prescribe Message","Some error occured. Try Again",buttons = QMessageBox.Close)
            message.exec_()





    def reset_all(self):
        self.iaid.clear()
        self.ianame.clear()
        self.icity.clear()
        self.istate.clear()



app = QApplication(sys.argv)
start = Airport_Add()
start.show()
app.exec_()
