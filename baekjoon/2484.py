num = int(input())

result = []
for i in range(num):

    n = list(map(int, input().split()))

    a = dict()
    for i in n:
        if i in a.keys():
            a[i] += 1
        else:
            a[i] = 1

    b = a.items()
    m = sorted(b, key=lambda x:x[1], reverse=True)

    count = m[0][1]

    if count == 4:
        ans = 50000 + m[0][0]*5000
    elif count == 3:
        ans = 10000 + m[0][0]*1000
    elif count == 2:
        if m[1][1] == 2:
            ans = 2000 + m[0][0]*500 + m[1][0]*500
        else:
            ans = 1000 + m[0][0]*100
    else:
        ans = max(n)*100

    result.append(ans)

print(max(result))
