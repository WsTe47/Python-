# 计算两个矩阵的 Hadamard 乘积。
# 要求输入矩阵的行/列数（在这里假设我们使用的是 n × n 的矩阵）
# 哈达玛积(Hadamard product)是矩阵的一类运算，若A=(aij)和B=(bij)是两个同阶矩阵，若cij=aij×bij,则称矩阵C=(cij)为A和B的哈达玛积，或称基本积
n = int(input("Enter the value of n: "))
print("Enter values for the Matrix A")

a = []

for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter values for the Matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])

c = []
for i in range(n):
    c.append([int(a[i][j] * b[i][j]) for j in range(n)])

for m in c:
    for n in m:
        print(str(n), end=' ')
    print()
