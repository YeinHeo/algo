a = list(map(int, input().split()))

length = len(a)
result = 0
for i in range(length-1):
    if a[i] < a[i+1]:
        result += 1
    else:
        result -= 1

if result == (length-1):
    print('ascending')
elif result == -(length-1):
    print('descending')
else:
    print('mixed')
