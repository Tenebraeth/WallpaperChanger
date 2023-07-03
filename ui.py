# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(408, 474)
        MainWindow.setFixedSize(408, 474)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:#293241\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 411, 191))
        self.frame.setStyleSheet("background-color: rgb(238, 108, 77);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, -10, 381, 91))
        font = QtGui.QFont()
        font.setFamily("Work Sans ExtraBold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(140, 70, 121, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pictures/label.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 230, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Work Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(39, 48, 62);\n"
"border: 3px solid rgb(238, 108, 77);\n"
"border-radius: 10;\n"
"color: rgb(255, 255, 255)")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 310, 61, 61))
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(41, 50, 65);\n"
"image: url(pictures/caret-right-fill.png);"                                      
"border: 4px solid rgb(167, 201, 87);\n"
"border-radius: 10;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 4px solid rgb(106, 177, 118);\n"
"image: url(pictures/caret-right-fill-hover.png)"                                      
"}")
        self.pushButton.setText("")
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 310, 61, 61))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"background-color: rgb(41, 50, 65);\n"
"image: url(pictures/stop-mini-fill.png);"                                        
"border: 4px solid rgb(188, 71, 73);\n"
"border-radius: 10;\n"
"}\n"
"QPushButton:hover{\n"
"border: 4px solid rgb(151, 84, 115);\n"
"image: url(pictures/stop-mini-fill-hover.png);"                                        
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setIconSize(QtCore.QSize(30, 50))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 380, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Work Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(218, 199, 198)")
        self.label_3.setObjectName("label_3")
        self.label_3.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WallpaperChanger"))
        self.label_3.setText(_translate("MainWindow", "Идет поиск изображений..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())