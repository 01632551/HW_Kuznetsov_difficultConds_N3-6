def sumOfDevs(n):
    sumOfDevs = 0

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sumOfDevs += i

    return sumOfDevs

for j in range(1, 5000):
    s = sumOfDevs(j)
    for k in range(1, 10000):
        if s == k and sumOfDevs(k) == j \
                and k >= j:
            print(j, k)
