# N6
from random import randint

a = [randint(0, 100) for x in range(10)]
print(a)
s1, c1, s2, c2 = 0, 0, 0, 0

for i in a:
    if i < 50:
        s1 += i
        c1 += 1

    else:
        s2 += i
        c2 += 1

print('среднее значение для элементов <50:', s1//c1,
      '\nсреднее значение для элементов >= 50:', s2//c2)