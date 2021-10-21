import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import csv



outfile = open('exported_data.csv','w', newline='')
writer = csv.writer(outfile)
writer.writerow(["Price", " Vin"])

URL = "https://www.bmwseattle.com/new-vehicles/m3/?_dFR%5Bmake%5D%5B0%5D=BMW&_dFR%5Bmodel%5D%5B0%5D=M3&_dFR%5Btype%5D%5B0%5D=New&_paymentType=our_price"
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome('chromedriver',options=chrome_options)
driver.get(URL)
time.sleep(5)
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

price_spans = soup.find_all('span', {'class' : 'price'})
for price in price_spans:
    writer.writerow([price.text])

vin_divs = soup.find_all('div', {'class' : 'vin-row'})
for vin in vin_divs:
    writer.writerow([vin.text])

outfile.close()
driver.close() # closing the webdriver
