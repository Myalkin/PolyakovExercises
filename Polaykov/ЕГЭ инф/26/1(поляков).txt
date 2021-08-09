with open("C:\\Users\\rmyal\\Desktop\\26-1.txt", "r") as F:
    s = F.readlines()
S, _ = map(int, s[0].split())
del s[0]
s = sorted(list(map(int, s)))
total=0
for i, val in enumerate(s):
    if total + val > S: break
    total += val
print(i)
delta = S - total
candidates = [x for x in s
              if x-s[i-1]<=delta]
print(max(candidates))
