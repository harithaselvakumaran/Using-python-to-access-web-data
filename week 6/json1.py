import json
import urllib.request, urllib.parse, urllib.error

url=input('Enter: ')
uh=urllib.request.urlopen(url)
data=uh.read()

info=json.loads(data)
sum=0
count=0
for item in info['comments']:
    y=item['count']
    sum=sum+y
    count=count+1
print('Sum: ',sum)
print('Count: ',count)
