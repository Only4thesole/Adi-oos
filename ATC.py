import requests
from requests import session
import bs4
from bs4 import BeautifulSoup
import bruteforce
import billing
import checkout
import cli
import main
import captcha

class ATC(object):

    pass

    def add(self):
        r = requests.session()

        product_headers = {
        'Host': 'www.adidas.com',
        'Connection': 'keep-alive',
        'Content-Length': '611',
        'Origin': 'http://www.adidas.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': self.link,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        }

        ATC_data = {
        'layer': 'Add To Bag overlay',
        'pid': '{}_{}'.format(self.sku, self.size),
        'Quantity': '1',
        'g-recaptcha-response': self.gresponse,
        'masterPid': self.sku,
        'sessionSelectedStoreID': 'null',
        'ajax': 'true',
        }

        try:
            ATC = r.post('http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-MiniAddProduct', headers=product_headers, data=ATC_data, proxies=self.proxy)

        except:
            print "Unknown Error..."
            print "Retrying"
            ATC().add()

        headers = {
        'Host': 'www.adidas.com',
        'Connection': 'keep-alive',
        'Content-Length': '69',
        'Cache-Control': 'max-age=0',
        'Origin': 'https://www.adidas.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'https://www.adidas.com/us/checkout-start',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        }

        get_data = r.get('https://www.adidas.com/us/checkout-start', headers=headers, proxies=proxy)
        data = r.text
        soup = BeautifulSoup(data, "lxml")
        findsecurekey = soup.find("input", { "name" : "dwfrm_login_securekey" })
        self.securekey = str(findsecurekey).split('value=')[1].split('"')[1]
        finddwcont = soup.find("form", { "class" : "fancyform clearfix" })
        self.dwcont = str(findwcont).split('"')[1].split('=')[1]

        info_headers = {
        'Host': 'www.adidas.com',
        'Connection': 'keep-alive',
        'Content-Length': '108',
        'Origin': 'https://www.adidas.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'text/html, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.adidas.com/us/delivery-start',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        }

        info_data = {
        'stateCode': self.state,
        'address1': self.address1,
        'address2': self.address2,
        'editable': 'true',
        'shippingMethodID': '2ndDay',
        'shippingMethodType': 'inline',
        'page': 'delivery',
        }
