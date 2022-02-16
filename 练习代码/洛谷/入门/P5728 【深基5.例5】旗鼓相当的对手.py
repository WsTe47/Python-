n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    a[i].append(a[i][0] + a[i][1] + a[i][2])
# 0 1 2为三科单科成绩  3位总分
x = 0
print(a)
for i in range(n):
    for j in range(i + 1, n):
        if -10 <= a[i][3] - a[j][3] <= 10 and -5 <= a[i][0] - a[j][0] <= 5 and -5 <= a[i][1] - a[j][1] <= 5 and -5 <= \
                a[i][2] - a[j][2] <= 5:
            x += 1
print(x)
# 0 1 2 3 4
# 0---1 2 3 4
# 1---2 3 4
# 2---3 4
# 3---4
# 4---4

# input
# 5
# 75 70 79
# 70 75 73
# 71 78 75
# 77 74 77
# 71 74 71
