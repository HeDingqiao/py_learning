from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
pages=set()
random.seed(datetime.datetime.now())
def getInternalLinks(soup,includeUrl):
    internalLinks=[]
    for link in soup.findAll("a",href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks
def getExternalLinks(soup,excludeUrl):
    externalLinks=[]
    for link in soup.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks
def splitAddress(address):
    addressParts=address.replace("http://","").split("/")
    return addressParts
def getRandomExternalLinks(startingPage):
    html=urlopen(startingPage)
    soup=BeautifulSoup(html)
    externalLinks=getExternalLinks(soup,splitAddress(startingPage)[0])
    if len(externalLinks)==0:
        internalLinks=getInternalLinks(startingPage)
        return getNextExternalPage(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]
def getNextExternalPage(intern)
    html=urlopen(intern)
    soup=BeautifulSoup(html)
    ex=getExternalLinks(soup,splitAddress(intern)[0])
    return getExternalLinks(ex[random.randint(0,len(ex)-1)])
def followExternalOnly(startingSite):
    externalLink=getRandomExternalLinks("http://www.baidu.com")
    print("Random external link is"+externalLink)
    followExternalOnly(externalLink)
followExternalOnly("http://www.baidu.com")

