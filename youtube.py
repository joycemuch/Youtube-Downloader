# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YouTube.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 533)
        # self.setWindowTitle(QtGui.QIcon('TV.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 821, 541))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 130, 781, 71))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(570, 280, 81, 41))
        self.comboBox.setStyleSheet("background-color: rgb(78, 214, 192);\n"
"color: rgb(0, 0, 0);\n"
"font: 25 8pt \"Montserrat Light\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(4, "")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(150, 460, 521, 16))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    \n"
"   border-style:none;\n"
"  border-radius:8px;\n"
" text-align:center;\n"
"    background-color: rgb(202, 202, 202);\n"
"\n"
"}\n"
"QProgressBar::chunk{\n"
"   border-radius:8px;\n"
"  \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(24, 159, 148, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", 10)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(160, 280, 391, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255); font-size:15px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Enter the url")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Downloader"))
        MainWindow.setWindowIcon(QtGui.QIcon('TV.ico'))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#189f94;\">YouTube Downloader :)</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MP4 1080"))
        self.comboBox.setItemText(1, _translate("MainWindow", "MP4 720"))
        self.comboBox.setItemText(2, _translate("MainWindow", "MP4 360"))
        self.comboBox.setItemText(3, _translate("MainWindow", "WEBM"))
        self.comboBox.activated.connect(self.do_something)
        # self.comboBox.activated.connect(self.download )

    def do_something(self):
        try:
            yt = YouTube(self.lineEdit.text())
            if self.comboBox.currentText() == "MP4 1080":
                yt.streams.get_by_itag(137).download()
                self.comboBox.activated.connect(self.download)

            elif self.comboBox.currentText() == "MP4 720":
                yt.streams.get_by_itag(22).download()
            elif self.comboBox.currentText() == "MP4 360":  
                yt.streams.get_by_itag(18).download() 
            elif self.comboBox.currentText() == "WEBM": 
                yt.streams.get_by_itag(140).download()
            print(self.comboBox.currentText())
        except:
            pass


    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progressBar.setValue(self.completed)

  



         
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
