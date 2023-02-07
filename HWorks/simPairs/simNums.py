a= [int(x) for x in open ('17 (1).txt')]
ans = []
avMaxMin = (max(a) + min(a)) / 2

for i in range(len(a)//2):
    if (a[i] < avMaxMin and a[-(i+1)] > avMaxMin) or (a[i] > avMaxMin and a[-(i+1)] < avMaxMin):
        ans.append(a[i] + a[-(i+1)])

print(len(ans), max(ans))