from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

html = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
).read().decode('utf-8')
# print(html)

# res = re.findall(r"<p>(.+?)</p>",html, flags=re.DOTALL)
# print("\nPage tile is: ",res[0])

res = re.findall(r'href="(.*?)"',html)
print("\nPage tile is: \n",res)

# soup = BeautifulSoup(html,features='lxml')
# print(soup.h1)
# print('\n',soup.p)

# all_href = soup.findall('篮球')
# print(all_href)