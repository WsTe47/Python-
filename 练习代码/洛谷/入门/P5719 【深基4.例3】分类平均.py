x=list(map(int,input().split()))
n = x[0]
k = x[1]
# n = int(input())
# k = int(input())
A = []
B = []
for i in range(1, n + 1):
    if i % k == 0:
        A.append(i)
    else:
        B.append(i)
print(f"{(sum(A) / len(A)):.1f}", end=" ")
print(f"{(sum(B) / len(B)):.1f}")
