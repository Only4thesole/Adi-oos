import requests
from requests import session
import settings
import main

class TwoCaptcha(object):

	pass

	def worker(self):
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
	        TwoCaptcha().worker()
	    gresponse = recaptcha_answer.split('|')[1]
	    self.gresponse = gresponse
	except:
		print "Error..."
		print "Retrying..."
	TwoCaptcha().worker()
