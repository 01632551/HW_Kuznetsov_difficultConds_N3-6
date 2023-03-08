from random import randint

a = [randint(0, 1000) for x in range(10)]
print(a)
n = int(input())
f = []

for i in a:
    s = 0
    n1 = i
    while n1 > 0:
        s += n1 % 10
        n1 //= 10

    if s == n:
        f.append(i)
        
print(f)