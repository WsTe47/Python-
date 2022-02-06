a = []
for i in range(7):
    a += [list(map(int, input().split()))]
c = [0, 0, 0, 0, 0, 0, 0]
for j in range(7):
    c[j] = a[j][0] + a[j][1]

d = [0, 0, 0, 0, 0, 0, 0]
for x in range(7):
    if c[x] <= 8:
        d[x] = 0
    else:
        d[x] = c[x]
if sum(d) == 0:
    print(0)
else:
    print(d.index(max(d)) + 1)
