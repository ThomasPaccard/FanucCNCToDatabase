from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import sys

from gui.fanucCNCgui import Ui_MainWindow

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec_())

print(choucroute)
print(choux)