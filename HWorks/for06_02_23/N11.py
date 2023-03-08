from random import randint

a = [randint(0, 1000) for x in range(10)]
print(a)


def sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10

    return s


j1 = 0
for i in range(len(a)):
    mn = 30
    for j in range(i, len(a)):
        s = sum(a[j])
        if s < mn:
            mn = s
            j1 = j

    a.insert(0, a.pop(j1))

print(a)
