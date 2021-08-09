with open ("C:\\Users\\rmyal\\Desktop\\24-j5.txt","r") as F:
    s=F.readline()
curlen=0
maxlen=0
for i in range (1,len(s)):
    if s[i-1]=="K" and s[i]=="O" and s[i+1]=="T":
        curlen+=1
        if curlen>maxlen:
            maxlen=curlen
print(maxlen)