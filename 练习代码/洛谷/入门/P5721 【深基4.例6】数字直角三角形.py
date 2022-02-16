n = int(input())
x = 1
for i in range(n):
    for j in range(n - i):
        if x <= 9:
            print('0{}'.format(x), end="")
        else:
            print(x, end="")
        x += 1
    print()
