n = int(input())
a = list(input())

score = 0
bonus = 0
for i in range(len(a)):
    if a[i] == 'X':
        bonus = 0
    else:
        score += (i+1) + bonus
        bonus += 1

print(score)
