n = int(input())

if n > 12:
    print('Ошибка')
else:
    if n > 7:
        if n % 2 == 0:
            print('31')
        else: print('30')
    else:
        if n % 2 == 0:
            print('30')
        else: print('31')