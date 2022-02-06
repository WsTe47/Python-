a = list(map(int, input().split()))
h = int(input())
s = 0
for i in a:
    if h + 30 >= i:
        s += 1
print(s)
