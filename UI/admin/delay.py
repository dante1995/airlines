__author__ = 'sabya'


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb
import time
import sys
import datetime
import time
from datetime import *
from PyQt4 import QtGui,QtCore
class Delay(QFrame):
    def __init__(self):
        super(Delay,self).__init__()
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

        self.fid = QLabel("Flight ID")
        self.ifid = QLineEdit()
        self.ifid.setPlaceholderText("Enter Flight ID")
        self.date = QLabel("Date")
        self.idate = QLineEdit()
        self.idate.setPlaceholderText("Enter Date")
        self.delay = QLabel("Delay")
        self.idelay = QLineEdit()
        self.idelay.setPlaceholderText("Enter Delay Duration(in mins)")
        self.temp = QLabel("")
        self.cal = QPushButton("CAL")

        self.setGeometry(250,250,500,500)

        self.fid.setFixedWidth(200)
        self.idate.setFixedWidth(200)
        self.idelay.setFixedWidth(200)

        self.fid.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.date.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.delay.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        self.grid = QGridLayout()
        self.grid.addWidget(self.fid,0,0)
        self.grid.addWidget(self.ifid,0,1)
        self.grid.addWidget(self.date,1,0)
        self.grid.addWidget(self.idate,1,1)
        self.grid.addWidget(self.delay,2,0)
        self.grid.addWidget(self.idelay,2,1)
        # self.grid.addWidget(self.temp,2,2)
        self.grid.addWidget(self.cal,1,2)

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
        self.connect(self.cal,SIGNAL("clicked()"),self.cal_func)

    def cal_func(self):
        print "yo"
        gui = Calendar()
        gui.exec_()
        self.idate.setText(str(gui.aweeklater))

    def canceli(self):
        self.db.close()
        self.close()

    def entry(self):
        id_flight = str(self.ifid.text())
        date = str(self.idate.text())
        delay = str(self.idelay.text())

        if(delay.isdigit() == 0):
            message = QMessageBox(QMessageBox.Warning,"Error Message","Delay must be an integer. Try Again",buttons = QMessageBox.Close)
            message.exec_()
            return

        self.cursor.execute("select flight_id from flight")
        result = self.cursor.fetchall()

        flag=0
        for i in range(len(result)):
            if str(result[i][0]) == id_flight:
                flag=1
                break

        if flag==0:
            message = QMessageBox(QMessageBox.Warning,"Error Message","This flight_id is not present in the database. Try Again",buttons = QMessageBox.Close)
            message.exec_()
            return

        try:
            self.cursor.execute("select schedule_id,departure,arrival from schedule where flight_id=\'"+id_flight+"\' and flight_date=\'"+date+"\'")
            r1=self.cursor.fetchall()

            #print type(r1[0][1])
            for j in range(len(r1)):
                a = time.strptime(str(r1[j][1]), "%H:%M:%S")
                dep_sec=(datetime.timedelta(hours=a.tm_hour, minutes=a.tm_min, seconds=a.tm_sec).seconds)+(int(delay)*60)
                dep_hrs=datetime.timedelta(seconds=dep_sec)

                b = time.strptime(str(r1[j][2]), "%H:%M:%S")
                arr_sec=(datetime.timedelta(hours=b.tm_hour, minutes=b.tm_min, seconds=b.tm_sec).seconds)+(int(delay)*60)
                arr_hrs=datetime.timedelta(seconds=arr_sec)

                print dep_hrs
                print arr_hrs
                self.cursor.execute("update schedule set departure=\'"+str(dep_hrs)+"\' where schedule_id=\'"+r1[j][0]+"\' ")
                self.cursor.execute("update schedule set arrival=\'"+str(arr_hrs)+"\' where schedule_id=\'"+r1[j][0]+"\' ")
                self.db.commit()
                self.reset_all()
        except:
            self.db.rollback()
            message = QMessageBox(QMessageBox.Warning,"Prescribe Message","Some error occured. Try Again",buttons = QMessageBox.Close)
            message.exec_()





    def reset_all(self):
        self.ifid.clear()
        self.idate.clear()
        self.idelay.clear()



class Calendar(QDialog):
    """
    A QCalendarWidget example
    """

    def __init__(self):
        # create GUI
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('Calendar widget')
        # Set the window dimensions
        self.resize(300,100)

        # vertical layout for widgets
        self.vbox = QtGui.QVBoxLayout()
        self.setLayout(self.vbox)

        # Create a calendar widget and add it to our layout
        self.cal = QtGui.QCalendarWidget()
        self.vbox.addWidget(self.cal)

        # Create a label which we will use to show the date a week from now
        self.lbl = QtGui.QLabel()
        self.vbox.addWidget(self.lbl)

        # Connect the clicked signal to the centre handler
        self.connect(self.cal, QtCore.SIGNAL('selectionChanged()'), self.date_changed)

    def date_changed(self):
        """
        Handler called when the date selection has changed
        """
        # Fetch the currently selected date, this is a QDate object
        date = self.cal.selectedDate()

        # This is a gives us the date contained in the QDate as a native
        # python date[time] object
        pydate = date.toPyDate()
        # Calculate the date a week from now
        sevendays = timedelta(days=7)
        self.aweeklater = pydate
#
# def main():
#
#     app = QApplication(sys.argv)
#     start = Delay()
#     start.show()
#     app.exec_()
#
#
# if __name__ == '__main__':
#     main()