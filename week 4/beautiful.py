import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl #for https sites

#Ignoring SSL certifications
ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter')
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')   #gives you a clean html file

#Retrieving anchor tags
sum=0
count=0
tags=soup('span')      # Returns a List and type the tag you want
for tag in tags:
    a=tag.contents[0]    #gives you contents of the tag
    b=int(a)
    sum=sum + b
    count=count + 1
print('Count: ',count)
print('Sum: ',sum)
