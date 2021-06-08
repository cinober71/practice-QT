# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_in_face.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 519)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(230, 80, 321, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 30, 141, 18))
        self.label.setObjectName("label")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(120, 80, 161, 32))
        self.username.setObjectName("username")
        self.passwrd = QtWidgets.QLineEdit(self.frame)
        self.passwrd.setGeometry(QtCore.QRect(120, 130, 161, 32))
        self.passwrd.setObjectName("passwrd")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 87, 58, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 58, 18))
        self.label_3.setObjectName("label_3")
        self.enter_btn = QtWidgets.QPushButton(self.frame)
        self.enter_btn.setGeometry(QtCore.QRect(60, 180, 88, 34))
        self.enter_btn.setObjectName("enter_btn")
        self.exit_btn = QtWidgets.QPushButton(self.frame)
        self.exit_btn.setGeometry(QtCore.QRect(170, 180, 88, 34))
        self.exit_btn.setObjectName("exit_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Вхід до системи"))
        self.label_2.setText(_translate("MainWindow", "Логін"))
        self.label_3.setText(_translate("MainWindow", "Пароль"))
        self.enter_btn.setText(_translate("MainWindow", "Вхід"))
        self.exit_btn.setText(_translate("MainWindow", "Вихід"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
