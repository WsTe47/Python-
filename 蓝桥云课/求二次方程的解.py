# ax^2 + bx +c =0
import math

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

d = b ** 2 - 4 * a * c
if d < 0:
    print('No Result')
elif d == 0:
    print('x1=x2={}'.format(-b / (2 * a)))
else:
    print('x1={},x2={}'.format(((-b + math.sqrt(d)) / 2 * a), (-b - math.sqrt(d)) / 2 * a))
