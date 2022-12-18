n = int(input())

if n > 12:
    print('Ошибка!')
else:
    for i in range(4):
        if n // 3 == i + 1:
            print(i)
            break
