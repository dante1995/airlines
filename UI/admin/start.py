__author__ = 'root'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb
import time
import sys
import datetime
from route_add import *
from flight_add import *
from delay import *
from airport_add import *
from view_reservations import *
from view_userlist import *
from schedule_add import *

class Start(QDialog):
    def __init__(self):
        super(Start,self).__init__()
        self.initUI()

    def initUI(self):

        #while 1:
            # try:
            #     self.db = MySQLdb.connect("10.5.18.66","12CS10042","btech12","12CS10042")
            #     break
            # except:
            #     time.sleep(.1)
            #     continue

        # self.cursor = self.db.cursor()

        self.grid = QGridLayout()
       # self.grid.addWidget(temp,0,0)

        self.vbox = QVBoxLayout()
        self.route = QPushButton("Add Route")
        self.route.setFixedSize(300,30)
        self.flight = QPushButton("Add Flight")
        self.reservation = QPushButton("View Reservation")
        self.userlist = QPushButton("View Userlist")
        self.delay = QPushButton("Delay")
        self.airport = QPushButton("Add Airport")
        self.schedule = QPushButton("Add Schedule")
        self.route.setStyleSheet("color: black; background-color:gray")
        self.flight.setStyleSheet("color: black; background-color:gray")
        self.reservation.setStyleSheet("color: black; background-color:gray")
        self.userlist.setStyleSheet("color: black; background-color:gray")
        self.delay.setStyleSheet("color: black; background-color:gray")
        self.airport.setStyleSheet("color: black; background-color:gray")
        self.schedule.setStyleSheet("color: black; background-color:gray")

        temp = QLabel("")

        #self.vbox.addStretch(1)
        self.grid.setSpacing(10)
        self.grid.addWidget(self.route,0,1)
        self.grid.addWidget(self.flight,1,1)
        self.grid.addWidget(self.reservation,2,1)
        self.grid.addWidget(self.userlist,3,1)
        self.grid.addWidget(self.delay,4,1)
        self.grid.addWidget(self.airport,5,1)
        self.grid.addWidget(self.schedule,6,1)

        self.grid.addWidget(temp,0,0)
        self.grid.addWidget(temp,0,2)

        self.vbox = QHBoxLayout()
        self.hbox = QVBoxLayout()
        #self.vbox.addLayout(self.grid)
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.grid)
        self.hbox.addStretch(1)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(1)
        #self.grid.addWidget(self.vbox,0,1)


        self.setGeometry(250,250,500,500)
        self.setLayout(self.vbox)


        self.connect(self.route,SIGNAL("clicked()"),self.add_route_f)
        self.connect(self.flight,SIGNAL("clicked()"),self.add_flight_f)
        self.connect(self.reservation,SIGNAL("clicked()"),self.view_res_f)
        self.connect(self.userlist,SIGNAL("clicked()"),self.view_ul_f)
        self.connect(self.delay,SIGNAL("clicked()"),self.add_delay_f)
        self.connect(self.airport,SIGNAL("clicked()"),self.add_airp_f)
        self.connect(self.schedule,SIGNAL("clicked()"),self.add_sch_f)

    def add_route_f(self):
        r_add = Route_Add()
        r_add.exec_()

    def add_flight_f(self):
        r_fli = Flight_Add()
        r_fli.exec_()

    def view_res_f(self):
        resv = View_Reservations()
        resv.exec_()

    def view_ul_f(self):
        ul = View_Userlist()
        ul.exec_()

    def add_delay_f(self):
        delay = Delay()
        delay.exec_()

    def add_airp_f(self):
        air = Airport_Add()
        air.exec_()

    def add_sch_f(self):
        sch = Schedule_Add()
        sch.exec_()

# app = QApplication(sys.argv)
# start = Start()
# start.show()
# app.exec_()