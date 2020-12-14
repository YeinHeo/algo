from itertools import combinations

n, m = map(int, input().split())

a = []
for i in range(n):
    a.append((i+1))

b = list(combinations(a, m))
for i in range(len(b)):
    c = list(b[i])
    print(' '.join(map(str, c)))
