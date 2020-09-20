n = int(input())

for i in range(n):
    m = list(input())

    if m[len(m)//2] == m[len(m)//2 -1]:
        print("Do-it")
    else:
        print("Do-it-Not")
