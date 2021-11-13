from ui_to_py.dialog import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pyperclip
import datetime,time
import random

class PageSetting:

	def get_link(self):
		list_link = list(filter(None,self.textEdit_link.toPlainText().strip().split('\n')))
		return list_link

	def get_reaction(self):
		list_reaction = list()
		if self.checkBox_like.isChecked(): list_reaction.append(1)
		if self.checkBox_love.isChecked(): list_reaction.append(2)
		if self.checkBox_wow.isChecked(): list_reaction.append(4)	
		return list_reaction

	def get_num_thread(self):
		num_thread = self.spinBox_threading.value()
		return num_thread

	def enable_hour(self):
		
		time = datetime.datetime.now()
		h_display = time.strftime("%H") 
		m_display = str(int(time.strftime("%M")) +1)

		self.set_start_gio.setText(h_display)
		self.set_start_phut.setText(m_display)

		self.set_start_gio.setEnabled(self.checkBox_timer.isChecked())
		self.set_start_phut.setEnabled(self.checkBox_timer.isChecked())


	def enable_minutes(self):
		m_f = int(self.delay_from.text())
		m_t = int(self.delay_to.text())
		if m_t < m_f:
			msg = Dialog_MessageBox(
			self.styleSheet(),
			icon='warning',
			boldtext='Không hợp lệ',
			text ='Thời gian giãn cách từ nhỏ đến lớn',
			ok =True,
			cancel = False)
			msg.exec_()		
			return
		
		m_r = random.randint(m_f, m_t)
		

		self.delay_from.setEnabled(self.checkBox_delay.isChecked())
		self.delay_to.setEnabled(self.checkBox_delay.isChecked())
		return m_r


	def condition_time(self):
		hour = int(self.set_start_gio.text())
		minutes = int(self.set_start_phut.text())
		if hour >23: 
			hour = 23
			self.set_start_gio.setText(str(hour))			
		if minutes>59:
			minutes =59
			self.set_start_phut.setText(str(minutes))

		

		

	def count_hour(self):
		time = datetime.datetime.now()
		h_n = int(time.strftime("%H"))
		m_n = int(time.strftime("%M"))
		time_n = h_n*3600 + m_n*60

		h_s = int(self.set_start_gio.text())
		m_s = int(self.set_start_phut.text())
		time_s = h_s*3600 + m_s*60

		time_run = time_s - time_n	
		return time_run


	def check_option(self):
		for i in self.list_options:
			if i.isChecked():				
				return self.list_options.index(i)
				

	def settings(self):
		settings_value = {'reaction':self.get_reaction(),
							'list_link':self.get_link(),
							'delay' : self.enable_minutes(),
							'counter_thread' : self.get_num_thread(),
							'timer': self.count_hour() if self.checkBox_timer.isChecked() else False,
							'options':self.check_option()


		}	
		return 	settings_value	
