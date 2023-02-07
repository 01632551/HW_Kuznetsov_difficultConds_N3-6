'''
Файл содержит последовательность целых чисел, по модулю не превышающих 10 000.
Назовём парой два идущих подряд элемента последовательности.

1.Определите количество таких пар, в которых запись меньшего по
значению элемента пары заканчивается цифрой 3.

2. Определить наибольшую из сумм таких пар.

3. Определить наименьший из элементов последовательности,
запись которых заканчивается цифрой 3.
'''

a = [int(x) for x in open('17 (2).txt')]
mn = min(x for x in a if x % 10 == 3)
ans = []

for i in range(len(a) - 1):
    if min(a[i], a[i+1]) % 10 == 3:
        ans.append(a[i] + a[i+1])

print(len(ans), max(ans), mn)
