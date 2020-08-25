import itertools

a, value = list(map(int, input().split()))
b = list(map(int, input().split()))

c = list(itertools.combinations(b, 3))

result = 0
for i in range(len(c)):
    if result == value:
        break
    if sum(c[i]) <= value:
        result = max(result, sum(c[i]))
print(result)
