from random import randint

a = [randint(1000, 2000) for x in range(10)]
print(a)
c = 0

for i in a:
    if ((i // 10) % 10) % 2 == 0:
        c += 1

print(c)