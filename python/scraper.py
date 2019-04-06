from urllib.request import Request, urlopen
import re
req = Request('https://medium.com/sitemap/posts/2019/posts-2019-03-27.xml', headers={'User-Agent': 'Mozilla/5.0'})
the_page =  urlopen(req).read()
the_page=str(the_page)

count=0

for links in re.findall('http[s]?://*.medium.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', the_page):
    #print(links)
    for link in re.findall('http[s]?://*.medium.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', links):
        print(link)
#Some how extract that wanted data
    f = open('scrap.txt', 'w')
    f.write(str(links))
    f.close()

          
