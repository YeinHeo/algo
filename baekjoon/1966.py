test = int(input())

for i in range(test):
    N, M = list(map(int, input().split(' ')))
    a = list(map(int, input().split(' ')))

    b = {}
    for i in range(len(a)):
        b[i] = a[i]

    isavailable = True
    count = 0
    while isavailable:
        for j in range(len(a)):
            temp = max(b.values())
            if temp == b[j]:
                b[j] = 0
                count += 1
            if b[M] == 0:
                print(count)
                isavailable = False
                break

