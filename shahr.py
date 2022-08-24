from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_city(object):
    def setupUi(self, SubWindow):
        SubWindow.setObjectName("get city")
        SubWindow.resize(388, 206)
        self.centralwidget = QtWidgets.QWidget(SubWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 130, 261, 31))
        self.lineEdit.setToolTip("")
        self.lineEdit.setStatusTip("")
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setAccessibleName("")
        self.lineEdit.setAccessibleDescription("")
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, -10, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(16, 30, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(16, 60, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(16, 90, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        SubWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SubWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 388, 21))
        self.menubar.setObjectName("menubar")
        SubWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SubWindow)
        self.statusbar.setObjectName("statusbar")
        SubWindow.setStatusBar(self.statusbar)
        l1 = "ببین برای آب و هوا به اسم شهرت نیاز دارم"
        l2 = "فقط اسم استانت رو وارد کن که شناخته"
        l3 = " شده باشه و مرکز هواشناسی توش باشه"
        l4 = " فقط درست وارد کنی ها"
        self.retranslateUi(SubWindow, l1, l2, l3, l4)
        self.pushButton.clicked.connect(self.get_shahr)
        QtCore.QMetaObject.connectSlotsByName(SubWindow)

    def get_shahr(self):
        shahr = self.lineEdit.text()
        f = open("shahr.txt", "w", encoding="utf8")
        f.write(shahr)
        f.close()
        l1 = ''
        l2 = 'می تونی این پنجره رو ببندی'
        l3 = 'یه بار خود برنامه رو هم ببند'
        l4 = ''
        self.retranslateUi(QtWidgets.QMainWindow(), l1, l2, l3, l4)

        
    def retranslateUi(self, SubWindow, l1, l2, l3, l4):
        _translate = QtCore.QCoreApplication.translate
        SubWindow.setWindowTitle(_translate("get city", "get city"))
        self.pushButton.setText(_translate("get city", "تایید"))
        self.label.setText(_translate("get city", l1))
        self.label_2.setText(_translate("get city", l2))
        self.label_3.setText(_translate("get city", l3))
        self.label_4.setText(_translate("get city", l4))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SubWindow = QtWidgets.QMainWindow()
    ui = Ui_city()
    ui.setupUi(SubWindow)
    SubWindow.show()
    sys.exit(app.exec_())
