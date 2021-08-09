with open ("C:\\Users\\rmyal\\Desktop\\k7-53.txt", "r") as F:
    s = F.readline()
curlen=0
maxlen=0
for i in range (1,len(s)):
    if s[i] == "C":
        curlen+=1
        if curlen>maxlen:
            maxlen=curlen
    else:
        curlen=0
print(maxlen)