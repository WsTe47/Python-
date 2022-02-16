from math import sqrt

n = int(input())
Fn = (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) / sqrt(5)
print(f"{Fn:.2f}")
