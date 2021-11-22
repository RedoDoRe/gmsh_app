
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui,QtCore


import qss as style
import json, os
import random


from concurrent.futures import ThreadPoolExecutor

from ui_to_py.gmsh import Ui_MainWindow
from ui_to_py.create_file import Ui_Dialog_CreateFile as Form_File
from ui_to_py.import_data import Ui_Dialog_ImportNick as Form_Nick
from ui_to_py.sticker import Ui_MainWindow as Sticker

from func.sticker_btn import *
from func.table_func import *
from func.get_page_setting import *
from func.reaction import*
from func.comment import*
from func.login import *
from func.emoji import *

import threading, time


#Set state_stop
state_stop = False

class MainSticker(QMainWindow,Sticker):
	def __init__(self, parent = None):
		super(MainSticker,self).__init__(parent)
		self.setupUi(self)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.pushButton_close_sticker.clicked.connect(self.close) 

		self.mouseMoveEvent = self.moveWindow	

		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(15)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QtGui.QColor(89, 145, 255))
		self.widget.setGraphicsEffect(self.shadow)

	def moveWindow(self,event):
		# MOVE WINDOW 
		
		if event.buttons() == QtCore.Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()			
			event.accept()

	def mousePressEvent(self,event):
		self.dragPos = event.globalPos()

