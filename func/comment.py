from ui_to_py.dialog import *

from PyQt5 import QtCore, QtGui, QtWidgets

import requests,threading,json, sys,re
import random
from bs4 import BeautifulSoup
from urllib.parse import unquote

class Comment:
	headers= {
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
				"sec-ch-ua-mobile": "?0",
				"sec-ch-ua-platform": '"Windows"',
				"Upgrade-Insecure-Requests": '1',
				"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
				}

	def login(self,data):	
		
		session = requests.Session()
		url = 'https://giaimasohoc.com/login/login'
		
		soup_full = BeautifulSoup(session.get(url).text,'lxml') # Lấy data sau khi login thành công
		_xfToken = soup_full.find(attrs={'name':'_xfToken'})['value']

		tk = data.split('|')[1]
		mk = data.split('|')[2]

		data_json = {'login': tk,
					'password':mk,
					'_xfToken':_xfToken
					}
		
		soup = session.post(url ,data=data_json, headers = self.headers).text # Lấy data sau khi login thành công
		if tk.lower() in soup.lower():
			self.new_signal.emit(int(data.split('|')[0]),'login thành công!','normal',False)		
			return {
					'_xfToken': _xfToken,'session':session,
					}
		
		self.new_signal.emit(int(data.split('|')[0]),'login thất bại!','red',True)
		return False


	#Lấy form để viết bài đăng hoặc trả lời comment 
	def get_form_cmt(self,session,data):
		data_total = session.get(self.link_cmt).text
		soup_full = BeautifulSoup(data_total,'lxml') # Lấy data sau khi login thành công

		

		attachment_hash= soup_full.find(attrs={'name':'attachment_hash'})['value']

		attachment_hash_combined = soup_full.find(attrs={'name':'attachment_hash_combined'})['value']		
		
		link_get_html = self.link_cmt.replace(self.link_cmt.split('/')[-1],'') + 'reply?quote=' + self.link_cmt.split('post-')[-1]
		get_html_msg = session.get(link_get_html).text
		soup_html_msg = BeautifulSoup(get_html_msg,'lxml')

		for a in soup_html_msg.find_all("textarea", class_="input js-editor u-jsOnly"):
			form_reply = f"{unquote(a.text)}<p>{data.split('|')[3]}<p>"

		
		return {
				"form_reply":form_reply,
				"attachment_hash":attachment_hash,
				"attachment_hash_combined":attachment_hash_combined,
				}


	#Lấy form để viết lên tường cá nhân (Profile)
	def get_link_profile(self,session):		
		
		data_total = session.get(self.link_cmt, timeout = 10).text
		soup_full = BeautifulSoup(data_total,'lxml') # Lấy data sau khi login thành công 			
		form_post= soup_full.find('form',action=re.compile('post'))['action']		
				
		if form_post:
				link_profile = 'https://giaimasohoc.com'+ form_post
		else:
			return 0 
		return link_profile


		# Ảnh được upload từ trong máy tính và lưu trên database của web	
	
	def upload_image(self,_xfToken,session,data):
		raw = self.link_cmt.split('.')[-1]
		id_thread =  raw.split('/')[0]					
		data_total	= self.get_form_cmt(session,data)
			

		url_upload = f"https://giaimasohoc.com/attachments/upload?type=post&context[thread_id]={id_thread}&hash={data_total['attachment_hash']}"
		form_data = {
						'_xfToken': _xfToken,
						'_xfResponseType': 'json',
						'_xfWithData': 1,

					}
		files = {
		'upload': open(data.split('|')[4],'rb')
		}		
		
		img_post =session.post(url = url_upload,files=files,data=form_data).json()
		link_post_imgae = "https://giaimasohoc.com"+img_post["link"]
		return link_post_imgae
				

			# Lấy form để gửi ảnh có trong data.split('|')[3] hoặc bài đăng
	

	def get_form_image(self,_xfToken,session,data):
		if data.split('|')[4] =="":
			form_image = ''	
		elif 'https://' in data.split('|')[4]:
			form_image = f'<br><img src="{data.split("|")[4]}" style="width: auto;" class="fr-fic fr-dii fr-draggable">'			

		# ''' Sử dụng ảnh trong máy tính '''		
		else:		

			link_post_imgae = self.upload_image(_xfToken,session,data)
			
			form_image =  f'<br><img src="{link_post_imgae}" style="width: auto;" class="fr-fic fr-dii fr-draggable">'
		
		return form_image

	def comment_threading(self,data):
		self.new_signal.emit(int(data.split('|')[0]),'Đang chạy.....', 'normal',False)
		data_login = self.login(data)	
		if not data_login == False:	
			if self.settings["options"] ==3 :				 			
				data_form_post = self.get_form_cmt(data_login['session'],data)	
				form_message = data_form_post["form_reply"]  #Trả lời bài viết
				
				link_post = self.link_cmt.replace(self.link_cmt.split('/')[-1],'add-reply')
				form_message = form_message + self.get_form_image(data_login["_xfToken"],data_login["session"],data)

				form_data = {
					'message_html': form_message,
					'attachment_hash': data_form_post["attachment_hash"],
					'attachment_hash_combined':data_form_post["attachment_hash_combined"],
					'_xfToken':data_login["_xfToken"],
					'_xfResponseType':'json'
				}

				post = data_login["session"].post(url = link_post, data = form_data, headers = self.headers).status_code



			elif self.settings["options"] ==4 :				
				data_form_post = self.get_form_cmt(data_login['session'],data)
				form_message = f"<p>{data.split('|')[3]}</p>" # Viết bài đăng
				
				link_post = self.link_cmt.replace(self.link_cmt.split('/')[-1],'add-reply')
				form_message = form_message + self.get_form_image(data_login["_xfToken"],data_login["session"],data)

				form_data = {
					'message_html': form_message,
					'attachment_hash': data_form_post["attachment_hash"],
					'attachment_hash_combined':data_form_post["attachment_hash_combined"],
					'_xfToken':data_login["_xfToken"],
					'_xfResponseType':'json'
				}

				post = data_login["session"].post(url = link_post, data = form_data,headers = self.headers).status_code


			elif self.settings["options"] ==5 :			
				form_message = f"<p>{data.split('|')[3]}</p>" #Viết lên tường cá nhân				
				link_post = self.get_link_profile(data_login["session"])

				form_data = {
							'message_html' :f"<p>{data.split('|')[3]}</p>",
							'_xfToken':data_login["_xfToken"],
						}

				post = data_login["session"].post(link_post, data= form_data, headers = self.headers).status_code		
				

			if post==200:			
				self.new_signal.emit(int(data.split('|')[0]),'Comment OK', 'blue',True)
			else:
				self.new_signal.emit(int(data.split('|')[0]),'Comment FALSE','red',False)	

		return



		



	