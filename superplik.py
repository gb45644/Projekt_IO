import pandas as pd
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from pandas import DataFrame
import sys
import pymysql
import numpy as np

def loadcapcal():
    db = pymysql.connect('localhost', 'root', 'root', 'io')
    cursor = db.cursor()

    fetch_queries = 'Select calendar.id, calendar.Datagr From calendar ' \
 \
    # queries execution
    cursor.execute(fetch_queries)
    lines = cursor.fetchall()
    calendarcap = []
    for line in lines:
        calendarcap.append(line)
    calendarcap = pd.DataFrame(calendarcap)

    db.commit()
    db.close()
    return calendarcap


def loadWO():
    db = pymysql.connect('localhost', 'root', 'root', 'io')
    cursor = db.cursor()

    fetch_queries = 'Select wo.id, wo.quantity, wo.start_date, items.id, items.description, ' \
                    'std_op.line, std_op.speed From wo Join wo_item ON wo.id = ' \
                    'wo_fk Join items ON wo_item.item_fk = items.id Join item_std ON ' \
                    'items.id = item_std.item_fk Join std_op ON item_std.std_op_fk = std_op.id'

    # queries execution
    cursor.execute(fetch_queries)
    lines = cursor.fetchall()
    wolist = []
    for line in lines:
        wolist.append(line)
    wolist = pd.DataFrame(wolist)

    db.commit()
    db.close()
    return wolist


calendar = pd.DataFrame(loadcapcal())
wolist = pd.DataFrame(loadWO())

# calendar['1'].dt.week

calendar.columns = ['byle jak', 'Data']
# print(calendar.dtypes)
# calendar[['rok','miesiac','dzien']]=calendar.Data.str.split("-",expand=True)
# print(calendar)
# print(calendar.Data.apply(lambda x: pd.Series(str(x).split("-"))))
calendar['Data'] = pd.to_datetime(calendar['Data'])
wolist[2] = pd.to_datetime(wolist[2])
# calendar.dropna(inplace=True)
# cal = calendar["Data"].split("-", n=2, expand=True)
# calendar["Rok"]=cal[1]
# calendar["Miesiac"]=cal[2]
# calendar["Dzien"]=cal[3]
# calendar.drop(columns=["Data"],inplace=True)
# print(calendar)

calendar['Nr tygodnia'] = calendar['Data'].dt.week
wolist[7] = wolist[2].dt.week
header = calendar['Nr tygodnia']
header.columns = ['num tyg']

linesdrop = wolist.drop(columns=[0, 1, 2, 3, 4, 6, 7])
linesdrop = linesdrop.drop_duplicates(subset=[5])
wolist.columns = ['numer zlecenia', 'ilosc', 'data', 'indeks', 'opis', 'linia', 'predkosc', 'num tyg']
wolist['lin cap'] = wolist['predkosc'] * 24 * 5
data_single = pd.pivot_table(wolist, values=['ilosc', 'lin cap'], index=['num tyg'], columns=['linia'],
                    aggfunc={'ilosc': np.sum, 'lin cap': np.mean}).transpose()





from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


        self.pushButton.clicked.connect(self.btn_clk)

        MainWindow.show()

    def btn_clk(self):
        path = self.lineEdit.text()
        df = pd.read_csv(path)
        self.tableView.set(df)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())