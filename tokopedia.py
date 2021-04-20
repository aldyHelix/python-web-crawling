import requests
from bs4 import BeautifulSoup
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
keyword = 'laptop'
url = 'https://www.tokopedia.com/search?st=product&q={}&navsource=home'.format(keyword)
page = requests.get(url, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')

if page.status_code == 200:
	rows = soup.find("div", class_="css-rjanld")
	divs = rows.findAll("div", {"class" : "css-1db8ct"})
	for div in divs:
		print(div.find("div", class_="css-18c4yhp").text)
elif page.status_code == 404:
	print('page not found')
else:
	print('check connection!')


