#!user/bin/env python3
# -*- coding: gbk -*-
'''
Created on 2017��1��25��

@author: mazicwong
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages=set()
random.seed(datetime.datetime.now())

#��ȡҳ�����Ѓ������б�
def getInternalLinks(bsObj,includeUrl):
    internalLinks=[]  #list,�ɱ䳤
    #�ҵ�������'/'��ͷ������
    for link in bsObj.findAll("a",href=re.compile("^(/|.*)"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

#��ȡҳ�������������б�
def getExternalLinks(bsObj,excludeUrl):
    externalLinks=[]
    #�ҳ�������"http"����"www"��ͷ��첻����ǰurl������
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks
    
def splitAddress(address):
    addressParts=address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html=urlopen(startingPage)
    bsObj=BeautifulSoup(html,"html.parser")
    externalLinks=getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks=getInternalLinks(startingPage)
        return getNextExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]
    
def followExternalOnly(startingSite):
    externalLink=getRandomExternalLink("http://oreilly.com")
    print("���������: "+externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")
    
    
    
    
    
    
    
    