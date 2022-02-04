# 要求输入学生数量，以及各个学生物理、数学、历史三科的成绩，如果总成绩小于 120，程序打印 “failed”，否则打印 “passed”。

Students_Number = int(input('学生数量'))
for i in range(Students_Number):
    Grades = []
    Grades.append(int(input('物理')))
    Grades.append(int(input('数学')))
    Grades.append(int(input('历史')))
    Grades_sum = 0
    for j in Grades:
        Grades_sum += j
    if Grades_sum<120:
        print('Student {} failed'.format(i+1))

    else:
        print('Student {} passed'.format(i+1))
    # print(Grades_sum)
