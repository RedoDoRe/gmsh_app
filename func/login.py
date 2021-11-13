from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import os, time,sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager




class Login:
	path_driver = ChromeDriverManager().install()
	def ChromeOptions(self,position_x,position_y):
		option= Options()
		option.add_argument(f"--window-position={position_x},{position_y}")
		option.add_argument(("--window-size=1100,550"))# kích cỡ cửa sổ width x height
		option.add_argument("--disable-infobars")  # tắt thanh bar Notification chrome bị điều khiển
		option.add_argument("--disable-gpu") # tắt extension
		option.add_argument("--no-sandbox") 	# tắt sanbox
		option.add_argument("--log-level=3")
		# option.add_extension('./extensions/cookieFlus.crx') # Thêm extension
		option.add_argument("--autoplay-policy=no-user-gesture-required")

		option.add_experimental_option("detach", True)  # giữ chrome luôn mở

		option.add_experimental_option("excludeSwitches", ["enable-automation"])

		prefs ={
		"profile.default_content_setting_values.notifications": 2,
		'credentials_enable_service': False,
		"profile": {
		'password_manager_enabled': False,
		}}
		option.add_experimental_option('prefs',prefs) 
		driver = webdriver.Chrome(options = option,executable_path= self.path_driver)
		
		return driver

	def login_driver(self,data,position_x,position_y):
		driver = self.ChromeOptions(position_x,position_y)
		driver.get('https://giaimasohoc.com/login/login')
		time.sleep(1)
		driver.find_element_by_name('login').send_keys(data.split('|')[1])
		time.sleep(1)
		driver.find_element_by_name('password').send_keys(data.split('|')[2])
		time.sleep(1)
		driver.find_element_by_class_name('button--primary.button.button--icon.button--icon--login').click()
		time.sleep(1)
		try:
			WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'p-navgroup-linkText')))
			driver.get(self.settings['list_link'][0])
			time.sleep(1)
			self.new_signal.emit(int(data.split('|')[0]),'Đăng nhập OK','blue',True)
		except TimeoutException:
			self.new_signal.emit(int(data.split('|')[0]),'Đăng nhập FALSE','red',False)
			driver.quit()
		return





