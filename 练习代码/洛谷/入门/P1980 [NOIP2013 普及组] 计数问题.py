# a = list(input().split())
# n = a[0]
# x = a[1]
# s = 0
# for i in range(1, int(n)+1):
#     for j in range(len(str(i))):
#         if str(i)[j] == x:
#             s += 1
# print(s)

# 上面代码AC了四个点，超时了六个点。

# 1234:1234//1000==1  (1234-1000)//100==2 (1234-1000-200)//10=3 (1234-1000-200-30)//1=4
# a = list(map(int, input().split()))
# n = a[0]
# x = a[1]
# s = 0
# for i in range(1, n + 1):
#     for j in range(len(str(i))):
#         if i % 10 == x:
#             s += 1
#         i = (i - (i % 10)) / 10
#
# print(s)
# 上面代码依旧AC了四个点，超时了六个点。


a = input().split()
n = a[0]
x = a[1]
s = 0
for i in range(1, int(n) + 1):
    s += str(i).count(x)
print(s)
# 可算AC了。。。
