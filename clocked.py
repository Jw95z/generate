
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from threading import Timer

import time



 
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
 
class CWidget(QWidget):
 
    def __init__(self):
 
        super().__init__()
        self.year = QLCDNumber(self)        
        self.month = QLCDNumber(self)
        self.day = QLCDNumber(self)
        self.hour = QLCDNumber(self)
        self.min = QLCDNumber(self)
        self.sec = QLCDNumber(self)
        self.initUI()
 
 
    def initUI(self):        
         
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.year)
        hbox1.addWidget(self.month)
        hbox1.addWidget(self.day)
 
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.hour)
        hbox2.addWidget(self.min)
        hbox2.addWidget(self.sec)
 
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
 
        self.setLayout(vbox)
 
        self.setWindowTitle('clock')
        self.setGeometry(200,200, 400, 200)  
 
        self.showtime()
 
    def showtime(self):
        
        t = time.time()
        
        a = time.localtime(t)
        
        self.year.display(a.tm_year)
        self.month.display(a.tm_mon)
        self.day.display(a.tm_mday)
        self.hour.display(a.tm_hour)
        self.min.display(a.tm_min)
        self.sec.display(a.tm_sec)
        timer = Timer(1, self.showtime)
        timer.start()
 
 
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    w = CWidget()
    w.show()    
    sys.exit(app.exec_())