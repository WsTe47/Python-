import math

m, t, s = map(int, input().split())
if t==0:
    print(0)
else:
    print(max(0,(m - math.ceil(s / t))))
