a = list(map(int, input()))

a.sort(reverse=True)
b = ''.join(map(str, a))
print(b)

