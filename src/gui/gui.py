#pyside2-uic gui/fanucCNC.ui > gui/fanucCNCgui.py

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import sys
import time

from gui.fanucCNCgui import Ui_MainWindow
from influxDB import *
from fanucPy import *

class Player_thread(QThread):

    job_done = Signal(list)

    def __init__(self):
        QThread.__init__(self)
        self.delay_ms = 1000


    def setDelay(self, delay):
        self.delay_ms = delay

    def run(self):

        while(1):
            self.job_done.emit(None)
            self.msleep(self.delay_ms)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ip = '132.207.165.127'
        self.port = '8193'

        self.token = 'WuAkbaCMucy5L6IKaBroNpSd-XcJiEFRv-RhYrIO-vyK3nis0XP1YGpCRnMx24NxVIWjAkgT_crMw19UZHrVQA=='
        self.org = "remy.cretin@polymtl.ca"
        self.bucket = "fanucCNC"

        self.ui.lineEdit_ip.setText(self.ip)
        self.ui.lineEdit_port.setText(self.port)

        dataRateSelection = ['0.1', '0.2', '0.5', '1', '2', '5', '10']
        self.ui.comboBox_data_rate.addItems(dataRateSelection)

        self.ui.lineEdit_token.setText(self.token)
        self.ui.lineEdit_org.setText(self.org)
        self.ui.lineEdit_bucket.setText(self.bucket)

        self.PyFwlib_instance = PyFwlib()
        self.player_thread_instance = Player_thread()

        #Signal/Slot Connection
        self.ui.toolButton.clicked.connect(self.setPath)
        self.ui.pushButton_start.clicked.connect(self.start)
        self.ui.pushButton_stop.clicked.connect(self.stop)

        self.player_thread_instance.job_done.connect(self.job_done)
    
    def setPath(self):
        wPath, _ = QFileDialog.getSaveFileName(self)
        self.ui.lineEdit_csv_path.setText(wPath)

    def start(self):
        ip = str(self.ui.lineEdit_ip.text())
        port = int(self.ui.lineEdit_port.text())
        
        #connect to the CNC. to do : add verification 
        
        self.player_thread_instance.start()        

        if self.PyFwlib_instance.connect('132.207.165.127', 8193) != 0:
            return -1

        
    def job_done(self):
        delay = float(self.ui.comboBox_data_rate.currentText())
        delay = int(delay*1000)

        self.player_thread_instance.setDelay(delay)

        vitesse = self.PyFwlib_instance.rdSpeed()

        if self.ui.radioButton_csv.isChecked():
            print(str(vitesse), int(round(time.time() * 1000)))

        else:
            influxDB_send_data(vitesse)
        

    def stop(self):
        self.player_thread_instance.terminate()
        


            
