import requests
from requests import session
import settings
import main
import random

class Captcha(object):
	def two_cap(self):
		if self.API_KEY = False:
			Captcha().manual_file()
		else:
			pass
	    API_KEY = self.API_KEY
	    site_key = self.site_key
	    url = self.link
	r = requests.session()
	try:
	    captcha_id = r.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(API_KEY, site_key, url)).text
	    recaptcha_answer = r.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id)).text
	    while 'CAPCHA_NOT_READY' in recaptcha_answer:
	        sleep(1)
	        recaptcha_answer = r.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(API_KEY, captcha_id)).text
	    if 'ERROR_CAPTCHA_UNSOLVABLE' in recaptcha_answer:
	    	print "Invalid Captcha Token..."
	    	print "Retrying..."
	        Captcha().two_cap()
	    gresponse = recaptcha_answer.split('|')[1]
	    self.gresponse = gresponse
	except:
		print "Error..."
		print "Retrying..."
	TwoCaptcha().worker()

	def manual_file(self):
		print "Looking for Captcha Token..."
		print "Please Open Manual Solver to Complete this Process..."
		with open('C:/xamp/htdocs/captcha/files/captcha.txt').read().splitlines() as self.captcha_file:
			Captcha().manual()

	def manual(self):
		while "None" in self.captcha_file:
			print "No Valid Captcha Token Found..."
			print "Keep Trying!"
			sleep(15)
			Captcha().manual()
		else:
			self.gresponse = random.choice(self.captcha_file)
			print "Successfully Found a Captcha Token!"
			rid = self.captcha_file.replace(self.gresponse, "")
			self.captcha_file.close()