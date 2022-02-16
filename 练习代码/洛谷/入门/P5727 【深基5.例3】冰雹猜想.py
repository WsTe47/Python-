def isodd(x):
    if x % 2 == 1:
        return True
    else:
        return False


def act():
    global n
    if isodd(n):
        n = n * 3 + 1
    else:
        n = n / 2


n = int(input())
a = [n]
while n != 1:
    act()
    a.append(int(n))
a.reverse()
for i in a:
    print(i, end=" ")
