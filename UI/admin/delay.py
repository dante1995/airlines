# __author__ = 'sabya'
#
#
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
# import MySQLdb
# import time
# import sys
# import datetime
#
#
# class Delay(QFrame):
#     def __init__(self):
#         super(Delay,self).__init__()
#         self.initUI()
#
#     def initUI(self):
#
#         while 1:
#             try:
#                 self.db = MySQLdb.connect("10.5.18.66","12CS10041","btech12","12CS10041")
#                 break
#             except:
#                 time.sleep(.1)
#                 continue
#
#         self.cursor = self.db.cursor()
#
#         self.fid = QLabel("Flight ID")
#         self.ifid = QLineEdit()
#         self.ifid.setPlaceholderText("Enter Flight ID")
#         self.date = QLabel("Date")
#         self.idate = QLineEdit()
#         self.idate.setPlaceholderText("Enter Date")
#         self.delay = QLabel("Delay")
#         self.idelay = QLineEdit()
#         self.idelay.setPlaceholderText("Enter Delay Duration")
#         self.temp = QLabel("")

#         self.setGeometry(250,250,500,500)
#
#         self.fid.setFixedWidth(200)
#         self.idate.setFixedWidth(200)
#         self.idelay.setFixedWidth(200)
#
#         self.fid.setAlignment(Qt.AlignRight | Qt.AlignCenter)
#         self.date.setAlignment(Qt.AlignRight | Qt.AlignCenter)
#         self.delay.setAlignment(Qt.AlignRight | Qt.AlignCenter)
#
#         self.grid = QGridLayout()
#         self.grid.addWidget(self.fid,0,0)
#         self.grid.addWidget(self.ifid,0,1)
#         self.grid.addWidget(self.date,1,0)
#         self.grid.addWidget(self.idate,1,1)
#         self.grid.addWidget(self.delay,2,0)
#         self.grid.addWidget(self.idelay,2,1)
#         self.grid.addWidget(self.temp,2,2)
#
#         self.hbox = QHBoxLayout()
#         self.reset = QPushButton("Reset")
#         self.update = QPushButton("Update")
#         self.update.setStyleSheet("color: black; background-color:gray")
#         self.reset.setStyleSheet("color: black; background-color:gray")
#         self.cancel = QPushButton("Cancel")
#         self.cancel.setStyleSheet("color: balck; background-color:gray")
#
#         self.hbox.addStretch(1)
#         self.hbox.addWidget(self.reset)
#         self.hbox.addWidget(self.update)
#         self.hbox.addWidget(self.cancel)
#         self.hbox.addStretch(1)
#
#         self.vbox = QVBoxLayout()
#         self.vbox.addLayout(self.grid)
#         self.vbox.addLayout(self.hbox)
#
#         self.setLayout(self.vbox)
#
#
#         self.connect(self.update,SIGNAL("clicked()"),self.entry)
#         self.connect(self.reset,SIGNAL("clicked()"),self.reset_all)
#         self.connect(self.cancel,SIGNAL("clicked()"),self.canceli)
#
#
#     def canceli(self):
#         self.db.close()
#         start.close()
#
#     def entry(self):
#         id_flight = str(self.ifid.text())
#         date = str(self.idate.text())
#         delay = str(self.idelay.text())
#
#         if(delay.isdigit() == 0):
#             message = QMessageBox(QMessageBox.Warning,"Error Message","Room must be an integer. Try Again",buttons = QMessageBox.Close)
#             message.exec_()
#             return
#
#         self.cursor.execute("select RoomNo,Building from Room")
#         result = self.cursor.fetchall()
#         for i in range(len(result)):
#             if str(result[i][0]) == room and str(result[i][1]) == building:
#                 message = QMessageBox(QMessageBox.Warning,"Error Message","This room in already entered. Try Again",buttons = QMessageBox.Close)
#                 message.exec_()
#                 return
#
#         try:
#             self.cursor.execute("insert into Room(RoomNo,Building,Department,Purpose) values('%s','%s','%s','%s')"%(room,building,dept,prps))
#             self.db.commit()
#             self.reset_all()
#         except:
#             self.db.rollback()
#             message = QMessageBox(QMessageBox.Warning,"Prescribe Message","Some error occured. Try Again",buttons = QMessageBox.Close)
#             message.exec_()
#
#
#
#
#
#     def reset_all(self):
#         self.ifid.clear()
#         self.idate.clear()
#         self.idelay.clear()
#
#
#
# app = QApplication(sys.argv)
# start = Delay()
# start.show()
# app.exec_()
# __author__ = 'root'
