from itertools import permutations

n, m = map(int, input().split())

a = []
for i in range(n):
    a.append((i+1))

b = list(permutations(a, m))
for i in range(len(b)):
    c = list(b[i])
    for j in range(m):
        if (j+1 == m):
            print(c[j])
        else:
            print(c[j], end=' ')