class MainWindow(QMainWindow,Ui_MainWindow,Table,PageSetting,Button):
	def __init__(self, parent = None):
		super(MainWindow,self).__init__(parent)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.setupUi(self)	
		self.setUpButton()		
		self.setUpMain()
		self.setUpTheme()
		self.setNickOnTable()
		self.define_shortcuts()
		


		#Set sicker
		self.sticker = MainSticker()
		self.sticker_command()

		#Set comboxBox
		self.comboBox.currentTextChanged.connect(self.setNickOnTable)

		#Set display page		
		self.state_page = True

		#Set checkbox All
		self.checkBox_num = QtWidgets.QCheckBox(self.tableWidget)
		self.checkBox_num.setObjectName("checkBox_num")	
		self.checkBox_num.setFixedSize(40,25)	
		self.checkBox_num.setCheckState(QtCore.Qt.Unchecked)
		self.checkBox_num.toggled.connect(self.setCheckAll)


		#Set zoom goc cuoi 
		self.sizegrip = QSizeGrip(self.frame_grip)
		self.sizegrip.setStyleSheet(r"QSizeGrip {width:10px;height:10px;margin:7px} ")
		self.state_setMaximum = False
		

		# Set display QLineEdit
		self.delay_from.setValidator(QtGui.QIntValidator())
		self.delay_to.setValidator(QtGui.QIntValidator())
		self.set_start_gio.setValidator(QtGui.QIntValidator())
		self.set_start_phut.setValidator(QtGui.QIntValidator())

		self.set_start_gio.textChanged.connect(self.condition_time)
		self.set_start_phut.textChanged.connect(self.condition_time)

		self.set_start_gio.setEnabled(False)
		self.set_start_phut.setEnabled(False)
		self.delay_from.setEnabled(True)
		self.delay_to.setEnabled(True)
		self.checkBox_timer.toggled.connect(self.enable_hour)
		self.checkBox_delay.toggled.connect(self.enable_minutes)

		self.checkBox_delay.setChecked(True)

		# Set radiobutton		
		self.radioButton_bv.setChecked(True)
		self.list_options = [self.radioButton_bv,\
							self.radioButton_profile,\
							self.radioButton_topic,\
							self.radioButton_rep,\
							self.radioButton_post,\
							self.radioButton_cmt_wall]

		

		#Đường dẫn ảnh máy tính:
		self.tableWidget.doubleClicked.connect(self.clickUploadImage)

		#Search taikhoan:
		self.lineEdit_search.textChanged.connect(self.findNickOnTable)		


		#Context Menu :

		self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.tableWidget.customContextMenuRequested.connect(lambda point:self.context_menu_table(point))


				


	def setUpMain(self):
		self.stackedWidget.setCurrentWidget(self.page_setting)		
		self.shadow =QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(10)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QtGui.QColor(89, 145, 255))
		self.label_title.mouseMoveEvent = self.moveWindow 
		self.frame_main.setGraphicsEffect(self.shadow)

		self.comboBox.addItems(file.replace('.txt','') for file in os.listdir('data'))


	def define_shortcuts(self):
		QShortcut(QtGui.QKeySequence("Space"),self.tableWidget).activated.connect(self.setStateNick)
		QShortcut(QtGui.QKeySequence("Esc"),self.tableWidget).activated.connect(self.uncheckNick)
		QShortcut(QtGui.QKeySequence("Ctrl+c"),self).activated.connect(self.copyTable)
		QShortcut(QtGui.QKeySequence("Ctrl+v"),self).activated.connect(self.pasteTable)
		QShortcut(QtGui.QKeySequence("Ctrl+b"),self).activated.connect(self.changePage)
		QShortcut(QtGui.QKeySequence("Delete"), self.tableWidget).activated.connect(self.deleteTable)
		QShortcut(QtGui.QKeySequence("F5"), self.tableWidget).activated.connect(self.setNickOnTable)

		QShortcut(QtGui.QKeySequence("F3"), self).activated.connect(self.showSticker)

		


	def setUpTheme(self):
		with open('settings/setting.json','r') as f:
			theme = json.load(f)
		self.state_theme = theme['state']
		self.changeTheme()

	def changeTheme(self):
		if self.state_theme:
			self.setStyleSheet(style.dark_theme)			
			self.state_theme = False
			current_theme = {
								"theme": "dark",
								"state": True,
							}
		else:
			self.setStyleSheet(style.light_theme)
			
			self.state_theme = True
			current_theme = {
								"theme": "light",
								"state": False,
							}
		
		with open('settings/setting.json','w') as file:
			file.write(json.dumps(current_theme,indent=4))

	def setMaximum(self):
		if self.state_setMaximum:
			self.showNormal()
			self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
			self.state_setMaximum = False
		else:
			self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
			self.state_setMaximum = True
			self.showMaximized()

	def setUpButton(self):
		self.pushButton_setting.clicked.connect(self.showPageSetting)
		self.pushButton_get_cmt.clicked.connect(self.showPageImportCmt)
		self.pushButton_export_cmt.clicked.connect(self.setCmtOnTable)
		self.pushButton_import_cmt.clicked.connect(self.showPageImportCmt)
		self.pushButton_home.clicked.connect(self.changeTheme)
		self.pushButton_close.clicked.connect(self.close)
		self.pushButton_zoom_in.clicked.connect(self.showMinimized)
		self.pushButton_zoom_out.clicked.connect(self.setMaximum)

		self.pushButton_import_file.clicked.connect(self.showFormFile)
		self.pushButton_import_nick.clicked.connect(self.showImportNick)

		

		# Đang test chương trình
		
		self.pushButton_stop.clicked.connect(self.setNickOnTable)
		

		self.pushButton_delete_file.clicked.connect(self.deleteFile)

		self.pushButton_start_like.clicked.connect(self.auto_like)
		self.pushButton_start_cmt.clicked.connect(self.auto_cmt)
		self.pushButton_login.clicked.connect(self.auto_login)
		self.pushButton_stop.clicked.connect(self.stopThreading)



	def moveWindow(self,event):
		# MOVE WINDOW 
		if event.buttons() == QtCore.Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()

	def mousePressEvent(self,event):
		self.dragPos = event.globalPos()

	def changePage(self):
		if self.state_page:
			self.showPageImportCmt()
			self.state_page = False 
		else:
			self.showPageSetting()
			self.state_page = True 

	def showPageSetting(self):
		self.stackedWidget.setCurrentWidget(self.page_setting)	

	def showPageImportCmt(self):
		self.stackedWidget.setCurrentWidget(self.page_import_cmt)
		

	
	def showFormFile(self):
		self.form_file = Dialog_CreateFile(self.styleSheet())


		self.form_file.pushButton_create_file.clicked.connect(self.createFile)		
		self.form_file.pushButton_import_data.clicked.connect(self.showImportNick)	

		self.form_file.exec_() # K tương tác được gui nữa - MAIN bị khóa


	def showImportNick(self):		
		self.import_nick = Dialog_ImportNick(self.styleSheet())

		self.setItemImportNick()

		self.import_nick.pushButton_create_file.clicked.connect(self.showFormFile)
		self.import_nick.pushButton_close_file.clicked.connect(self.import_nick.close)
		self.import_nick.pushButton__save_file.clicked.connect(self.saveFileNick)

		self.import_nick.exec_()


	def showSticker(self):
		self.sticker.show()

	def stopThreading(self):
		global state_stop
		state_stop = True


	def auto_like(self,state_time): # Kết nối hàm trong main và class khác
		list_account = self.getData() # Hàm trong main
		setting = self.settings()
		state_time = self.checkBox_timer.isChecked()


		if len(setting['list_link']) <=0:
			msg = Dialog_MessageBox(
				self.styleSheet(),
				icon='warning',
				boldtext='Cảnh báo',
				text ='Không thể để trống đường link',
				ok =True,
				cancel = False)
			msg.exec_()
			return
		elif setting['options'] not in [0,1,2]:
			msg = Dialog_MessageBox(
				self.styleSheet(),
				icon='warning',
				boldtext='Cảnh báo',
				text ='Vui lòng chọn chế độ like',
				ok =True,
				cancel = False)
			msg.exec_()
			return

		self.reaction_like  = ThreadReaction(list_account,setting,state_time) # Class khác nhưng truyền dữ liệu main
		
		self.reaction_like.new_signal.connect(self.status_set)


		self.reaction_like.start()


	def auto_cmt(self): # Kết nối hàm trong main và class khác
		list_account = self.getData() # Hàm trong main
		setting = self.settings()
		state_time = self.checkBox_timer.isChecked()

		if len(setting['list_link']) <=0:
			msg = Dialog_MessageBox(
				self.styleSheet(),
				icon='warning',
				boldtext='Cảnh báo',
				text ='Không thể để trống đường link',
				ok =True,
				cancel = False)
			msg.exec_()
			return
		elif setting['options'] not in [3,4,5]:
			msg = Dialog_MessageBox(
				self.styleSheet(),
				icon='warning',
				boldtext='Cảnh báo',
				text ='Vui lòng chọn chế độ comment',
				ok =True,
				cancel = False)
			msg.exec_()
			return

		self.comment  = ThreadComment(list_account,setting,state_time) # Class khác nhưng truyền dữ liệu main		
		self.comment.new_signal.connect(self.status_set)
		self.comment.start()

	def auto_login(self):
		list_account = self.getData() # Hàm trong main
		setting = self.settings()
		if len(setting['list_link']) <=0:
			msg = Dialog_MessageBox(
				self.styleSheet(),
				icon='warning',
				boldtext='Cảnh báo',
				text ='Không thể để trống đường link',
				ok =True,
				cancel = False)
			msg.exec_()
			return
		if list_account ==[]:
			msg = Dialog_MessageBox(
				self.styleSheet(),
				icon='warning',
				boldtext='Cảnh báo',
				text ='Chọn nick để đăng nhập!',
				ok =True,
				cancel = False)
			msg.exec_()
			return
		self.login = ThreadLogin(list_account,setting)
		self.login.new_signal.connect(self.status_set)
		self.login.start()


	


	@QtCore.pyqtSlot(int,str,str,bool)	
	def status_set(self,row,text,color,boolean):
		if not self.state_theme:
			color_dict = {'blue':(102, 153, 204),
						  'red' : (255, 94, 94),
						 'normal': (248,248,248)
						
			}
		else:
			color_dict = {'blue':(0, 0, 255),
						  'red' : (255, 0, 0),
						 'normal': (33,33,33)
						
			}
		r,g,b = color_dict[color]
		item =  QtWidgets.QTableWidgetItem(text)
		item.setForeground(QtGui.QColor(r,g,b))
		self.tableWidget.setItem(row,6,item)
		if boolean:			
			self.checkbox_list[row].setCheckState(QtCore.Qt.Unchecked)

					



