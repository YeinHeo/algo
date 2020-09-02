n = list(map(int, input().split()))

a = dict()
for i in n:
    if i in a.keys():
        a[i] += 1
    else:
        a[i] = 1

print(a)
