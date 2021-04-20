import requests
import os
import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
#chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver.exe')
driver.get('https://shopee.co.id/search?keyword=laptop')
time.sleep(10)
SCROLL_PAUSE_TIME = 0.5 
current_height = 0
height = driver.execute_script("return document.body.scrollHeight")
while current_height <= height:
	driver.execute_script("window.scrollTo(0, {});".format(current_height))
	time.sleep(SCROLL_PAUSE_TIME)
	current_height += 50

time.sleep(15)
itemname = driver.find_elements_by_css_selector(".shopee-search-item-result__item")
#page_controller = driver.find_elements_by_css_selector(".shopee-page-controller")
active_page = driver.find_elements_by_css_selector(".shopee-button-solid")
#print(active_page[0])
with open('data.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["SN", "Name", "Price", "Sales", "Image URL", "Item URL"])
	#print(str(len(itemname)))
	for i in range(len(itemname)):
		products = itemname[i].find_elements_by_css_selector(".yQmmFK")
		price = itemname[i].find_elements_by_css_selector(".WTFwws")
		sales =  itemname[i].find_elements_by_css_selector(".go5yPW")
		if itemname[i] != [] :
			image_selector =  itemname[i].find_elements_by_css_selector("._25_r8I")

			if image_selector[0] != [] :
				image_url_tag = image_selector[0].find_elements_by_tag_name('img')
				image_url = image_url_tag[0].get_attribute("src")
			else:
				image_url = "-"
			
			item_selector =  itemname[i].find_elements_by_tag_name('a')

			if item_selector[0] != [] :
				item_url = item_selector[0].get_attribute("href")
			else:
				item_url = "-"

			if sales != [] :
				item_sales = sales[0].text
			else:
				item_sales = "0 terjual"
			 
			# print(item_url)
			# print(image_url)
			# print(item_sales)

			data = [i, products[0].text, price[0].text, item_sales, image_url, item_url]  
			print(data)

		writer.writerow(data)
		# else:
		# 	print('no title')

driver.quit()

