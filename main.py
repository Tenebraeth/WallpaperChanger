import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon, QMovie
from ui import Ui_MainWindow
from WallpaperChangerV2 import WallpaperChangee
from time import sleep

class WCThread(QThread):
    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow
    def run(self):
        input_theme = self.mainwindow.ui.lineEdit.text()
        WallpaperChangee(input_theme)

class WallpaperChanger(QtWidgets.QMainWindow):
    def __init__(self):
        super(WallpaperChanger, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    def  init_UI(self):
        self.setWindowTitle('WallpaperChanger')
        self.setWindowIcon(QIcon('pictures\label.png'))
        self.movie = QMovie("pictures\\bongo-cat-transparent.gif")
        self.ui.label_3.setMovie(self.movie)
        self.movie.start()
        self.movie.stop()


        self.ui.lineEdit.setPlaceholderText('Введите тему обоев:')

        self.ui.pushButton.clicked.connect(self.Launch_Changer)
        self.ui.pushButton_2.clicked.connect(self.Stop_Changer)

        self.WCThread_instance = WCThread(mainwindow=self)

    def Launch_Changer(self):
        self.movie.start()
        self.WCThread_instance.start()

    def Stop_Changer(self):
        self.movie.stop()
        self.WCThread_instance.terminate()



app = QtWidgets.QApplication([])
application = WallpaperChanger()
application.show()

sys.exit(app.exec())