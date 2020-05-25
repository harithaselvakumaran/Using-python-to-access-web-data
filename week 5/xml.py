import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url=input('Enter: ')
uh=urllib.request.urlopen(url)
data=uh.read()

tree=ET.fromstring(data)
result=tree.find('comments/comment')    #returns a list
c=0
sum=0
for item in result:
    x=item.find('count').text
    x=int(x)
    print(x)
    sum=sum+x
    c=c+1
print('Sum: ',sum)
print('Count: ',c)
