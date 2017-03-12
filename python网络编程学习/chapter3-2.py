#!user/bin/env python3
# -*- coding: gbk -*-

'''
Created on 2017��1��24��

@author: mazicwong
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()  # �ü���set����ȥ���ظ���URL

def getLinks(pageUrl):
    global pages
    html = urlopen("https://en.wikipedia.org/" + pageUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    try:
        print(bsObj.h1.get_text())
        #print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("ҳ��ȱ��һЩ����! �������õ���...")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:  #��������ҵ�������,���ǲ����Ѿ��е�������
                # �������µ�ҳ��ʱ
                newPage = link.attrs["href"]
                print("--------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")
