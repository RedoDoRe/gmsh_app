from ui_to_py.dialog import *
from PyQt5 import QtCore, QtGui, QtWidgets

import requests,threading
import random
from bs4 import BeautifulSoup

class GetId:

	def get_id_thread(self):	

		session = requests.Session()
		url = 'https://giaimasohoc.com/login/login'	

		rq = session.get(url).text

		soup_full = BeautifulSoup(rq,'lxml') # Lấy data sau khi login thành công
		
		_xfToken = soup_full.find(attrs={'name':'_xfToken'})['value']


		data_json = {'login':'tuantran' ,
				'password':'thienha#qc',
				'_xfToken':_xfToken
				}

		soup = session.post(url ,data=data_json, headers = self.headers).text # Lấy data sau khi login thành công
			

		data = session.get(self.settings['list_link'][0]).text
		soup_full = BeautifulSoup(data,'lxml')

		get_id = soup_full.find_all('article',class_='message message--post js-post js-inlineModContainer')
		list_id = [a['id'].split('-')[-1] for a in get_id]
		return list_id

	def reaction_topic(self):
		list_link =list()
		for post_id in self.get_id_thread():
			link = f'https://giaimasohoc.com/posts/{post_id}/react?reaction_id={random.choice(self.settings["reaction"])}'
			list_link.append(link)
		
		return list_link


class Reaction:
	headers = {
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
				"sec-ch-ua-mobile": "?0",
				"sec-ch-ua-platform": '"Windows"',
				"Upgrade-Insecure-Requests": '1',
				"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
				}
	 
	def login_gmsh(self,data):		
		session = requests.Session()
		url = 'https://giaimasohoc.com/login/login'	
				
		soup_full = BeautifulSoup(session.get(url).text,'lxml') # Lấy data sau khi login thành công
		
		_xfToken = soup_full.find(attrs={'name':'_xfToken'})['value']

		tk = data.split('|')[1]
		mk = data.split('|')[2]
	

		data_json = {'login': tk,
				'password':mk,
				'remember': 1,
				'_xfRedirect':'/',
				'_xfToken':_xfToken
				}
		

		soup = session.post(url ,data=data_json, headers = self.headers).text # Lấy data sau khi login thành công
		

		if tk.lower() in soup.lower():
			self.new_signal.emit(int(data.split('|')[0]),'login thành công!','normal',False)
			return (_xfToken,session)
		self.new_signal.emit(int(data.split('|')[0]),'login thất bại!','red',True)
		return False

	def reaction_post(self):	
	
		_list_link =list()
		for link in self.settings['list_link']:
			post_id = link.split('post-')[1].rstrip()
			url = f'https://giaimasohoc.com/posts/{post_id}/react?reaction_id={random.choice(self.settings["reaction"])}'
			_list_link.append(url)
		return _list_link


	def reaction_profile(self):
		_list_link =list()
		for link in self.settings['list_link']:
			post_id = link.split('post-')[-1].rstrip()
			url = f'https://giaimasohoc.com/profile-posts/{post_id}/react?reaction_id={random.choice(self.settings["reaction"])}'
			_list_link.append(url)

		return _list_link


	def reaction(self,data,_xfToken,session,url,num,num_link):		
		form_data = {
				'reaction_id':random.choice(self.settings["reaction"]),
				'_xfToken' : _xfToken
				}
		react = session.post(url = url, data= form_data)

		
		if react.status_code==200 or react.status_code == 301:
			num.append(react)
			display_num = str(len(num))+'/'+ str(num_link)
			self.new_signal.emit(int(data.split('|')[0]),'Like OK ' + display_num,'blue',True)
		else:
			self.new_signal.emit(int(data.split('|')[0]),'Like FALSE','red',False)





	def reaction_threading(self,data):
		num = []
		self.new_signal.emit(int(data.split('|')[0]),'Loading...','normal',False)
		data_login = self.login_gmsh(data)
		if data_login:
			_xfToken,session = data_login
			try:
				if self.settings['options'] ==0:
					list_link = self.reaction_post()				
				elif self.settings['options'] ==1:
					list_link = self.reaction_profile()
				elif self.settings['options'] ==2:
					list_link = self.list_link_topic						
			
				num_link = len(list_link)				

				for link in list_link:
					threading.Thread(target = self.reaction, args = (data,_xfToken,session,link,num,num_link)).start()
			except Exception as e:	
				print(e)			
				self.new_signal.emit(int(data.split('|')[0]),'Err','red',False)



