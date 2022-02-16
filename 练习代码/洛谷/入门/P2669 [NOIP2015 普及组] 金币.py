k = int(input())
S = 0
n = 1  # 该天给的金币
d = 1  # 天数
c = 1  # 层数
while d <= k:
    for i in range(c):
        if d > k:
            break
        S += n
        d += 1
    c += 1
    n += 1
print(S)
# 1
# 2+2
# 3+3+3
# 4+4+4+4
