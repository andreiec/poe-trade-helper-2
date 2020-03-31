from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Ui_MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.name_list = QtWidgets.QListWidget(self)
        self.price_list = QtWidgets.QListWidget(self)
        self.money_list = QtWidgets.QListWidget(self)
        self.auto_msg = QtWidgets.QCheckBox(self)
        self.price_img = QtWidgets.QLabel(self)
        self.money_img = QtWidgets.QLabel(self)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.status = QtWidgets.QLabel(self)
        self.stop_button = QtWidgets.QPushButton(self)
        self.resume_button = QtWidgets.QPushButton(self)
        self.start_button = QtWidgets.QPushButton(self)

        # Global flag to check if window should be closed
        self.closeWindow = False

    # Setup the ui
    def setupUi(self):
        # Setup Window size
        self.setObjectName("MainWindow")
        self.resize(340, 400)
        self.setFixedSize(self.size())

        # Setup icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # Trade name list Widget
        self.name_list.setGeometry(QtCore.QRect(10, 220, 220, 175))
        self.name_list.setObjectName("name_list")
        self.name_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.name_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # Price list Widget
        self.price_list.setGeometry(QtCore.QRect(286, 220, 45, 175))
        self.price_list.setObjectName("price_list")
        self.price_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.price_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # Money list Widget
        self.money_list.setGeometry(QtCore.QRect(236, 220, 45, 175))
        self.money_list.setObjectName("money_list")
        self.money_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.money_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # Auto-Message checkbox Widget
        self.auto_msg.setGeometry(QtCore.QRect(13, 110, 291, 20))
        self.auto_msg.setChecked(False)
        self.auto_msg.setObjectName("auto_msg")

        # Price list icon
        self.price_img.setGeometry(QtCore.QRect(292, 185, 32, 32))
        self.price_img.setObjectName("price_img")
        # 20 -> 32
        # Money list icon
        self.money_img.setGeometry(QtCore.QRect(242, 185, 32, 32))
        self.money_img.setObjectName("money_img")
        self.resume_button.setHidden(True)
        # Grid (all of top-half) Widget
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 311, 101))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(2, 0, 6, 0)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.lineEdit_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())

        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setMaximumSize(QtCore.QSize(62, 16))
        self.lineEdit_1.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_1.setAcceptDrops(True)
        self.lineEdit_1.setAutoFillBackground(False)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout_2.addWidget(self.lineEdit_1, 0, 2, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())

        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())

        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())

        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(62, 16))
        self.lineEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_3.setAcceptDrops(True)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 2, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(80, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(80, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(80, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)

        self.lineEdit_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())

        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(62, 16))
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_2.setAcceptDrops(True)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 2, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())

        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())

        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(80, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 1, 1, 1)

        self.lineEdit_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())

        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(62, 16))
        self.lineEdit_4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_4.setAcceptDrops(True)
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 2, 1, 1)

        # Status Text
        self.status.setGeometry(QtCore.QRect(14, 200, 211, 16))
        self.status.setObjectName("status")

        # Start Button
        self.start_button.setGeometry(QtCore.QRect(10, 160, 75, 23))
        self.start_button.setObjectName("start_button")

        # Resume Button
        self.resume_button.setGeometry(QtCore.QRect(170, 160, 75, 23))
        self.resume_button.setObjectName("resume_button")

        # Stop Button
        self.stop_button.setGeometry(QtCore.QRect(90, 160, 75, 23))
        self.stop_button.setObjectName("stop_button")

        # Tab Order
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        self.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        self.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        self.setTabOrder(self.lineEdit_4, self.auto_msg)
        self.setTabOrder(self.auto_msg, self.start_button)
        self.setTabOrder(self.start_button, self.stop_button)
        self.setTabOrder(self.stop_button, self.resume_button)
        self.setTabOrder(self.resume_button, self.name_list)
        self.setTabOrder(self.name_list, self.price_list)
        self.setTabOrder(self.price_list, self.money_list)
        self.setTabOrder(self.money_list, self.price_img)
        self.setTabOrder(self.price_img, self.money_img)

    # Show text on ui
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Trade Helper 2.0"))
        self.auto_msg.setText(_translate("MainWindow", "Auto send Message when you find a new trade"))
        self.label.setText(_translate("MainWindow", "Trade Code:"))
        self.label_2.setText(_translate("MainWindow", "Minimum Price:"))
        self.label_4.setText(_translate("MainWindow", "Available Currency:"))
        self.label_3.setText(_translate("MainWindow", "Maximum Price:"))
        self.status.setText(_translate("MainWindow", "Status:"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.resume_button.setText(_translate("MainWindow", "Resume"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))

    def closeEvent(self, event):
        import time
        self.closeWindow = True
        time.sleep(0.75)
        event.accept()

    def gameOpenedPopUp(self):
        QtWidgets.QMessageBox.about(self, "Game Error", "No opened instance of 'Path of Exile' found.\nMaybe consider opening the game?")

    # Returns -1 if field is not completed and -2 if field is of invalid input
    def getTradeCode(self):
        if len(self.lineEdit_1.text()) > 0:
            return self.lineEdit_1.text().strip()
        return -1

    # Returns -1 if field is not completed and -2 if field is of invalid input
    def getMinimumPrice(self):
        number = self.lineEdit_2.text().strip()
        if len(number) > 0:
            if number.replace('.', '', 1).isdigit():
                if float(number) > 0:
                    return float(number)
            return -2
        return -1

    # Returns -1 if field is not completed and -2 if field is of invalid input
    def getMaximumPrice(self):
        number = self.lineEdit_3.text().strip()
        if len(number) > 0:
            if number.replace('.', '', 1).isdigit():
                if float(number) > 0:
                    return float(number)
            return -2
        return -1

    # Returns -1 if field is not completed and -2 if field is of invalid input
    def getAvailableCurrency(self):
        number = self.lineEdit_4.text().strip()
        if len(number) > 0:
            if number.replace('.', '', 1).isdigit():
                if float(number) > 0:
                    return float(number)
            return -2
        return -1

    def isAutoTextChecked(self):
        return self.auto_msg.isChecked()
