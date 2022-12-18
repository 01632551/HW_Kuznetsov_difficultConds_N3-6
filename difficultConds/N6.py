m, d = int(input()), int(input())

# ds - кол-во дней только в полных месяцах до нового года
# s - кол-во месяцев, из которых стоит отнимать введённое (от условия)

# if n > 7: 3 по 31, 2 по 30 (всего 153)
# if n < 7: 5 по 30 и 7 по 31

if m > 12 or d > 31 or d == 0:
    print('ошибка')
else:
    if m > 7:
        ds = 0
        s = 12

        if m % 2 == 0:
            ds += 31 - d
        elif m % 2 == 1 and m <= 30:
            ds += 30 - d
        else: print('ошибка')

    else:
        ds = 153 # кол-во дней в 8-12 месяцах
        s = 7

        if m % 2 == 1:
            ds += 31 - d
        elif m % 2 == 0 and m <= 30:
            ds += 30 - d
        else: print('ошибка')


    for i in range(s - m):
        if (i + 1) % 2 == 1:
            ds += 31
        else:
            ds += 30
