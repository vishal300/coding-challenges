from urllib.request import Request, urlopen
import re
from collections import OrderedDict

import threading
import time
url="http://medium.com/"
def recursiveUrl(url,link,depth):
       # print(link)
        if depth<=5:
            return url
        else:
            f = open('output.txt', 'w')
            f.write(str(link))
            f.close()
            page = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
            soup = urlopen(page).read().decode('utf-8')
            soup=str(soup)
            newlinks = re.findall('http[s]?://*.medium.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',soup)
            newlink=[newlinks]
            print(newlink)
            if len(newlink) == 0:
                return url
            else:
                return newlink, recursiveUrl(url,newlink,depth-1)
 
                print(newlink)

def getLinks(url):
    page = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = urlopen(page).read().decode('utf-8')
   # soup=str(soup)
    links = re.findall('http[s]?://*.medium.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',soup)
    unique_list = list(OrderedDict.fromkeys(links))
    del unique_list[-1]



    for link in unique_list:
        links.append(recursiveUrl(url, link,55555))
    return links
    #print(link)
getLinks(url)



