from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')

soup = BeautifulSoup(html,features='lxml')
img_link = soup.find_all("img",{"src":re.compile('.?\.jpg')})
for link in img_link:
    print(link['src'])