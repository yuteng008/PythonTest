from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
# print(html)

soup = BeautifulSoup(html,features='lxml')
print(soup.h1)

all_href = soup.find_all('a')
all_href = [i['href']for i in all_href]
print('\n',all_href)