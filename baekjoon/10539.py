n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(len(a)):
    b.append(a[i]*(i+1))

c = []
c.append(b[0])
for i in range(1, len(b)):
    c.append(b[i] - b[i-1])

for i in c:
    print(i, end=' ')
