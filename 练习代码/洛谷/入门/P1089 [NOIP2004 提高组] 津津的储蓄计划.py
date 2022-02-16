a = []
x = 0  # x为手上的钱
y = 0  # y为妈妈的钱
for i in range(12):
    a.append(int(input()))
# a[i]为这个月的开支
for i in range(12):
    x += 300
    while (x - a[i]) >= 100:
        x -= 100
        y += 100
    if x - a[i] < 0:
        print('-{}'.format(i))
        x = 0
        break
    else:
        x -= a[i]
else:
    print(int(1.2 * y)+x)
# 50分 不知道哪里错了，两个自己测试点都OK
