k = int(input())
S = 0
n = 0
while S <= k:
    n += 1
    S += 1 / n
print(int(n))
