year, month = map(int, input().split())


def isleap():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print('31')
elif month == 4 or month == 6 or month == 9 or month == 11:
    print('30')
elif month == 2:
    if isleap():
        print('29')
    else:
        print('28')
