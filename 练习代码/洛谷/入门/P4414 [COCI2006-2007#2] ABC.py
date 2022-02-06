a = [x for x in input().split()]
b = input()
a.sort()

if b[0] == 'A':
    print(a[0], end=' ')
elif b[0] == 'B':
    print(a[1], end=' ')
elif b[0] == 'C':
    print(a[2], end=' ')

if b[1] == 'A':
    print(a[0], end=' ')
elif b[1] == 'B':
    print(a[1], end=' ')
elif b[1] == 'C':
    print(a[2], end=' ')

if b[2] == 'A':
    print(a[0], end=' ')
elif b[2] == 'B':
    print(a[1], end=' ')
elif b[2] == 'C':
    print(a[2], end=' ')
