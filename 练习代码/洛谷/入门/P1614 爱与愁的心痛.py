a = list(map(int, input().split()))
n = a[0]
m = a[1]
k = []
for i in range(n):
    k += input().split()
x = 3333333  # x为最小值
y = 0  # y 为当前最小值
for i in range(0, n - m + 1):
    for j in range(m):
        y += int(k[i+j])
    if y < x:
        x = y
    y = 0
print(x)
