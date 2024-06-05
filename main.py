import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from UI_framework import UI_bttns
from PyQt5.QtCore import QDate, QTimer, QTimer, QTime, Qt

class POS_UI(QDialog):
    def __init__(self):
        super(POS_UI,self).__init__()
        self.widget=QtWidgets.QStackedWidget()
        loadUi("POS.ui",self)
        self.displayDateTime()
        UI_bttns(self)
        
        self.bttn_exit.clicked.connect(QApplication.quit)

    #displaying date and time
    def displayDateTime(self):
        now = QDate.currentDate()
        self.lblDate.setText(now.toString(Qt.DefaultLocaleLongDate))
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

    def showTime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.lblTime.setText(label_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = POS_UI()
    dialog.setFixedWidth(1560)
    dialog.setFixedHeight(950)
    dialog.show()
    sys.exit(app.exec_())
