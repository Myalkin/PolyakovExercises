for n in range (244143, 1367821+1):
    divs=[]
    for d in range(1,n+1):
        if n % d == 0:
            divs.append(d)
    if len(divs)==5:
        print (divs)