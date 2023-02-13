'''
заполнить массив первыми числами Фибоначчи
'''

'''
через цикл

n = int(input())
fib = [0, 1]

for i in range(2, n + 1):
    fib.append(fib[i - 2] + fib[i - 1])

print(fib)
'''

'''
через рекурсию'''

n = int(input())
fib = []


def f(n):
    if n == 1 or n == 0:
        return 1

    else:
        return f(n - 1) + f(n - 2)


for i in range(n):
    fib.append(f(i + 1))

print(fib)
