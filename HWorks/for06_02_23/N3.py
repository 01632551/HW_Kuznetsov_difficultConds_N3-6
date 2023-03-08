# N3
num, num1 = int(input()), int(input())

while num1 != 0:
    m = min(num, num1)
    num, num1 = m, max(num, num1) % m

print(num)