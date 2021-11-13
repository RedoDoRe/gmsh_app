
from ui_to_py.dialog import *
from func.emoji import *

from PyQt5 import QtCore, QtGui, QtWidgets
import pyperclip


class Table:
	#self: Parameter

	#QTableView has contextMenuEvent() event, to show a right-click menu:
	def context_menu_table(self,point):
		
		self.contextMenu = QtWidgets.QMenu(self.tableWidget)
		# self.contextMenu.setObjectName("tableMenu")

		#Choose row
		choose_row = QtWidgets.QAction('Chọn dòng bôi đen',self.tableWidget)
		choose_row.setShortcut('Space')
		choose_row.triggered.connect(lambda action : self.setStateNick())
		self.contextMenu.addAction(choose_row)

		#Add Sticker
		sticker = QtWidgets.QAction('Sticker',self.tableWidget)
		sticker.setShortcut('F3')
		sticker.triggered.connect(lambda action : self.showSticker())
		self.contextMenu.addAction(sticker)

		#Cancel row
		cancel_row = QtWidgets.QAction('Hủy những dòng đã chọn',self.tableWidget)
		cancel_row.setShortcut('Esc')
		cancel_row.triggered.connect(lambda action : self.uncheckNick())
		self.contextMenu.addAction(cancel_row)

		#Choose All
		choose_all = QtWidgets.QAction('Chọn tất cả',self.tableWidget)		
		choose_all.triggered.connect(lambda action : self.checkedNick())
		self.contextMenu.addAction(choose_all)

	
		

		#Refresh F5
		refresh = QtWidgets.QAction('Làm mới',self.tableWidget)
		refresh.setShortcut('F5')
		refresh.triggered.connect(lambda action : self.setNickOnTable())
		self.contextMenu.addAction(refresh)
		




		#Display Menu 
		self.contextMenu.exec_(self.tableWidget.mapToGlobal(point))   





	def createFile(self):
		file_name = self.form_file.lineEdit_file.text().strip()
		if file_name =='':
			msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='warning',
			boldtext='Lỗi tên file',
			text ='Tên file không thể để trống',
			ok =True,
			cancel = False)
			msg.exec_()

			return
		elif os.path.isfile(f'data/{file_name}.txt'):
			msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='warning',
			boldtext='Lỗi tên file',
			text ='File đã tồn tại vui lòng đặt tên khác!',
			ok =True,
			cancel = False)
			msg.exec_()		
			return
		elif'/' in file_name or '\\' in file_name:
			msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='warning',
			boldtext='Lỗi tên file',
			text ='Tên file không được chứa kí tự đặc biệt',
			ok =True,
			cancel = False)
			msg.exec_()		
			return

		open(f'data/{file_name}.txt','w')
		msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='information',
			boldtext='Thành công',
			text =f'Tạo thành công file {file_name}',
			ok =True,
			cancel = False)		
		
		if msg.exec() == 1:			
			self.form_file.close()

		self.comboBox.insertItem(0,file_name)
		self.comboBox.setCurrentText(file_name)
		try:
			self.import_nick.comboBox_list_file.insertItem(0,file_name)
			self.import_nick.comboBox_list_file.setCurrentText(file_name)
		except:
			pass

		self.showImportNick()
		# self.saveFileNick()

		return
	

	def deleteFile(self):
		file_name = self.comboBox.currentText()
		msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='question',
			boldtext='Thông báo',
			text =f"Bạn chắc chắn muốn xóa file {file_name}?",
			ok =True,
			cancel = True)
		
		if msg.exec()==1:
			os.remove(f'data/{file_name}.txt')
			index = self.comboBox.findText(file_name)  # find the index of text
			self.comboBox.removeItem(index)  # remove item from index
		
		return

	def setItemImportNick(self):		
		self.import_nick.comboBox_list_file.addItems(filename.replace('.txt','') for filename in os.listdir('data'))
		self.import_nick.comboBox_list_file.setCurrentText(self.comboBox.currentText())
		

	def saveFileNick(self):
		file_name = self.import_nick.comboBox_list_file.currentText().strip()
		data_raw = self.import_nick.textEdit_import_nick.toPlainText()
		data_nick = list(filter(None,data_raw.strip().split('\n')))
		
		if file_name=='':
			msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='warning',
			boldtext='Cảnh báo',
			text =f"Tên file trống, cần khởi tạo!",
			ok =True,
			cancel = False)
			msg.exec_()
			return
		elif len(data_nick) <= 0:
			msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='warning',
			boldtext='Cảnh báo',
			text =f"Vui lòng nhập tài khoản cần lưu",
			ok =True,
			cancel = False)
			msg.exec_()
			return
		elif '|' not in data_raw:
			msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='warning',
			boldtext='Cảnh báo',
			text =f"Sai định dạng dữ liệu",
			ok =True,
			cancel = False)
			msg.exec_()
			return
		# Lưu nick vào file name		

		with open(f'data/{file_name}.txt','a', encoding ='utf-8') as f:
			for data in data_nick:
				f.write(data+'\n')

		
		# Lọc trùng các nick ở trong file name
		with open(f'data/{file_name}.txt','r', encoding ='utf-8') as f:		
			data_total = set(f.readlines())  		
			with open(f'data/{file_name}.txt', 'w',encoding ='utf-8') as f:
					f.writelines(data_total)



		msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='information',
			boldtext='Thành công',
			text =f"Đã lưu {len(data_nick)} tài khoản vào file {file_name}\n",
			ok =True,
			cancel = True)		
		
		if msg.exec() == 1:			
			self.import_nick.close()

		self.setNickOnTable()

		return



	def getDataNick(self):		
		file_name = self.comboBox.currentText()

		#Lỗi trường hợp file chưa có thì try - except
		try:
			with open(f'data/{file_name}.txt','r') as f:
				list_data_nick = f.readlines()	

			list_data_info = [data.replace('\n','') for data in list_data_nick]
		except:
			pass

		return list_data_info
		



	def setNickOnTable(self):
		self.tableWidget.setColumnWidth(0,35)
		self.tableWidget.setColumnWidth(1,40)
		self.tableWidget.setStyleSheet("QAbstractItemView::indicator {width: 25px; height:25px;}\n")
			


		self.checkbox_list = list()
	

		list_data_info = self.getDataNick()
		self.tableWidget.setRowCount(len(list_data_info))
		
		for index, item in enumerate(list_data_info):		
							
			taikhoan = item.split('|')[0]
			matkhau = item.split('|')[1]
			taikhoan_widget = QtWidgets.QTableWidgetItem(taikhoan)
			matkhau_widget = QtWidgets.QTableWidgetItem(matkhau)
			cmt_widget = QtWidgets.QTableWidgetItem("")
			link_widget = QtWidgets.QTableWidgetItem("")
			status_widget= QtWidgets.QTableWidgetItem("")

			
			stt_widget = QtWidgets.QTableWidgetItem(str(index+1))
			stt_widget.setTextAlignment(QtCore.Qt.AlignCenter)	

			checkbox_item = QTableWidgetItem()			
			checkbox_item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
			checkbox_item.setCheckState(QtCore.Qt.Unchecked) 
			self.checkbox_list.append(checkbox_item)

			self.tableWidget.setItem(index,0,checkbox_item)				
			self.tableWidget.setItem(index,1,stt_widget)
			self.tableWidget.setItem(index,2,taikhoan_widget)
			self.tableWidget.setItem(index,3,matkhau_widget)
			self.tableWidget.setItem(index,4,cmt_widget)
			self.tableWidget.setItem(index,5,link_widget)
			self.tableWidget.setItem(index,6,status_widget)

		return

	
	def setStateNick(self):		
		selection = [r.row() for r in self.tableWidget.selectedIndexes()]
		selection = list(set(selection))
		for i in selection:
			if self.checkbox_list[i].checkState() == QtCore.Qt.Checked:
				self.checkbox_list[i].setCheckState(QtCore.Qt.Unchecked)
			else: 
				self.checkbox_list[i].setCheckState(QtCore.Qt.Checked)

		self.get_list_checked()



	def clickUploadImage(self):
		selection = [r.row() for r in self.tableWidget.selectedIndexes()]
		selection = list(set(selection))		

		for row in selection:
			if self.tableWidget.currentColumn() ==5:
				link_image = self.getUploadImage()[0]
				item_link = QtWidgets.QTableWidgetItem(link_image)
				self.tableWidget.setItem(row,5,item_link)
		

			

			
		
	def getUploadImage(self):
		file_filter ="Images (*.png *.gif *.jpg);;Text files (*.txt);;XML files (*.xml)"
		link_image = QtWidgets.QFileDialog.getOpenFileName(
								parent = self,
								caption = "Chọn đường dẫn ảnh",
								directory = os.getcwd(),
								filter = file_filter,	
								)
		print(link_image[0])
		return link_image


	def get_list_checked(self):
		list_checked = list()
		for i in self.checkbox_list:
			if i.checkState() == QtCore.Qt.Checked:
				list_checked.append(i.row())
		
		
		return list_checked


	def getData(self):	
		list_checked = self.get_list_checked()
		list_account = list()
		for row in list_checked:
			taikhoan = self.tableWidget.item(row,2).text().strip()
			matkhau = self.tableWidget.item(row,3).text().strip()
			cmt = self.tableWidget.item(row,4).text().strip()
			image = self.tableWidget.item(row,5).text().strip()
			data = str(row)+'|'+taikhoan+'|'+matkhau+'|'+cmt+'|'+image
			list_account.append(data)
		return list_account

	def findNickOnTable(self):		
		name = self.lineEdit_search.text().strip()
		
		for row in range(self.tableWidget.rowCount()):
			taikhoan = self.tableWidget.item(row,2).text()
			if name not in taikhoan:
				self.tableWidget.setRowHidden(row,True)
			else:
				self.tableWidget.setRowHidden(row,False)



	def setCheckAll(self):	
		for checkbox in self.checkbox_list:		
			if self.checkBox_num.isChecked():
				checkbox.setCheckState(QtCore.Qt.Checked)

			else:
				checkbox.setCheckState(QtCore.Qt.Unchecked)
			
				

	def checkedNick(self):
		for i in self.checkbox_list:
			if i.checkState()==QtCore.Qt.Unchecked:
				i.setCheckState(QtCore.Qt.Checked)
		return


	def uncheckNick(self):
		for i in self.checkbox_list:
			if i.checkState()==QtCore.Qt.Checked:
				i.setCheckState(QtCore.Qt.Unchecked)
		return



	def deleteTable(self):
		selection = [r.row() for r in self.tableWidget.selectedIndexes()]
		selection = list(set(selection))
		
		col_selection = self.tableWidget.currentColumn()
		for r in selection:
			item = QtWidgets.QTableWidgetItem("")
			self.tableWidget.setItem(r,col_selection,item)
		
	def copyTable(self):
		copies_text =''
		selection = [r.row() for r in self.tableWidget.selectedIndexes()]
		selection = list(set(selection))		
		for r in selection:
			try:
				copies_text += self.tableWidget.item(r,4).text() +'\n'	# Cột thứ 4 là cột commnent
			except:
				pass

		#QApplication.clipboard() copy va paste
		QApplication.clipboard().setText(copies_text) 		
		
	def pasteTable(self):
		count = 0 		
		selection = [r.row() for r in self.tableWidget.selectedIndexes()]
		selection = list(set(selection))
		paste_text = QApplication.clipboard().text().split('\n')
		for r in selection:	
			try:		
				item = QtWidgets.QTableWidgetItem(paste_text[count])
				self.tableWidget.setItem(r,4,item)
				count +=1
			except:
				pass
			

	def convert_cmt_emoji(self,cmt):
		msg =""
		list_words = cmt.split(' ')
		for word in list_words:
			msg += emoji.get(word.upper(),word) + " "
		return msg


	def setCmtOnTable(self):
		list_checked = self.get_list_checked()
		list_cmt = list(filter(None,self.textEdit_export_cmt.toPlainText().split('\n')))
	
		for i in range(len(list_checked)):
			try:
				content = self.convert_cmt_emoji(list_cmt[i])
				item = QtWidgets.QTableWidgetItem(content)				
				self.tableWidget.setItem(list_checked[i],4,item)
			except:
				pass
		self.showPageSetting()

		
		




		




		





