N = int(input())
a = list(map(int, input().split()))
b = []
x = 0
for i in range(N):
    for j in range(i):
        if a[j] < a[i]:
            x += 1
    b.append(x)
    x = 0
for m in b:
    print(m, end=" ")
