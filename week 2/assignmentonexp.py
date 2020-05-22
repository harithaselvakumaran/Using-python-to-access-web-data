import re
fh=input('Enter file name: ')
fname=open(fh)
sum=0
for line in fname:
    line=line.rstrip()
    y=re.findall('[0-9]+',line)
    for i in y:
        i=int(i)
        sum=sum+i
print(sum)
