x = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
if x % a[0] == 0:
    n1 = x / a[0]
else:
    n1 = x // a[0] + 1
if x % b[0] == 0:
    n2 = x / b[0]
else:
    n2 = x // b[0] + 1
if x % c[0] == 0:
    n3 = x / c[0]
else:
    n3 = x // c[0] + 1

print(min(n1*a[1],n2*b[1],n3*c[1]))
