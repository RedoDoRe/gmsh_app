# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'option_theme.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 300)
        Dialog.setMinimumSize(QtCore.QSize(600, 300))
        Dialog.setMaximumSize(QtCore.QSize(600, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/gui/iconapp/gui/apple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_main = QtWidgets.QFrame(Dialog)
        self.frame_main.setStyleSheet("/*QFrame*/\n"
"QFrame#frame_main {\n"
"    background-color:rgb(50, 50, 50);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    }\n"
"    QFrame#frame_header{\n"
"    background-color:qlineargradient(spread:reflect, x1:0, y1:0.136, x2:0, y2:1, stop:0 rgba(50, 50, 50, 255), stop:0.774011 rgba(81, 81, 81, 255));\n"
"    border-bottom: 1px solid rgb(34,34,34);\n"
"    border-radius: 5px;\n"
"    border-bottom-right-radius: -5px;\n"
"    border-bottom-left-radius: -5px;\n"
"    }\n"
"/*QLabel*/\n"
"QLabel{\n"
"color: rgb(255,255,255);\n"
"}\n"
"QLabel#label_light{\n"
"    background-image: url(:/gui/iconapp/gui/light_theme.png);\n"
"    background-repeat:none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel#label_dark{\n"
"    background-image: url(:/gui/iconapp/gui/dark_theme.png);\n"
"    background-repeat: none;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"/* QRadioButton*/\n"
"QRadioButton{\n"
"        color:rgb(188, 192, 195);\n"
"\n"
"}\n"
"QRadioButton::indicator{\n"
"        color:rgb(188, 192, 195);\n"
"        border: 2px solid rgb(255,255,255);\n"
"        height: 20px;\n"
"        width:20px;\n"
"        border-radius:12px;\n"
"        background: rgb(44, 49, 60);\n"
"        \n"
"}\n"
"QRadioButton::indicator:hover{\n"
"         border-radius: 10px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"         background: 3px solid rgb(52, 59, 72);\n"
"        border: 2px solid rgb(138, 180, 248);  \n"
"        border-radius:12px;     \n"
"        background-image: url(:/resource/iconapp/24x24/cil-check-alt.png);\n"
"}\n"
"\n"
"/*QPushButton*/\n"
"\n"
"    /*QPushButton ok */\n"
"QPushButton#pushButton_ok {\n"
"        color: rgb(255, 255, 255);\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0.994, x2:0, y2:0.0569545, stop:0.0340909 rgba(0, 170, 255, 255), stop:1 rgba(170, 214, 255, 255));\n"
"        border: 1px solid rgb(76, 162, 249);\n"
"        border-radius: 5px;\n"
"           \n"
"}\n"
"QPushButton#pushButton_ok:hover { \n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 170, 255, 255), stop:0.755682 rgba(171, 224, 255, 255));\n"
"        border: 2px solid rgb(76, 162, 249);\n"
"       \n"
"    }\n"
"QPushButton#pushButton_ok:pressed {\n"
"           background-color: qlineargradient(spread:pad, x1:0, y1:0.994, x2:0, y2:0.0569545, stop:0.0340909 rgba(0, 170, 255, 255), stop:1 rgba(170, 214, 255, 255));\n"
" }\n"
"\n"
"\n"
"    /*QPushButton cancel*/\n"
"\n"
"QPushButton#pushButton_cancel {\n"
"        color: rgb(33, 33, 33);\n"
"        background-color: qlineargradient(spread:reflect, x1:0.0454545, y1:0, x2:0.006, y2:1, stop:0 rgba(235, 235, 235, 255), stop:0.801136 rgba(176, 176, 176, 255));\n"
"        border: 1px solid rgb(180, 180, 180);\n"
"        border-radius: 5px;\n"
"           \n"
"    }\n"
"QPushButton#pushButton_cancel:hover { \n"
"        background-color: qlineargradient(spread:reflect, x1:0.0454545, y1:0, x2:0.006, y2:1, stop:0 rgba(235, 235, 235, 255), stop:0.801136 rgba(210, 210, 210, 255));\n"
"        border: 2px solid rgb(76, 162, 249);\n"
"       \n"
"}\n"
"QPushButton#pushButton_cancel:pressed{\n"
"           background-color:  qlineargradient(spread:reflect, x1:0.0454545, y1:0, x2:0.006, y2:1, stop:0 rgba(235, 235, 235, 255), stop:0.801136 rgba(230, 230, 230, 255));\n"
" }\n"
"\n"
"QPushButton{\n"
"        background-color:rgb(75, 104, 133);\n"
"        color: rgba(255,255,255,210);\n"
"        border: None;\n"
"        border-radius: 10px;\n"
"        background-repeat: None;\n"
"        background-position:center;\n"
"\n"
"}\n"
"QPushButton:hover    {    \n"
"        background-color:rgb(65, 91, 116);\n"
"        border: 1px solid rgb(91, 152, 248);    \n"
"    }\n"
"QPushButton:pressed    {    \n"
"        background-color:  rgb(96, 134, 171);\n"
"}\n"
"")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_header = QtWidgets.QFrame(self.frame_main)
        self.frame_header.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_header.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.frame_header.setFont(font)
        self.frame_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header.setObjectName("frame_header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_logo = QtWidgets.QLabel(self.frame_header)
        self.label_logo.setMinimumSize(QtCore.QSize(20, 20))
        self.label_logo.setMaximumSize(QtCore.QSize(40, 20))
        self.label_logo.setStyleSheet("image: url(:/gui/iconapp/gui/apple.png);\n"
"width: 20px;\n"
"height:20px;")
        self.label_logo.setText("")
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout.addWidget(self.label_logo)
        self.label_title = QtWidgets.QLabel(self.frame_header)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        self.pushButton_close = QtWidgets.QPushButton(self.frame_header)
        self.pushButton_close.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButton_close.setMaximumSize(QtCore.QSize(40, 30))
        self.pushButton_close.setStyleSheet("QPushButton#pushButton_close\n"
"    {\n"
"        background: none;\n"
"        border: none;\n"
"        border-radius: -10px;\n"
"        background-repeat:none;\n"
"        background-position: center;\n"
"        background-image: url(:/bold/iconapp/bold.40x40/3.png);\n"
"    }\n"
"\n"
"    QPushButton#pushButton_close:hover\n"
"    {\n"
"        background-color: rgb(121, 121, 121);\n"
"        background-image: url(:/16x16/iconapp/16x16/cil-x.png);\n"
"        \n"
"    }\n"
"\n"
"    QPushButton#pushButton_close:pressed\n"
"    {\n"
"        background-color: rgb(252, 96, 66);\n"
"        \n"
"    }")
        self.pushButton_close.setText("")
        self.pushButton_close.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.verticalLayout.addWidget(self.frame_header)
        self.frame_img = QtWidgets.QFrame(self.frame_main)
        self.frame_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_img.setObjectName("frame_img")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_img)
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_light = QtWidgets.QRadioButton(self.frame_img)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.radioButton_light.setFont(font)
        self.radioButton_light.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_light.setStyleSheet("")
        self.radioButton_light.setCheckable(True)
        self.radioButton_light.setChecked(False)
        self.radioButton_light.setAutoRepeat(False)
        self.radioButton_light.setAutoExclusive(True)
        self.radioButton_light.setObjectName("radioButton_light")
        self.gridLayout.addWidget(self.radioButton_light, 3, 0, 1, 1)
        self.radioButton_dark = QtWidgets.QRadioButton(self.frame_img)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.radioButton_dark.setFont(font)
        self.radioButton_dark.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_dark.setStyleSheet("")
        self.radioButton_dark.setCheckable(True)
        self.radioButton_dark.setChecked(False)
        self.radioButton_dark.setAutoRepeat(False)
        self.radioButton_dark.setAutoExclusive(True)
        self.radioButton_dark.setObjectName("radioButton_dark")
        self.gridLayout.addWidget(self.radioButton_dark, 3, 1, 1, 1)
        self.pushButton_light = QtWidgets.QPushButton(self.frame_img)
        self.pushButton_light.setMinimumSize(QtCore.QSize(260, 140))
        self.pushButton_light.setMaximumSize(QtCore.QSize(260, 140))
        self.pushButton_light.setStyleSheet("background-image: url(:/gui/iconapp/gui/light_theme.png);")
        self.pushButton_light.setText("")
        self.pushButton_light.setObjectName("pushButton_light")
        self.gridLayout.addWidget(self.pushButton_light, 2, 0, 1, 1)
        self.pushButton_dark = QtWidgets.QPushButton(self.frame_img)
        self.pushButton_dark.setMinimumSize(QtCore.QSize(260, 140))
        self.pushButton_dark.setMaximumSize(QtCore.QSize(260, 140))
        self.pushButton_dark.setStyleSheet("background-image: url(:/gui/iconapp/gui/dark_theme.png);")
        self.pushButton_dark.setText("")
        self.pushButton_dark.setObjectName("pushButton_dark")
        self.gridLayout.addWidget(self.pushButton_dark, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.frame_img)
        self.frame_done = QtWidgets.QFrame(self.frame_main)
        self.frame_done.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_done.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_done.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_done.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_done.setObjectName("frame_done")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_done)
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 8)
        self.verticalLayout_4.setSpacing(17)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_done = QtWidgets.QHBoxLayout()
        self.horizontalLayout_done.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_done.setObjectName("horizontalLayout_done")
        self.pushButton_cancel = QtWidgets.QPushButton(self.frame_done)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cancel.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/16x16/iconapp/16x16/cil-account-logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cancel.setIcon(icon1)
        self.pushButton_cancel.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_cancel.setAutoDefault(False)
        self.pushButton_cancel.setDefault(False)
        self.pushButton_cancel.setFlat(False)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_done.addWidget(self.pushButton_cancel)
        self.label_done = QtWidgets.QLabel(self.frame_done)
        self.label_done.setText("")
        self.label_done.setObjectName("label_done")
        self.horizontalLayout_done.addWidget(self.label_done)
        self.pushButton_ok = QtWidgets.QPushButton(self.frame_done)
        self.pushButton_ok.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_ok.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_ok.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resource/resources/33.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ok.setIcon(icon2)
        self.pushButton_ok.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_ok.setAutoDefault(False)
        self.pushButton_ok.setDefault(False)
        self.pushButton_ok.setFlat(False)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_done.addWidget(self.pushButton_ok)
        self.verticalLayout_4.addLayout(self.horizontalLayout_done)
        self.verticalLayout.addWidget(self.frame_done)
        self.verticalLayout_3.addWidget(self.frame_main)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QC APP"))
        self.label_title.setText(_translate("Dialog", "QC - Ch???n giao di???n"))
        self.radioButton_light.setText(_translate("Dialog", "Giao di???n ban ng??y"))
        self.radioButton_dark.setText(_translate("Dialog", "Giao di???n ban ????m"))
        self.pushButton_light.setShortcut(_translate("Dialog", "1"))
        self.pushButton_dark.setShortcut(_translate("Dialog", "2"))
        self.pushButton_cancel.setText(_translate("Dialog", "THO??T"))
        self.pushButton_cancel.setShortcut(_translate("Dialog", "Esc"))
        self.pushButton_ok.setText(_translate("Dialog", "??I TI???P"))
        self.pushButton_ok.setShortcut(_translate("Dialog", "Return"))
import resource_rc
