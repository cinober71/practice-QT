from PyQt5 import QtCore, QtWidgets

import random as rnd
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import time

now = datetime.datetime.now()
s = now.strftime("%d-%m-%Y %H:%M")
s1 = now.strftime("%d-%m-%Y")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 451, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.dial_pre = QtWidgets.QDial(self.frame)
        self.dial_pre.setGeometry(QtCore.QRect(30, 40, 101, 91))
        self.dial_pre.setObjectName("dial_pre")
        self.dial_vol = QtWidgets.QDial(self.frame)
        self.dial_vol.setGeometry(QtCore.QRect(160, 40, 101, 91))
        self.dial_vol.setMouseTracking(False)
        self.dial_vol.setTabletTracking(False)
        self.dial_vol.setAutoFillBackground(False)
        self.dial_vol.setInvertedAppearance(False)
        self.dial_vol.setInvertedControls(False)
        self.dial_vol.setWrapping(False)
        self.dial_vol.setNotchesVisible(False)
        self.dial_vol.setObjectName("dial_vol")
        self.dial_tem = QtWidgets.QDial(self.frame)
        self.dial_tem.setGeometry(QtCore.QRect(290, 40, 121, 91))
        self.dial_tem.setObjectName("dial_tem")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 111, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(280, 20, 151, 18))
        self.label_3.setObjectName("label_3")
        self.lcd_tem = QtWidgets.QLCDNumber(self.frame)
        self.lcd_tem.setGeometry(QtCore.QRect(320, 140, 64, 23))
        self.lcd_tem.setObjectName("lcd_tem")
        self.lcd_tem.setStyleSheet('background: rgb(0, 0, 200);')
        self.lcd_vol = QtWidgets.QLCDNumber(self.frame)
        self.lcd_vol.setGeometry(QtCore.QRect(180, 140, 64, 23))
        self.lcd_vol.setObjectName("lcd_vol")
        self.lcd_vol.setStyleSheet('background: rgb(0, 0, 200);')
        self.lcd_pre = QtWidgets.QLCDNumber(self.frame)
        self.lcd_pre.setGeometry(QtCore.QRect(50, 140, 64, 23))
        self.lcd_pre.setObjectName("lcd_pre")
        self.lcd_pre.setStyleSheet('background: rgb(0, 0, 200);')
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(10, 180, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(140, 180, 151, 18))
        self.label_4.setObjectName("label_4")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(460, 0, 131, 61))
        self.start.setObjectName("start")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(460, 80, 131, 61))
        self.stop_btn.setObjectName("stop_btn")
        self.alarm_btn = QtWidgets.QPushButton(self.centralwidget)
        self.alarm_btn.setGeometry(QtCore.QRect(460, 160, 131, 51))
        self.alarm_btn.setText("")
        self.alarm_btn.setStyleSheet('background: rgb(200, 0, 0);')
        self.alarm_btn.setObjectName("alarm_btn")
        self.chek_btn = QtWidgets.QPushButton(self.centralwidget)
        self.chek_btn.setGeometry(QtCore.QRect(620, 10, 201, 31))
        self.chek_btn.setObjectName("chek_btn")
        self.fire_chek_btn = QtWidgets.QPushButton(self.centralwidget)
        self.fire_chek_btn.setGeometry(QtCore.QRect(620, 50, 201, 31))
        self.fire_chek_btn.setObjectName("fire_chek_btn")
        self.textIN = QtWidgets.QTextBrowser(self.centralwidget)
        self.textIN.setGeometry(QtCore.QRect(620, 90, 201, 121))
        self.textIN.setObjectName("textIN")
        self.vertical_pre = QtWidgets.QSlider(self.centralwidget)
        self.vertical_pre.setGeometry(QtCore.QRect(50, 230, 20, 131))
        self.vertical_pre.setOrientation(QtCore.Qt.Vertical)
        self.vertical_pre.setObjectName("vertical_pre")
        self.vertical_vol = QtWidgets.QSlider(self.centralwidget)
        self.vertical_vol.setGeometry(QtCore.QRect(190, 230, 20, 131))
        self.vertical_vol.setOrientation(QtCore.Qt.Vertical)
        self.vertical_vol.setObjectName("vertical_vol")
        self.vertical_tem = QtWidgets.QSlider(self.centralwidget)
        self.vertical_tem.setGeometry(QtCore.QRect(330, 230, 20, 131))
        self.vertical_tem.setOrientation(QtCore.Qt.Vertical)
        self.vertical_tem.setObjectName("vertical_tem")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(690, 270, 141, 34))
        self.exit_btn.setObjectName("exit_btn")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(690, 310, 141, 32))
        self.username.setObjectName("username")
        self.username.setText("User_Test")
        self.date = QtWidgets.QLineEdit(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(690, 340, 141, 32))
        self.date.setObjectName("date")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(410, 230, 251, 131))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textOut = QtWidgets.QTextBrowser(self.frame_2)
        self.textOut.setGeometry(QtCore.QRect(0, 0, 251, 131))
        self.textOut.setObjectName("textOut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.date.setText(str(s1))

        self.retranslateUi(MainWindow)
        self.dial_vol.valueChanged['int'].connect(self.dial_vol.setValue)
        self.dial_pre.valueChanged['int'].connect(self.lcd_pre.display)
        self.dial_tem.valueChanged['int'].connect(self.lcd_tem.display)
        self.dial_vol.valueChanged['int'].connect(self.lcd_vol.display)
        self.vertical_pre.valueChanged['int'].connect(self.dial_pre.setValue)
        self.vertical_vol.valueChanged['int'].connect(self.dial_vol.setValue)
        self.vertical_tem.valueChanged['int'].connect(self.dial_tem.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Тиск в системі"))
        self.label_2.setText(_translate("MainWindow", "Об\'єм видобутку"))
        self.label_3.setText(_translate("MainWindow", "Температура в системі"))
        self.label_4.setText(_translate("MainWindow", "Наватеження системи"))
        self.start.setText(_translate("MainWindow", "ПУСК"))
        self.stop_btn.setText(_translate("MainWindow", "СТОП"))
        self.chek_btn.setText(_translate("MainWindow", "Перевірка датчиків"))
        self.fire_chek_btn.setText(_translate("MainWindow", "Перевірка пож. системи"))
        self.exit_btn.setText(_translate("MainWindow", "Вихід із системи"))
        self.start.clicked.connect(lambda: self.make_start())
        self.start.clicked.connect(lambda: self.progres())
        self.chek_btn.clicked.connect(lambda: self.make_test())
        self.fire_chek_btn.clicked.connect(lambda: self.make_fire_test())
        self.exit_btn.clicked.connect(lambda: self.make_exit())
        self.alarm_btn.clicked.connect(lambda: self.make_alarm())

    def make_start(self):
        self.textOut.append("Розпочато сеанс роботи номер зміни відповідає даті")
        self.textOut.append(s)

    def progres(self):
        a = int(self.dial_vol.value())
        b = int(self.dial_pre.value())
        c = int(self.dial_tem.value())
        I = [a, b, c]
        s = int(np.mean(I))
        for i in range(s):
            time.sleep(0.05)
            self.progressBar.setValue(i)
        print(s)

    def make_test(self):
        self.textIN.append("Розпочтато тестування датчиків")
        t = now.strftime("%H:%M:%S")
        self.textIN.append(t)
        self.textIN.append("Список справних датчиків:")
        flag = [True for i in range(11)]
        for i in range(11):
            if flag[i]:
                self.textIN.append("LP" + str(i))
            else:
                self.textIN.append("Неспвність:" + str(i))

    def make_fire_test(self):
        self.textIN.append("Перевірка протипоженої системи...")
        flag = [True for i in range(8)]
        print(flag)
        for i in flag:
            if i:
                self.textIN.append("Перевірка... Вдало")
            else:
                self.textIN.append("Виявено поломку, передаэмо дані у командний центр")

    def make_exit(self):
        sys.exit(app.exec_())

    def make_alarm(self):
        self.dial_vol.setValue(0)
        self.dial_tem.setValue(0)
        self.dial_pre.setValue(0)
        self.progressBar.setValue(0)
        self.textIN.append("Екстрена зупинка")
        self.textOut.append("Екстрена зупинка")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
