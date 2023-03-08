from random import randint

a = [randint(0, 1000) for x in range(10)]
print(a)

j1 = 0

for i in range(len(a)):
    mx_D = -1
    for j in range(i, len(a)):
        if a[j] % 10 >= mx_D:
            mx_D = a[j] % 10
            j1 = j

    a.insert(0, a.pop(j1))

print(a)