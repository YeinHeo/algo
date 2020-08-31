def find(a):
    if a == parent[a]:
        return a
    else:
        p = find(parent[a])
        parent[a] = p
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        number[a] += number[b]

n = int(input())
for _ in range(n):
    parent = dict()
    number = dict()

    m = int(input())
    for _ in range(m):
        a, b = input().split(' ')

        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1

        union(a,b)

        print(number[find(a)])


