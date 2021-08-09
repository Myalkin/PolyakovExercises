count = 0
maximal = 0
for n in range(1033, 7737 + 1):
    if n % 5 == 0 and n % 11 != 0 and n % 17 != 0 and n % 19 != 0 and n % 23 != 0:
        count += 1
        maximal = n

print(count, maximal)
