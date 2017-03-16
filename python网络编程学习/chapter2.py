#!user/bin/env python3
# -*- coding: gbk -*-
'''
Created on 2017��1��20��

@author: mazicwong
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, "html.parser")
images = soup.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
#һ��ʼfindallд��Сд��,һֱ����ȥ....��ʾ TypeError: 'NoneType' object is not callable
for image in images:
    print(image["src"])




