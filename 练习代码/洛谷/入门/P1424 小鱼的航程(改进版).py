x, n = map(int, input().split())
s = 0
a = [250, 250, 250, 250, 250, 0, 0, 250, 250, 250, 250, 250, 0, 0]
while n>0:
    if n < 7:
        s += a[x-1]
        x += 1
        n -= 1
    else:
        n -= 7
        s += 1250
print(s)
