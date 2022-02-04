# 1、使用 open 打开文件 String.txt 并读取其中的字符串
# 2、提取字符串中的所有数字，并组合成一个新的字符串，然后打印输出

f1 = open('String.txt')
s1 = f1.read()
s2 = ''
for x in s1:
    if x.isdigit():
        s2 += x
print(s2)
f1.close()
