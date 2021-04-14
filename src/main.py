from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import sys

from gui.fanucCNCgui import Ui_MainWindow

from fanuc_focas_connection.fanucTest import *

"""
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
"""
PyFwlib_instance = PyFwlib()
PyFwlib_instance.connect('192.168.0.12', 8193)
PyFwlib_instance.rdSpeed()