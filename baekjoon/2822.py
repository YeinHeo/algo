a = dict()
for i in range(8):
    a[i] = int(input())

a = sorted(a.items(), key=lambda x : x[1], reverse=True)

total = 0
result = []
for i in range(5):
    total += a[i][1]
    result.append(a[i][0]+1)

print(total)
result = sorted(result)
for i in result:
    print(i, end=' ')
