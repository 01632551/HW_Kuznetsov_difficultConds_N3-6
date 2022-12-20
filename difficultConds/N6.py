m, d = int(input()), int(input())
ds = 0
# ds - кол-во дней только в полных месяцах с нового года

# if n > 7: 3 по 31, 2 по 30 (всего 153)
# if n < 7: 4 по 30 и 7 по 31 и 1 по 28

if m > 12 or d > 31 or d == 0 \
        or (m in(4, 6, 9, 11) and d > 30) \
        or (m == 2 and d > 28):
    print('ошибка')

else:
    while m != 1:
        m -= 1

        if m in(4, 6, 9, 11):
            ds += 30

        elif m == 2:
            ds += 28

        else: ds += 31

    ds += d

    print(365 - ds)