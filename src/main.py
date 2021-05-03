from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import sys

from gui.fanucCNCgui import Ui_MainWindow

from fanucPy import *
from influxDB import *


PyFwlib_instance = PyFwlib()
PyFwlib_instance.connect('132.207.165.127', 8193)

a = list()

while(1):
    vitesse = PyFwlib_instance.rdSpeed()
    influxDB_send_data(vitesse)
    time.sleep(5)
