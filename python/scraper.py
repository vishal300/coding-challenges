from urllib.request import Request, urlopen
import re
req = Request('https://medium.com/', headers={'User-Agent': 'Mozilla/5.0'})
the_page =  urlopen(req).read()
print(the_page)
the_page=str(the_page)
links = re.findall('"((http)s?://.*?)"', the_page)
#Some how extract that wanted data

print(links)
links=str(links)
f = open('output.txt', 'w')
f.write(links)
f.close()

          
