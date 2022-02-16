a = list(map(int, input().split()))
a.remove(0)
a.reverse()
for m in a:
    print(m, end=" ")
