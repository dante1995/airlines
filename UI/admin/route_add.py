__author__ = 'sabya'


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb
import time
import sys
import datetime


class Route_Add(QFrame):
    def __init__(self):
        super(Route_Add,self).__init__()
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

        self.rt = QLabel("Route ID")
        self.irt = QLineEdit()
        self.irt.setPlaceholderText("Enter Route ID")
        self.src = QLabel("Source")
        self.isrc = QLineEdit()
        self.isrc.setPlaceholderText("Enter Source Airport")
        self.to = QLabel("Destination")
        self.ito = QLineEdit()
        self.ito.setPlaceholderText("Enter Destination Airport")
        self.temp = QLabel("")

        self.irt.setFixedWidth(200)
        self.isrc.setFixedWidth(200)
        self.ito.setFixedWidth(200)

        self.rt.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.src.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.to.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.grid = QGridLayout()
        self.grid.addWidget(self.rt,0,0)
        self.grid.addWidget(self.irt,0,1)
        self.grid.addWidget(self.src,1,0)
        self.grid.addWidget(self.isrc,1,1)
        self.grid.addWidget(self.to,2,0)
        self.grid.addWidget(self.ito,2,1)
        self.grid.addWidget(self.temp,2,2)

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
        id_route = str(self.irt.text())
        source = str(self.isrc.text())
        destination = str(self.ito.text())

        if(len(source)) == 0 or len(destination)==0:
            message = QMessageBox(QMessageBox.Warning,"Error Message","Please enter Full details. Try Again",buttons = QMessageBox.Close)
            message.exec_()
            return


        self.cursor.execute("select route_id from route")
        result = self.cursor.fetchall()
        for i in range(len(result)):
            if str(result[i]) == id_route:
                message = QMessageBox(QMessageBox.Warning,"Error Message","This id_route in already entered. Try Again",buttons = QMessageBox.Close)
                message.exec_()
                return

        try:
            self.cursor.execute("insert into route(route_id,source,destination) values('%s','%s','%s')"%(id_route,source,destination))
            self.db.commit()
            self.reset_all()
        except:
            self.db.rollback()
            message = QMessageBox(QMessageBox.Warning,"Prescribe Message","Some error occured. Try Again",buttons = QMessageBox.Close)
            message.exec_()





    def reset_all(self):
        self.irt.clear()
        self.isrc.clear()
        self.ito.clear()



app = QApplication(sys.argv)
start = Route_Add()
start.show()
app.exec_()
