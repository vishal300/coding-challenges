from urllib.request import Request, urlopen
req = Request('https://medium.com/', headers={'User-Agent': 'Mozilla/5.0'})
the_page =  urlopen(req).read()
print(the_page)

Sring = the_page.decode()
#Some how extract that wanted data

f = open('output.txt', 'w')
f.write(Sring)
f.close()
          
