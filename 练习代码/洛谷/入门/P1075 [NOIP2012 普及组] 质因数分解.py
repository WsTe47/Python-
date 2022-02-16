def isprime(x):
    if x == 1:
        return False
    if x == 2 or x == 3:
        return True
    else:
        for j in range(2, x):
            if x % j == 0:
                return False
            else:
                continue
        return True


n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        if isprime(i) or isprime(n // i):
            print(max(i, n // i))
            break
        else:
            continue
    else:
        continue
