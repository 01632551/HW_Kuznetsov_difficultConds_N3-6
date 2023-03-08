from random import randint

a = [randint(0, 1000) for x in range(10)]
print(a)
f = []


def isPrime(n):
    """
    определяет, простое число или нет
    :param n: число, которое проверяет функция
    :return: True (если число простое), False (если число составное)
    """
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False

    else:
        return True


for i in a:
    if isPrime(i):
        f.append(i)

print(f)