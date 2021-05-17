from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import sys

from gui.gui import MainWindow




#pip install influxdb-client
"""
PyFwlib_instance = PyFwlib()
PyFwlib_instance.connect('132.207.165.127', 8193)

a = list()

while(1):
    vitesse = PyFwlib_instance.rdSpeed()
    influxDB_send_data(vitesse)
    time.sleep(5)
"""

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())