# №1
num = int(input())
f = [0] * 10

while num > 0:
    f[num%10] += 1
    num //= 10

f.sort()

if f[9] == 3 and f[8] < 2:
    print('число подходит')

else: print('число не подходит')