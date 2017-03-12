#!user/bin/env python3
# -*- coding: gbk -*-
'''
Created on 2017��1��20��

@author: mazicwong
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bs0bj = BeautifulSoup(html, "html.parser")
# nameList = bs0bj.findAll("span", {"class": "green"})
# for name in nameList:
#     print(name.get_text())



html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
#һ��ʼfindallд��Сд��,һֱ����ȥ....��ʾ TypeError: 'NoneType' object is not callable
for image in images:
    print(image["src"])