class Dialog_CreateFile(QDialog,Form_File):
	def __init__(self,style,parent =None):
		super(Dialog_CreateFile,self).__init__(parent)
		self.setupUi(self)
		self.setStyleSheet(style)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.pushButton_close.clicked.connect(self.close)

		self.shadow =QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(15)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QtGui.QColor(89, 145, 255))

		self.frame_body.setGraphicsEffect(self.shadow)
		self.label.mouseMoveEvent = self.moveWindow 


	def moveWindow(self,event):
		# MOVE WINDOW 
		if event.buttons() == QtCore.Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()

	def mousePressEvent(self,event):
		self.dragPos = event.globalPos()

class Dialog_ImportNick(QDialog,Form_Nick):
	def __init__(self,style,parent =None):
		super(Dialog_ImportNick,self).__init__(parent)
		self.setupUi(self)
		self.setStyleSheet(style)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.pushButton_close.clicked.connect(self.close)

		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(15)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QtGui.QColor(89, 145, 255))


		self.frame_body.setGraphicsEffect(self.shadow)
		self.label.mouseMoveEvent = self.moveWindow 




	def moveWindow(self,event):
		# MOVE WINDOW 
		if event.buttons() == QtCore.Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()

	def mousePressEvent(self,event):
		self.dragPos = event.globalPos()







