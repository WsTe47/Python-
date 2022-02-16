n = int(input())
tn = list(map(int, input().split()))
mn = []
x = 0  # x为中奖彩票数
b = [0, 0, 0, 0, 0, 0, 0]  # b为几等奖数目
for i in range(n):
    m = list(map(int, input().split()))
    mn.append(m)
for i in range(n):
    y = 0  # y为中奖号码数
    for j in range(7):
        for k in range(7):
            if mn[i][j] == tn[k]:
                y += 1
    b[-y] += 1
for i in b:
    print(i, end=" ")
