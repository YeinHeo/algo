n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = list(reversed(sorted(b)))

sum = 0
for i in range(n):
    sum += a[i]*b[i]

print(sum)
