n, m = map(int, input().split())

a = dict()
for _ in range(n):
    team = input()
    member = int(input())
    name = []
    for _ in range(member):
        name.append(input())
    a[team] = name

for _ in range(m):
    who = input()
    game = int(input())

    if game == 1:
        for k, v in a.items():
            if who in v:
                print(k)

    else:
        result = sorted(a[who])
        for i in result:
            print(i)
