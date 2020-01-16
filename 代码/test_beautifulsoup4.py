from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import time

base_url = "https://baike.baidu.com"
his = ["/item/PUA/5999185#hotspotmining"]

for i in range(20):
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html,features='lxml')
    print(soup.find('h1').get_text(),'  Url:',his[-1])

    sub_urls = soup.find_all("a",{"target":"_blank","href":re.compile("/item/(%.{2})+$")})

    if len(sub_urls)!=0:
        his.append(random.sample(sub_urls,1)[0]['href'])
    else:
        his.pop()
    print(his)
    time.sleep(3)