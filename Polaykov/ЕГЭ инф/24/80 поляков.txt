with open ("C:\\Users\\rmyal\\Desktop\\k8-4.txt","r") as F:
    s=F.readline()
curlen=0
maxlen=0
for i in range (1,len(s)):
    if s[i]!=s[i-1]:
       curlen+=1
       if curlen>maxlen:
           maxlen=curlen
    else:
        curlen=1
print(maxlen)       