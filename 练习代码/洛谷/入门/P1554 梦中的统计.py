# q = list(map(int, input().split()))
# m = q[0]
# n = q[1]
# x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(q[0], q[1] + 1):
#     i = str(i)
#     for j in range(len(i)):
#         z = i[j:j + 1:]
#         x[int(z)] += 1
# for i in x:
#     print(i, end=" ")
# 最后两个点 TLE 了。。前面8个点AC


q = list(map(int, input().split()))
a = ''
b = ''
for i in range(q[0], q[1] + 1):
    b = str(i)
    a += b
print(a.count('0'), a.count('1'), a.count('2'), a.count('3'), a.count('4'), a.count('5'), a.count('6'), a.count('7'),
      a.count('8'), a.count('9'))
# AC了
