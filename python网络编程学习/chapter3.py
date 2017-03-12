#!user/bin/env python3
# -*- coding: gbk -*-
'''
Created on 2017��1��20��

@author: mazicwong
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# ��ʱ�����������������α�����
random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen("https://en.wikipedia.org/" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

    
