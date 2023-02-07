n = int(input())
print('1')

for i in range(2, int(n/2) + 1):
    if n % i == 0:
        print(i)

