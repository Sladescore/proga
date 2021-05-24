from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(482, 380)
        MainWindow.setMinimumSize(QtCore.QSize(482, 380))
        MainWindow.setMaximumSize(QtCore.QSize(482, 380))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.trackList = QtWidgets.QListWidget(self.centralwidget)
        self.trackList.setGeometry(QtCore.QRect(10, 10, 311, 281))
        self.trackList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.trackList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.trackList.setSelectionRectVisible(True)
        self.trackList.setObjectName("trackList")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(330, 10, 141, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.folderBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folderBtn.sizePolicy().hasHeightForWidth())
        self.folderBtn.setSizePolicy(sizePolicy)
        self.folderBtn.setObjectName("folderBtn")
        self.verticalLayout.addWidget(self.folderBtn)
        self.playBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playBtn.sizePolicy().hasHeightForWidth())
        self.playBtn.setSizePolicy(sizePolicy)
        self.playBtn.setObjectName("playBtn")
        self.verticalLayout.addWidget(self.playBtn)
        self.pauseBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pauseBtn.sizePolicy().hasHeightForWidth())
        self.pauseBtn.setSizePolicy(sizePolicy)
        self.pauseBtn.setObjectName("pauseBtn")
        self.verticalLayout.addWidget(self.pauseBtn)
        self.stopBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopBtn.sizePolicy().hasHeightForWidth())
        self.stopBtn.setSizePolicy(sizePolicy)
        self.stopBtn.setObjectName("stopBtn")
        self.verticalLayout.addWidget(self.stopBtn)
        self.nextBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextBtn.sizePolicy().hasHeightForWidth())
        self.nextBtn.setSizePolicy(sizePolicy)
        self.nextBtn.setObjectName("nextBtn")
        self.verticalLayout.addWidget(self.nextBtn)
        self.prevBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevBtn.sizePolicy().hasHeightForWidth())
        self.prevBtn.setSizePolicy(sizePolicy)
        self.prevBtn.setObjectName("prevBtn")
        self.verticalLayout.addWidget(self.prevBtn)
        self.shuffleBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shuffleBtn.sizePolicy().hasHeightForWidth())
        self.shuffleBtn.setSizePolicy(sizePolicy)
        self.shuffleBtn.setObjectName("shuffleBtn")
        self.verticalLayout.addWidget(self.shuffleBtn)
        self.progressSlider = QtWidgets.QSlider(self.centralwidget)
        self.progressSlider.setGeometry(QtCore.QRect(10, 330, 311, 22))
        self.progressSlider.setMinimum(1)
        self.progressSlider.setMaximum(100)
        self.progressSlider.setProperty("value", 1)
        self.progressSlider.setSliderPosition(1)
        self.progressSlider.setTracking(True)
        self.progressSlider.setOrientation(QtCore.Qt.Horizontal)
        self.progressSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.progressSlider.setObjectName("progressSlider")
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel.setGeometry(QtCore.QRect(10, 300, 311, 31))
        self.progressLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.progressLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.progressLabel.setObjectName("progressLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.folderBtn.setText(_translate("MainWindow", "Open folder"))
        self.playBtn.setText(_translate("MainWindow", "Play"))
        self.pauseBtn.setText(_translate("MainWindow", "Pause"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.nextBtn.setText(_translate("MainWindow", "Next track"))
        self.prevBtn.setText(_translate("MainWindow", "Previous track"))
        self.shuffleBtn.setText(_translate("MainWindow", "Shuffle"))
        self.progressLabel.setText(_translate("MainWindow", "0:00 / 0:00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
