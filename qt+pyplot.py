# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QFileDialog
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import random
import sys
import math
import numpy as np
from PyQt5.QtGui import QIcon

num_of_test = 0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphic = PlotWidget(self.centralwidget)
        self.graphic.setGeometry(QtCore.QRect(340, 180, 301, 221))
        self.graphic.setToolTipDuration(5)
        self.graphic.setObjectName("graphic")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 321, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nameoffile_2 = QtWidgets.QPushButton(self.frame)
        self.nameoffile_2.setGeometry(QtCore.QRect(10, 30, 151, 21))
        self.nameoffile_2.setObjectName("nameoffile_2")
        self.nameoffile_2.setStyleSheet('background: rgb(116, 133, 161, 150);')
        self.filename_2 = QtWidgets.QLineEdit(self.frame)
        self.filename_2.setGeometry(QtCore.QRect(170, 30, 141, 20))
        self.filename_2.setObjectName("filename_2")
        self.pathoffile_2 = QtWidgets.QLineEdit(self.frame)
        self.pathoffile_2.setGeometry(QtCore.QRect(100, 60, 211, 20))
        self.pathoffile_2.setObjectName("pathoffile_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 81, 20))
        self.label_4.setObjectName("label_4")
        self.num_of_vib = QtWidgets.QLineEdit(self.frame)
        self.num_of_vib.setGeometry(QtCore.QRect(142, 90, 171, 20))
        self.num_of_vib.setObjectName("num_of_vib")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(110, 120, 111, 20))
        self.label_6.setObjectName("label_6")
        self.change_gen = QtWidgets.QPushButton(self.frame)
        self.change_gen.setGeometry(QtCore.QRect(10, 142, 41, 31))
        self.change_gen.setText("")
        self.change_gen.setObjectName("change_gen")
        self.change_gen.setStyleSheet('background: rgb(116, 133, 161, 150);')
        self.name_of_generator = QtWidgets.QLabel(self.frame)
        self.name_of_generator.setGeometry(QtCore.QRect(80, 150, 121, 16))
        self.name_of_generator.setObjectName("name_of_generator")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 180, 321, 221))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.OutText_2 = QtWidgets.QTextBrowser(self.frame_3)
        self.OutText_2.setGeometry(QtCore.QRect(10, 10, 301, 201))
        self.OutText_2.setObjectName("OutText_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(330, 0, 311, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.CreateFile_2 = QtWidgets.QPushButton(self.frame_2)
        self.CreateFile_2.setGeometry(QtCore.QRect(50, 10, 211, 23))
        self.CreateFile_2.setObjectName("CreateFile_2")
        self.CreateFile_2.setStyleSheet('background: rgb(116, 133, 161, 150);')
        self.SeeStart_2 = QtWidgets.QPushButton(self.frame_2)
        self.SeeStart_2.setGeometry(QtCore.QRect(50, 40, 211, 23))
        self.SeeStart_2.setStyleSheet('background: rgb(116, 133, 161, 150);')
        self.SeeStart_2.setObjectName("SeeStart_2")
        self.Parameters_2 = QtWidgets.QPushButton(self.frame_2)
        self.Parameters_2.setGeometry(QtCore.QRect(50, 70, 211, 23))
        self.Parameters_2.setObjectName("Parameters_2")
        self.Parameters_2.setStyleSheet('background: rgb(116, 133, 161, 150);')
        self.PirsonTest_2 = QtWidgets.QPushButton(self.frame_2)
        self.PirsonTest_2.setGeometry(QtCore.QRect(50, 100, 211, 23))
        self.PirsonTest_2.setObjectName("PirsonTest_2")
        self.PirsonTest_2.setStyleSheet('background: rgb(116, 133, 161, 150);')
        self.SmirnovTest_2 = QtWidgets.QPushButton(self.frame_2)
        self.SmirnovTest_2.setGeometry(QtCore.QRect(50, 130, 211, 23))
        self.SmirnovTest_2.setObjectName("SmirnovTest_2")
        self.SmirnovTest_2.setStyleSheet('background: rgb(116, 133, 161, 150);')
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ср№2 Філоненко Т.О."))
        self.nameoffile_2.setText(_translate("MainWindow", "Робота із файлом на ім\'я"))
        self.label_4.setText(_translate("MainWindow", "Шлях до файлу"))
        self.label_5.setText(_translate("MainWindow", "Обсяг вибірки"))
        self.label_6.setText(_translate("MainWindow", "Вид Генератора"))
        self.name_of_generator.setText(_translate("MainWindow", "Нормальний"))
        self.CreateFile_2.setText(_translate("MainWindow", "Створення файлу"))
        self.SeeStart_2.setText(_translate("MainWindow", "Перегляд початку файлу"))
        self.Parameters_2.setText(_translate("MainWindow", "Параметри файлу"))
        self.PirsonTest_2.setText(_translate("MainWindow", "Тест файлу за Пірсоном"))
        self.SmirnovTest_2.setText(_translate("MainWindow", "Тест по Колмогорову - Смирнову"))
        self.graphic.setBackground("w")
        self.num_of_vib.setText("1000")
        self.pathoffile_2.setText("C:/Users/adamy/PycharmProjects/Sr2_IM_filonenko/test.txt")
        self.nameoffile_2.clicked.connect(lambda: self.get_Path())
        self.change_gen.clicked.connect(lambda: self.make_gen())
        self.CreateFile_2.clicked.connect(lambda: self.make_file())
        self.SeeStart_2.clicked.connect(lambda: self.start_check())
        self.Parameters_2.clicked.connect(lambda: self.chek_all())
        self.PirsonTest_2.clicked.connect(lambda: self.pirson_test())
        self.SmirnovTest_2.clicked.connect(lambda: self.kolmogorov_test())

    def plot(self, x, y):
        self.graphic.plot(x, y, clear=True, stepMode=True, fillLevel=0, brush=(116, 133, 161, 150))

    def get_Path(self):
        filename = QFileDialog.getOpenFileName()
        self.pathoffile_2.setText(filename[0])
        self.filename_2.setText("test")
        print(filename[0])

    num_of_gen = 0

    def make_gen(self):
        self.num_of_gen += 1
        if self.num_of_gen > 6:
            self.num_of_gen = 1
        if self.num_of_gen == 1:
            self.name_of_generator.setText("Нормальний")
        if self.num_of_gen == 2:
            self.name_of_generator.setText("Дискретний")
        if self.num_of_gen == 3:
            self.name_of_generator.setText("Рівномірний")
        if self.num_of_gen == 4:
            self.name_of_generator.setText("Довільний")
        if self.num_of_gen == 5:
            self.name_of_generator.setText("Ерланга")
        if self.num_of_gen == 6:
            self.name_of_generator.setText("Експоненціальний")

    def make_file(self):
        mainlist = []
        k = 50
        first = 0
        path = self.pathoffile_2.text()
        try:
            num = int(self.num_of_vib.text())
        except:
            self.OutText_2.append("Стандартне значення вибірки: 1000")
            num = 1000
            self.num_of_vib.setText("1000")
            raise
        if self.num_of_gen == 1:
            self.OutText_2.clear()
            self.OutText_2.append("Нормальний закон розподілення")
            for i in range(num):
                first = 0
                for j in range(100):
                    first += random.random()
                mainlist.append(first - 41)
                print(first - 41)
        if self.num_of_gen == 2:
            self.OutText_2.clear()
            self.OutText_2.append("Дискретний закон розподілення")
            X = [11, 22, 33, 44, 55]
            P = [0.01, 0.5, 0.39, 0.05, 0.05]
            o = 0.0
            while len(mainlist) < num:
                for j in range(len(P)):
                    if o < random.random() <= (o + P[j]):
                        mainlist.append(X[j])
                    o += P[j]
                o = 0
        if self.num_of_gen == 3:
            self.OutText_2.clear()
            self.OutText_2.append("Рівномірний закон розподілення")
            for i in range(num):
                first = random.random()
                mainlist.append(first)
        if self.num_of_gen == 4:
            self.OutText_2.clear()
            self.OutText_2.append("Довільний закон розподілення")
            for i in range(num):
                first = random.randint(0, 100)
                mainlist.append(first)
        if self.num_of_gen == 5:
            self.OutText_2.clear()
            self.OutText_2.append(" Закон розподілення Ерланга ")
            for i in range(num):
                first = -(1 / (k * 2)) * math.log(random.random() * random.random())
                mainlist.append(first)
        if self.num_of_gen == 6:
            self.OutText_2.clear()
            self.OutText_2.append("Експоненціальний закон розподілення")
            for i in range(num):
                first = -(1 / k) * math.log(random.random())
                mainlist.append(first)

        with open(path, "w") as f:
            for i in range(num):
                f.write(str(mainlist[i]) + "\n")

    def start_check(self):
        path = self.pathoffile_2.text()
        with open(path, "r") as f:
            Line = f.readlines()
            Line = [line.rstrip() for line in Line]
        self.OutText_2.append("Перевірка почтаку файлу:")
        if float(Line[0] )>1:
            self.OutText_2.append("Дискретна величина")
        else:
            self.OutText_2.append("Неперервна величина")
        self.OutText_2.append("++++++++++++++++++++++")

    def chek_all(self):
        path = self.pathoffile_2.text()
        mainlist = []
        try:
            with open(path,"r") as f:
               Line = f.readlines()
               Line = [line.rstrip() for line in Line]
        except:
            self.textBrowser.append("Error")
            raise

        for i in Line:
            mainlist.append(float(i))

        m = max(mainlist)
        Inter = []
        Freq = []
        Inter.append(0)
        s = m/20
        k = s

        for i in range(20):
            Inter.append(k)
            k+=s
        for i in range(20):
            k = 0
            for j in mainlist:
                if Inter[i] < j < Inter[i + 1]:
                    k += 1
            Freq.append(k/len(mainlist))
        self.plot(Inter, Freq)

        dispersion = np.var(mainlist)
        math_may = np.mean(mainlist)
        print(dispersion, math_may)
        self.OutText_2.append("Дисперсія для отрманої величини:")
        self.OutText_2.append(str(dispersion))
        self.OutText_2.append("Математичне сподівання:")
        self.OutText_2.append(str(math_may))

    def pirson_test(self):
        self.OutText_2.clear()
        path = self.pathoffile_2.text()
        mainlist = []
        try:
            with open(path, "r") as f:
                Line = f.readlines()
                Line = [line.rstrip() for line in Line]
        except:
            self.textBrowser.append("Error")
            raise
        for i in Line:
            mainlist.append(float(i))

        m = max(mainlist)
        Inter = []
        Freq = []
        Inter.append(0)
        s = m / 20
        k = s

        for i in range(20):
            Inter.append(k)
            k += s
        for i in range(20):
            k = 0
            for j in mainlist:
                if Inter[i] < j < Inter[i + 1]:
                    k += 1
            Freq.append(k / len(mainlist))

        pirson = 0
        for i in range(20):
            pirson += ((Freq[i] - 0.05)**2)/0.05
        print(pirson)
        self.OutText_2.append("Тест Пірсона:")
        self.OutText_2.append("Критичне значення:")
        self.OutText_2.append(str(pirson))


    def kolmogorov_test(self):
        self.OutText_2.clear()
        path = self.pathoffile_2.text()
        mainlist = []
        try:
            with open(path, "r") as f:
                Line = f.readlines()
                Line = [line.rstrip() for line in Line]
        except:
            self.textBrowser.append("Error")
            raise
        for i in Line:
            mainlist.append(float(i))

        m = max(mainlist)
        Inter = []
        Freq = []
        Inter.append(0)
        s = m / 20
        k = s

        for i in range(20):
            Inter.append(k)
            k += s
        for i in range(20):
            k = 0
            for j in mainlist:
                if Inter[i] < j < Inter[i + 1]:
                    k += 1
            Freq.append(k / len(mainlist))
        kolmogorov = 0
        for i in Freq:
            if abs(i - 0.05)> kolmogorov:
                kolmogorov = abs(i - 0.05)
        self.OutText_2.append("Тест Колмогорова-Смирнова:")
        self.OutText_2.append("Критичне значення:")
        self.OutText_2.append(str(kolmogorov))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
