num = int(input())
a = num % 2 == 0
b = 4 < num <= 12
if a and b:
    u = 1
else:
    u = 0
if a or b:
    v = 1
    z = 0
else:
    v = 0
    z = 1
if a ^ b:
    w = 1
else:
    w = 0
print(u, v, w, z)
