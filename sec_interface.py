# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sec_inteface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import numpy as np
import time
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.handdrive_btn = QtWidgets.QPushButton(self.centralwidget)
        self.handdrive_btn.setGeometry(QtCore.QRect(0, 30, 131, 61))
        self.handdrive_btn.setObjectName("handdrive_btn")
        self.takedata_btn = QtWidgets.QPushButton(self.centralwidget)
        self.takedata_btn.setGeometry(QtCore.QRect(630, 30, 131, 34))
        self.takedata_btn.setObjectName("takedata_btn")
        self.list_of_station = QtWidgets.QTextBrowser(self.centralwidget)
        self.list_of_station.setGeometry(QtCore.QRect(390, 30, 231, 192))
        self.list_of_station.setObjectName("list_of_station")
        self.error_in_work = QtWidgets.QTextBrowser(self.centralwidget)
        self.error_in_work.setGeometry(QtCore.QRect(140, 30, 231, 192))
        self.error_in_work.setObjectName("error_in_work")
        self.lcd_vol = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_vol.setGeometry(QtCore.QRect(140, 230, 64, 23))
        self.lcd_vol.setObjectName("lcd_vol")
        self.lcd_tem = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_tem.setGeometry(QtCore.QRect(220, 230, 64, 23))
        self.lcd_tem.setObjectName("lcd_tem")
        self.lcd_pre = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_pre.setGeometry(QtCore.QRect(300, 230, 64, 23))
        self.lcd_pre.setObjectName("lcd_pre")
        self.sendbrake_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sendbrake_btn.setGeometry(QtCore.QRect(0, 100, 131, 41))
        self.sendbrake_btn.setObjectName("sendbrake_btn")
        self.check_btn = QtWidgets.QPushButton(self.centralwidget)
        self.check_btn.setGeometry(QtCore.QRect(630, 70, 131, 31))
        self.check_btn.setObjectName("check_btn")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(390, 230, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 230, 101, 18))
        self.label.setObjectName("label")
        self.work_with_client = QtWidgets.QTextBrowser(self.centralwidget)
        self.work_with_client.setGeometry(QtCore.QRect(140, 281, 231, 181))
        self.work_with_client.setObjectName("work_with_client")
        self.strateg = QtWidgets.QTextBrowser(self.centralwidget)
        self.strateg.setGeometry(QtCore.QRect(390, 281, 231, 181))
        self.strateg.setObjectName("strateg")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(690, 420, 88, 34))
        self.exit_btn.setObjectName("exit_btn")
        self.chek_quality_btn = QtWidgets.QPushButton(self.centralwidget)
        self.chek_quality_btn.setGeometry(QtCore.QRect(630, 270, 131, 34))
        self.chek_quality_btn.setObjectName("chek_quality_btn")
        self.strateg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.strateg_btn.setGeometry(QtCore.QRect(630, 310, 131, 34))
        self.strateg_btn.setObjectName("strateg_btn")
        self.add_client_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_client_btn.setGeometry(QtCore.QRect(10, 270, 121, 34))
        self.add_client_btn.setObjectName("add_client_btn")
        self.sort_client_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sort_client_btn.setGeometry(QtCore.QRect(10, 310, 121, 34))
        self.sort_client_btn.setObjectName("sort_client_btn")
        self.delete_from_list_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_from_list_btn.setGeometry(QtCore.QRect(10, 350, 121, 34))
        self.delete_from_list_btn.setObjectName("delete_from_list_btn")
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(630, 350, 131, 34))
        self.delete_btn.setObjectName("delete_btn")
        self.sort_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sort_btn.setGeometry(QtCore.QRect(630, 110, 131, 34))
        self.sort_btn.setObjectName("sort_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 10, 191, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 10, 141, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 260, 141, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 260, 121, 18))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.handdrive_btn.setText(_translate("MainWindow", "?????????? ??????????????????"))
        self.takedata_btn.setText(_translate("MainWindow", "?????????? ??????????"))
        self.handdrive_btn.clicked.connect(lambda: self.progres())
        self.list_of_station.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. C????????????: ??????????????????????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. ??????????????: ??????????????????????????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. ??????????????: ??????????????????????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. ??????????????: ????????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5. ??????????????: ??????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6. ??????????????: ??????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7. ??????????????: ????????????????????</p></body></html>"))
        self.error_in_work.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">?????????????? ?? ???????????? ??????????</p></body></html>"))
        self.sendbrake_btn.setText(_translate("MainWindow", "??????????????. \n"
"?????? ?????????????? "))
        self.check_btn.setText(_translate("MainWindow", "??????????????????"))
        self.label.setText(_translate("MainWindow", "????????????????????????"))
        self.work_with_client.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. ?????? &quot;???????????????? ??????????????&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. ?????? &quot;???????????? ????????&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. ?????? ???? &quot;????????????&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. ?????? &quot;?????????????????? ??????&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5. ?????? &quot;??????????????&quot;</p></body></html>"))
        self.strateg.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. ?????? &quot;???????????????? ??????????????&quot; - 50. ??????.????????(??????????)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. ?????? &quot;???????????? ????????&quot; - 200 ??????. ??????.????????????(??????)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. ?????? ???? &quot;????????????&quot;- 100. ??????. ???????? (??????????)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. ?????? &quot;?????????????????? ??????&quot; - 1 ?????????? ??????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5. ?????? &quot;??????????????&quot; - 500 ??????. ??????.????????????(??????)</p></body></html>"))
        self.exit_btn.setText(_translate("MainWindow", "??????????"))
        self.chek_quality_btn.setText(_translate("MainWindow", "???????????? ???????????? "))
        self.strateg_btn.setText(_translate("MainWindow", "?????????????????? ??????????"))
        self.add_client_btn.setText(_translate("MainWindow", "???????????? ??????????????"))
        self.sort_client_btn.setText(_translate("MainWindow", "???????????????????????? "))
        self.delete_from_list_btn.setText(_translate("MainWindow", "??????????. ???? ????????????"))
        self.delete_btn.setText(_translate("MainWindow", "   ???????????????? ???? ????????????"))
        self.sort_btn.setText(_translate("MainWindow", "???????????????????????? "))
        self.label_2.setText(_translate("MainWindow", "???????????? ?????????????? ??????????????????"))
        self.label_3.setText(_translate("MainWindow", "?????????????? ?? ????????????"))
        self.label_4.setText(_translate("MainWindow", "???????????? ???? ??????????????????"))
        self.label_5.setText(_translate("MainWindow", "?????????????????? ??????????"))

        self.lcd_vol.display(54)
        self.lcd_tem.display(43)
        self.lcd_pre.display(67)
        self.lcd_pre.setStyleSheet('background: rgb(0, 0, 200);')
        self.lcd_tem.setStyleSheet('background: rgb(0, 0, 200);')
        self.lcd_vol.setStyleSheet('background: rgb(0, 0, 200);')

        self.handdrive_btn.clicked.connect(lambda: self.progres())

    def progres(self):
        a = 54
        b = 43
        c = 67
        I = [a, b, c]
        s = int(np.mean(I))
        for i in range(s):
            time.sleep(0.05)
            self.progressBar.setValue(i)
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

