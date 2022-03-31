import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

url = 'https://www.y8.com/?page='
path = 'C:/webdrivers/chromedriver.exe'

chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-infobar')
# chrome_options.add_argument('disable-notifications')

datas = []

for page in range(1,11):
    driver = webdriver.Chrome(executable_path=path, options=chrome_options)
    driver.get(url + str(page))
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    soup = BeautifulSoup(html , 'html.parser')
    items = soup.findAll('div', 'item thumb videobox')

    for i in items :
        gameName = i.find('h4', 'title ltr').text
        plays = ''.join(i.find('p', 'plays-count').text.strip().split('\n'))
        persentase = ''.join(i.find('span', 'number').text.strip().split('\n'))
        img = i.find('div', 'thumb-img-container').find('img')['data-src']
        datas.append([gameName, plays, persentase, img])

driver.close()

headers_exel = ['Game Name', 'Plays', 'Persentase', 'Image']
writer = csv.writer(open('result/Scraping Y8.csv', 'w', newline=''))

writer.writerow(headers_exel)
for data in datas:
    writer.writerow(data)