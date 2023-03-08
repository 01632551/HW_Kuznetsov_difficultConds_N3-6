# № 4
from random import randint
a = [randint(20, 100) for x in range(10)]

c1 = 0
c2 = 0

for i in range(len(a)):
    if a[i] % 2 == 0:
        c1 += 1

    else: c2 += 1

print(c1, c2)