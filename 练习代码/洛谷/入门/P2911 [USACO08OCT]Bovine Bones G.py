a = [0 for i in range(100)]
b = list(map(int, input().split()))
s1, s2, s3 = b[0], b[1], b[2]

for i in range(1,s1+1):
    for j in range(1,s2+1):
        for k in range(1,s3+1):
            a[i+j+k] += 1
print(a.index(max(a)))
