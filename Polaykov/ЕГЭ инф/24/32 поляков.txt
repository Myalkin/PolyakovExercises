with open ("C:\\Users\\rmyal\\Desktop\\k7b-6.txt", "r") as F:
    s=F.readline()
curlen=0
maxlen=0
for i in range (1,len(s)):
    if s[i]=='A' and s[i-1]=='D' and s[i+1]=='F' or s[i]=='D' and s[i-1]=='F' and s[i+1]=='A' or s[i]=='F' and s[i-1]=='A' and s[i+1]=='D':
        curlen+=1
        if curlen>maxlen:
            maxlen=curlen
    else:
        curlen=1
print (maxlen+1) 
