m, n = map(float, input().split())
BMI = m / n ** 2
if BMI<18.5:
    print('Underweight')
elif BMI<24:
    print('Normal')
else:
    print(format(BMI,'6g'))
    print('Overweight')
#    print(format(BMI,'6g'))  保留六位有效数字

