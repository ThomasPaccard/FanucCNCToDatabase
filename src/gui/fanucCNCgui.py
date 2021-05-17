# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fanucCNC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(599, 640)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_ip = QLineEdit(self.groupBox_2)
        self.lineEdit_ip.setObjectName(u"lineEdit_ip")

        self.verticalLayout_2.addWidget(self.lineEdit_ip)

        self.lineEdit_port = QLineEdit(self.groupBox_2)
        self.lineEdit_port.setObjectName(u"lineEdit_port")

        self.verticalLayout_2.addWidget(self.lineEdit_port)

        self.comboBox_data_rate = QComboBox(self.groupBox_2)
        self.comboBox_data_rate.setObjectName(u"comboBox_data_rate")

        self.verticalLayout_2.addWidget(self.comboBox_data_rate)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.radioButton_csv = QRadioButton(self.groupBox_3)
        self.radioButton_csv.setObjectName(u"radioButton_csv")

        self.verticalLayout_6.addWidget(self.radioButton_csv)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEdit_csv_path = QLineEdit(self.groupBox_3)
        self.lineEdit_csv_path.setObjectName(u"lineEdit_csv_path")

        self.horizontalLayout_4.addWidget(self.lineEdit_csv_path)

        self.toolButton = QToolButton(self.groupBox_3)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_4.addWidget(self.toolButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.line = QFrame(self.groupBox_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.radioButton_server = QRadioButton(self.groupBox_3)
        self.radioButton_server.setObjectName(u"radioButton_server")

        self.verticalLayout_6.addWidget(self.radioButton_server)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_token = QLineEdit(self.groupBox_3)
        self.lineEdit_token.setObjectName(u"lineEdit_token")

        self.verticalLayout.addWidget(self.lineEdit_token)

        self.lineEdit_org = QLineEdit(self.groupBox_3)
        self.lineEdit_org.setObjectName(u"lineEdit_org")

        self.verticalLayout.addWidget(self.lineEdit_org)

        self.lineEdit_bucket = QLineEdit(self.groupBox_3)
        self.lineEdit_bucket.setObjectName(u"lineEdit_bucket")

        self.verticalLayout.addWidget(self.lineEdit_bucket)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.horizontalLayout_3.addWidget(self.pushButton_start)

        self.pushButton_stop = QPushButton(self.centralwidget)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.horizontalLayout_3.addWidget(self.pushButton_stop)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 599, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FanucToDatabase", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Communication configuration", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"IP :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Port :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"P\u00e9riode d'\u00e9chantillonage :", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.radioButton_csv.setText(QCoreApplication.translate("MainWindow", u"CSV", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u" Path :", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.radioButton_server.setText(QCoreApplication.translate("MainWindow", u"Influxdb server", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Token :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Org :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Bucket :", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

