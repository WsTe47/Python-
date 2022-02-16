n = int(input())
s = input()
for i in range(len(s)):
    if ord(s[i]) + n <= ord('z'):
        print(chr(ord(s[i]) + n), end="")
    else:
        print(chr(ord(s[i])+ord('a')-ord('z')-1 + n), end="")
