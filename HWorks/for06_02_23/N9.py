from random import randint

a = [randint(0, 1000) for x in range(10)]
print(a)
n = 3 # кол-во элементов для неполной сортировки

for i in range(n):
    mn = 1001
    for j in range(i, len(a)):
        if a[j] < mn:
            mn = a[j]
            j1 = j

    a.insert(i, a.pop(j1))

print(a)
