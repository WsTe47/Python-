N = 10
sum = 0
a = 0
for i in range(N):
    i = float(input())
    sum += i
    a = sum / N

print('{} number\'s average is {}'.format(N,a))
