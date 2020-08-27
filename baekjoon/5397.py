n = int(input())

for i in range(n):
    data = input()
    a = []
    b = []

    for j in data:
        if j == '-':
            if a:
                a.pop()
        elif j == '<':
            if a:
                b.append(a.pop())
        elif j == '>':
            if b:
                a.append(b.pop())
        else:
            a.append(j)

    a.extend(reversed(b))
    print(''.join(a))
