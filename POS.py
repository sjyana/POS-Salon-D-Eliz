import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from UI_framework import UI_bttns

class POS_UI(QDialog):
    def __init__(self):
        super(POS_UI,self).__init__()
        self.widget=QtWidgets.QStackedWidget()
        loadUi("POS.ui",self)

        UI_bttns(self)
        self.bttn_exit.clicked.connect(QApplication.quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = POS_UI()
    dialog.setFixedWidth(1560)
    dialog.setFixedHeight(950)
    dialog.show()
    sys.exit(app.exec_())
