from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
import sys
import random
import numpy as np
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os

Form, Window = uic.loadUiType("interface.ui")
app = QtWidgets.QApplication(sys.argv)
window = Window()
form = Form()
form.setupUi(window)
window.show()



def rand_num(Bit, Adt, Mult):
    i = 0
    zero = random.randint(0, 10)
    Rand = []
    while i < 1000:
        zero = (Adt + (Mult * zero)) % Bit
        Rand.append(zero / Bit)
        i += 1
    return Rand



def stochasticity(Rand, R, L):
    B = []
    t = 0
    for i in range(L):
        if Rand[i] < R:
            t += 1
        elif Rand[i] > R:
            B.append(t)
            t = 0
    k = 0
    r = 0
    for i in range(len(B)):
        if B[i] == 0:
            k += 1

    return B, k, len(B)



def get_intervals(N):
    Interval = []
    k = 1 / N
    for i in np.arange(0, 1 + k, k):
        Interval.append(round(i, 2))

    return Interval



def return_data():
    adt = form.adt_const.text()
    mult = form.mult_const.text()
    bit = form.bit_num.text()
    a = rand_num(int(bit), float(adt), float(mult))
    print(a)
    return a


def stochast():
    a = (return_data())
    b = float(form.interval_num.text())
    l = int(form.num_vib.text())
    print(stochasticity(a, b, l))
    return stochasticity(a, b, l)


def Pyplot():
    n = int(form.interval_num.text())
    num_list = return_data()
    form.textEdit.append(str(return_data()))
    interval = get_intervals(n)
    y = []
    z = []
    for i in range(n):
        t = 0
        for j in range(100):
            if interval[i] <= num_list[j] <= interval[i + 1]:
                t += 1
        i += 1
        y.append(t)
    for i in range(len(y)):
        x = y[i] / 100
        z.append(x)
    form.textEdit.append(str(interval))
    form.textEdit.append('Тетсуваня на рівномірність')
    form.textEdit.append(str(y))
    form.textEdit.append(str(z))
    form.graphic.plot(interval, z, clear=True, stepMode=True, fillLevel=0, brush=(127, 41, 0, 255), background ='white' )


def radio():
    if form.period_test.isChecked():
        form.label_8.setText("Довжина вибірки ")
        form.label_9.setText("R для перевірки ")
        form.textEdit.append(str(return_data()))

        form.textEdit.append("Тест на стохастичність:")
        form.textEdit.append(str(stochast()))

    if form.stoh_test.isChecked():
        form.textEdit.append(str(return_data()))
        form.textEdit.append("Тест на рівномірність")
        form.textEdit.append("Результат - таблиця")
        form.textEdit.append("Де елемени це серії")
        form.textEdit.append("_______________________________")
        Pyplot()
        form.textEdit.append("_______________________________")



def return_standart():
    form.label_8.setText("Обсяг вибірки")
    form.label_9.setText("Кількість інтервалів")
    form.adt_const.setText(str(11))
    form.mult_const.setText(str(25214903917))
    form.bit_num.setText(str(31))


form.pushButton.clicked.connect(return_standart)
form.make_test.clicked.connect(radio)
app.exec_()
