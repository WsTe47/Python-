n = int(input())
x = 1
for j in range(n):
    for i in range(n):
        if x <= 9:
            print("0{}".format(x), end="")
        else:
            print(x, end="")
        x += 1
    print()
print()
y = 1
for j in range(1, n + 1):
    print(2 * (n - j) * ' ', end="")
    for i in range(1, j + 1):
        if y <= 9:
            print("0{}".format(y), end="")
        else:
            print(y, end="")
        y += 1
    print()
