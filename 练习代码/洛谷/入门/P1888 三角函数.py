def Max_Common_Divisor(a, b):
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            mcd = i
    return mcd


x = list(map(int, input().split()))
x.sort()
a=x[0] // Max_Common_Divisor(x[0], x[2])
b=x[2] // Max_Common_Divisor(x[0], x[2])
print('{}/{}'.format(int(a), int(b)))
# print(Max_Common_Divisor(x[0],x[2]))
