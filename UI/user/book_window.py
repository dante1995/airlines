__author__ = 'sabya'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MySQLdb
import time
import sys
import datetime
from user import *
from show_flights import *
from datetime import timedelta
global gl_date
class book_window(QDialog):
    def __init__(self,uid):
        super(book_window,self).__init__()
        self.uid = uid
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
        completer = QCompleter()

        model = QStringListModel()
        completer.setModel(model)
        self.get_data(model)

        self.fro = QLabel("From")
        self.ifro = QLineEdit()
        self.ifro.setCompleter(completer)

        self.ifro.setPlaceholderText("Enter Start Airport")

        self.dest = QLabel("To")
        self.idest = QLineEdit()
        self.idest.setCompleter(completer)
        self.idest.setPlaceholderText("Enter Destination Airport")

        self.date = QLabel("Date")
        self.idate = QLineEdit()


        self.no_passengers = QLabel("No of passengers")
        self.ino_passengers = QLineEdit()
        self.cal = QPushButton()
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
        self.grid.addWidget(self.cal,2,2)
        self.grid.addWidget(self.no_passengers,3,0)
        self.grid.addWidget(self.ino_passengers,3,1)
        self.grid.addWidget(self.temp,3,2)

        self.hbox = QHBoxLayout()
        self.book = QPushButton("Show flights")
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
        self.connect(self.cal,SIGNAL("clicked()"),self.cal_func)

    def book_func (self):
        self.no = self.ino_passengers.text()
        self.des = self.idest.text()
        self.src = self.ifro.text()
        self.dt = self.idate.text()
        sw = show_flights(self.uid,self.no,self.des,self.src,self.dt)


        sw.exec_()
        print "yo"
    def reset_func(self):
        self.ifro.clear()
        self.idest.clear()
        self.idate.clear()
        self.ino_passengers.clear()

    def cal_func(self):
        print "yo"
        gui = Calendar()
        gui.exec_()
        self.idate.setText(str(gui.aweeklater))
    def get_data(self,model):
        self.cursor.execute("select distinct city from airport;")
        result = self.cursor.fetchall()
        data = []
        for x in result:
            data.append(x[0])
        print data
        model.setStringList(data)

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



# def main():
#
#     app = QApplication(sys.argv)
#     start = book_window()
#     start.show()
#     app.exec_()
#
#
# if __name__ == '__main__':
#     main()