class ThreadReaction(QtCore.QThread,Reaction,GetId):
	new_signal = QtCore.pyqtSignal(int, str, str,bool) 
	def __init__(self,list_account,settings,state_time):
		super(ThreadReaction,self).__init__()
		self.list_account = list_account 
		self.settings = settings
		self.state_time = state_time		
		self.list_link_topic = []
		if 	self.settings['options'] ==2:
			self.list_link_topic= self.reaction_topic()	

	#Threading với nhiều tài khoản
	def run(self): 
		global state_stop



		if self.state_time:
			for data in self.list_account:
				self.new_signal.emit(int(data.split('|')[0]),f'Hẹn giờ chạy sau: {self.settings["timer"]} giây...','normal',False)
			time.sleep(self.settings["timer"])		

		with ThreadPoolExecutor(max_workers =self.settings["counter_thread"]) as executor:
			for data in self.list_account:
				if state_stop:
					state_stop = False 
					break
				executor.submit(self.reaction_threading,data)
				QtCore.QThread.sleep(self.settings["delay"])					

class ThreadComment(QtCore.QThread,Comment):
	new_signal = QtCore.pyqtSignal(int, str, str,bool) 
	def __init__(self,list_account,settings, state_time):
		super(ThreadComment,self).__init__()
		self.list_account = list_account	  
		self.settings = settings
		self.state_time = state_time
		self.link_cmt = self.settings['list_link'][0]
			
	#Threading với nhiều tài khoản
	def run(self):			
		global state_stop	 
		if self.state_time:
			for data in self.list_account:
				self.new_signal.emit(int(data.split('|')[0]),f'Hẹn giờ chạy sau: {self.settings["timer"]} giây...','normal',False)
			time.sleep(self.settings["timer"])		

		with ThreadPoolExecutor(max_workers =self.settings["counter_thread"]) as executor:
			for data in self.list_account:
				if state_stop:
					state_stop = False 
					break
				executor.submit(self.comment_threading,data)
				QtCore.QThread.sleep(self.settings["delay"])	
			

class ThreadLogin(QtCore.QThread,Login):
	new_signal = QtCore.pyqtSignal(int, str, str,bool) 
	def __init__(self,list_account,settings):
		super(ThreadLogin,self).__init__()
		self.list_account = list_account
		self.settings = settings
		

	def run(self):
		global state_stop
		position_x = 0
		position_y = 0
		count = 0

		with ThreadPoolExecutor(max_workers= self.settings["counter_thread"]) as executor:
			for data in self.list_account:
				if state_stop:
					state_stop = False 
					break		
				executor.submit(self.login_driver,data,position_x,position_y) 
				QtCore.QThread.sleep(2)				
				count +=1
				position_x+=60
				position_y+=35
				if count % 10 ==0:
					position_x+= 80
					position_y=0
					count =0
		return





