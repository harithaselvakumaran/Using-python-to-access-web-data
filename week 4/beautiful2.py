import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignoring ssl certificates
ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter: ')
pos=input('Enter position: ')
count=input('Enter count: ')
pos=int(pos)
count=int(count)

for i in range(count):
    html=urllib.request.urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    l=list()
    for tag in tags:
        a=tag.get('href',None)
        l.append(a)
    print(l[pos-1])
    url=l[pos-1]
