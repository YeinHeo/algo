n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

b = sorted(a, key=lambda x: x[1])
c = sorted(b, key=lambda x: x[0])

print(c)
