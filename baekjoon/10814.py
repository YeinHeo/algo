n = int(input())

a = []
for i in range(n):
    x = list(input().split())
    a.append(x)

b = dict()
c = dict()

for i in range(n):
    b[i] = int(a[i][0])
    c[i] = a[i][1]

d = dict(sorted(b.items(), key=lambda item: item[1]))

for key, value in d.items():
    print(str(value) + ' ' + c[key])
