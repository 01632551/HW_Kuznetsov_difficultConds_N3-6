a, b = int(input()), int(input())
while b != 0:
     m = min(a, b)
     a, b = m, max(a, b) - m

print(a)