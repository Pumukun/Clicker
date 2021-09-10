from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QIcon
from design import Ui_MainWindow
import sys

cnt = 1


class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.ui = Ui_MainWindow()   
        self.ui.setupUi(self)
        self.init_UI()
        self.ui.clickB.clicked.connect(self.change_label_txt)
        self.ui.clickB_2.clicked.connect(self.cnt_refresh)

    def init_UI(self):
        self.setWindowTitle('Clicker')
        self.setWindowIcon(QIcon('icon.png'))

    def change_label_txt(self):
        global cnt
        self.ui.count.setText(str(cnt))
        cnt += 1

    def cnt_refresh(self):
        global cnt
        cnt = 1
        self.ui.count.setText('0')


app = QtWidgets.QApplication([])
application = MainWin()
application.show()

sys.exit(app.exec())