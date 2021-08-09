for n in range(800001, 1000000+1):
    divs = []
    for d in range(2, n):
        divs = divs + [d, n//d]
        Smax = max(divs)
        Smin = min(divs)
        k = (Smin + Smax)
        if n % d == 0 and k % 138 == 0:
            print(n, k)