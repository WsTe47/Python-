import numpy as np

z = list(map(int, input().split()))
w = z[0]
x = z[1]
h = z[2]
a = np.ones((w, x, h), dtype=np.int16)

q = int(input())
for m in range(q):
    i1 = list(map(int, input().split()))
    for i in range(i1[0]-1, i1[3] ):
        for j in range(i1[1]-1, i1[4] ):
            for k in range(i1[2]-1, i1[5] ):
                a[i][j][k] = 0
print(np.count_nonzero(a))


# -----------------------------------------------------------------
# # 创建三维数组
# z = list(map(int, input().split()))
# w = z[0]
# x = z[1]
# h = z[2]
# m = []
# y = []
# a = []
# for k in range(h):
#     m.append(1)
# for j in range(x):
#     y.append(m)
# for i in range(w):
#     a.append(y)
# # q = int(input())
# # i1 = list(map(int, input().split()))
# # for i in range(i1[0], i1[3]+1):
# #     for j in range(i1[1], i1[4]+1):
# #         for k in range(i1[2], i1[5]+1):
# #             a[i][j][k] = 0
#
# # 输出现有的总的体积
#
# print(a[1])
# print(a[1][1])
# print(a[1][1][1])
# a[1][1][1]=0
# s = 0
# for i in range(w):
#     for j in range(x):
#         s += a[i][j].count(1)
# print(a)
# print(s)
#
