from math import sqrt

a, b, c = map(float, input().split())
p = (a + b + c) / 2
S = sqrt(p * (p - a) * (p - b) * (p - c))
print(f"{S:.1f}")
