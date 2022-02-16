n = int(input())
a = list(map(int, input().split()))
m = 1  # m为本次最大连号个数
M = 1  # m为最终最大连号个数
for i in range(1, n):
    if a[i] - a[i - 1] == 1:
        m += 1
    else:
        m = 1
    if m >= M:
        M = m
print(M)
