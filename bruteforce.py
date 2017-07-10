import requests
from requests import session
import bs4
from bs4 import BeautifulSoup
import time
from time import sleep
import captcha
import main
import ATC
import billing
import cli

class BruteForce(object):
    def wait(self):
        r = requests.session()
        counter = 0
        self.retry_count = counter + 1

        product_headers = {
        'Host': 'www.adidas.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.adidas.com/us/',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        }

        try:
            splash_wait = r.get(self.link, headers=product_headers, proxies=self.proxy)
            data = splash_wait.text
            soup = BeautifulSoup(data, "lxml")
            if "data-sitekey" in data:
                find_site_key = soup.find("div", { "class" : "g-recaptcha" })
                site_key = str(find_site_key).split('data-sitekey="')[1].split('"')[-1]
                self.site_key = site_key
                ATC.Add()
            if splash_wait.status_code == 404:
                print "Banned Thread"
            else:
                sleep(self.Refresh_Rate)
                BruteForce().wait()

        except:
            print "There was an Unexpected error..."
            print "Retrying..."
            sleep(self.refresh_rate)
            BruteForce.wait()
