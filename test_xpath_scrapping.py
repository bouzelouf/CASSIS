from lxml import html
import requests
from selenium import webdriver

'''
page = requests.get("http://econpy.pythonanywhere.com/ex/001.html")
tree = html.fromstring(page.content)
#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

print ('Buyers: ', buyers)
print ('Prices: ', prices)
'''

driver = webdriver.Chrome('//sites.google.com/a/chromium.org/chromedriver/home')
driver.get('http://econpy.pythonanywhere.com/ex/001.html')

tree = lxml.html.fromstring(driver.page_source)

results = tree.xpath('//*[@id="p-40"]/div[4]/table/tbody/tr/td[1]/text()')
results[1].strip()
