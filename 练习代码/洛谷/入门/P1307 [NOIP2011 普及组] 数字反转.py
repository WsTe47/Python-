n = input()
# 这是一个取巧的方法，本是想判断 while int(n) % 10 == 0 ，结果附加测试点 TLE 了。
# 由于题中数据−1,000,000,000≤N≤1,000,000,000，所以取巧用range
for i in range(11):
    if int(n) % 10 == 0:
        n = int(n) // 10
        n = str(n)
if int(n) >= 0:
    print(n[::-1])
else:
    print('-{}'.format(n[:0:-1]))
