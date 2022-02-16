m = float(input())
x = 2  # 此步距离
S = 0  # 总距离
n = 0  # 步数
while S < m:
    S += x
    x *= 0.98
    n += 1

print(n)
