a, b, c, d = map(int, input().split())
m = 60 * a + b
n = 60 * c + d
x = n - m
print(x // 60, x % 60)
