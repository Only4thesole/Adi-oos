import requests
from requests import session
import bs4
from bs4 import BeautifulSoup
import json

class App(object):

	pass

	def input(self):
		link = "http://www.adidas.com/apps/yeezy"
		self.link = link

	def proxy(self):
		with open("C:/Users/Nick/Desktop/NickBot/files/proxies.txt").read().splitlines() as self.file:
		self.BruteForceThreads = sum(1 for line in self.file)
		App().getproxy()

	def getproxy(self):
		proxy_line = random.choice(self.file)
		ip = str(proxy_line).split(':')[0]
		port = str(proxy_line).split(':')[1]
		username = str(proxy_line).split(':')[-2]
		password = str(proxy_line).split(':')[-1]
		proxy = {"http":"http://{}:{}@{}:{}".format(username, password, ip, port)}
		self.proxy = proxy
		rid = self.file.replace(proxy_line, "")


	def settings(self):
		with open('C:/Users/Nick/Desktop/NickBot/files/settings.json') as json_data_file:
		    data = json.load(json_data_file)

		try:
			self.API_KEY = data['SETTINGS']['2Captcha_API']
			self.rps = data['SETTINGS']['2Captcha_Requests_Per_Session']
			self.cooldown = data['SETTINGS']['2Captcha_Request_Cooldown']
			self.refresh_rate = data['SETTINGS']['Splash_Refresh_Rate']
		except:
			print "There are NO Saved Values in Settings..."
			print "Using Default Settings..."
			print "You Will Need to Solve Captchas Manually..."
			self.API_KEY = False
			self.rps = False
			self.cooldown = False
			self.refresh_rate = 40
