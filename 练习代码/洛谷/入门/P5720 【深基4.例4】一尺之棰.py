from math import floor
n = int(input())
d =1
while n > 1:
    n = floor(n/ 2)
    d += 1
print(d)
