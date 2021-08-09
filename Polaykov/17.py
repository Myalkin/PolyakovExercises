count = 0

maxGood = 0

for n in range(1016, 7937 + 1):
    if (n % 11 == 0) and (n % 7 != 0) and \
            (n % 13 != 0) and (n % 17 != 0) and (n % 19 != 0):
        maxGood = n
        count += 1
print(count, maxGood)
