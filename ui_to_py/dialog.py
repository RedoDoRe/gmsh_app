from main import *
from ui_to_py.message_box import Ui_Dialog_MessageBox as MessageBox

	


class Dialog_MessageBox(QDialog,MessageBox):
	def __init__(self,style, icon = None,boldtext="", text="", ok=True, cancel = False, parent=None):
		super(Dialog_MessageBox,self).__init__(parent)
		# Setting Translucent and Frameless Window
		self.setupUi(self)
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		# Setting Custom Background, Window Border and Shadow
		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(15)
		self.shadow.setOffset(0, 0)
		self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
		self.frame_msg_main.setGraphicsEffect(self.shadow)

		# Icon-Information- Button
		self.iconType = icon
		self.label_boldtext.setText(boldtext)
		self.label_text.setText(text)
		self.setStyleSheet(style)
		self.checkIcon()

		
		
		self.horizontalLayout_pushButton= QHBoxLayout(self.frame_ok)
		self.horizontalLayout_pushButton.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_pushButton.setSpacing(10)
		self.horizontalLayout_pushButton.setObjectName("horizontalLayout_pushButton")
		self.horizontalLayout_pushButton.setAlignment(QtCore.Qt.AlignRight)


		if ok:
			self.pushButton_ok = QPushButton()
			self.pushButton_ok.setObjectName("pushButton_ok")	
			self.pushButton_ok.setText('Ok')
			self.pushButton_ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))		
			self.pushButton_ok.setMinimumSize(QtCore.QSize(100, 30))
			self.pushButton_ok.setMaximumSize(QtCore.QSize(100, 30))
			font = QtGui.QFont()
			font.setPointSize(10)
			font.setBold(False)
			font.setWeight(50)
			self.pushButton_ok.setFont(font)
			self.horizontalLayout_pushButton.addWidget(self.pushButton_ok)
			self.pushButton_ok.clicked.connect(self.okButton)

		if cancel:
			self.pushButton_cancel = QPushButton()
			self.pushButton_cancel.setObjectName("pushButton_cancel")	
			self.pushButton_cancel.setText('Cancel')	
			self.pushButton_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))	
			self.pushButton_cancel.setMinimumSize(QtCore.QSize(100, 30))
			self.pushButton_cancel.setMaximumSize(QtCore.QSize(100, 30))
			font = QtGui.QFont()
			font.setPointSize(10)
			font.setBold(False)
			font.setWeight(50)
			self.pushButton_cancel.setFont(font)					
			self.horizontalLayout_pushButton.addWidget(self.pushButton_cancel)	
			self.pushButton_cancel.clicked.connect(self.cancelButton)
		
	def checkIcon(self):
		if self.iconType == "warning":
			self.label_icon.setStyleSheet("image: url(:/gui/iconapp/gui/warning.png)\n")
		elif self.iconType =="information":
			self.label_icon.setStyleSheet("image: url(:/gui/iconapp/gui/information.png)\n")
		elif self.iconType =="question":
			self.label_icon.setStyleSheet("image: url(:/gui/iconapp/gui/question.png)\n")
		else:
			self.label_icon.setStyleSheet("")

	def okButton(self):
		return self.done(1)
		
	def cancelButton(self):
		return self.done(0)
