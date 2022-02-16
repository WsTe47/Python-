k = list(int(i) for i in input().split())
m = k[0]  # m为马路长度
n = k[1]  # n为区域数目

a = [1 for i in range(m+1)]
for i in range(n):
    z = list(int(i) for i in input().split())
    u = z[0]
    v = z[1]
    for j in range(u, v + 1):
        a[j] = 0
print(a.count(1))
