N = int(input())  # n为总需要的钱
x = 0
k = 1
p = [0]  # x
q = [0]  # k
for x in range(1, 101):
    for k in range(1, 1002):
        if 52 * (7 * x + (1 + 2 + 3 + 4 + 5 + 6) * k) == N:  # 为募集的钱
            p.append(x)
            q.append(k)
print(p[-1])
print(q[-1])
