s = input()
a = dict()
for i in s:
    if i in a.keys():
        a[i] += 1
    else:
        a[i] = 1

num = 0
for j in a.values():
    if (j%2) != 0:
       num += 1

temp1 = ''
temp2 = ''
for i in sorted(a.items()):
    if i[1]%2 == 1:
        temp2 = i[0]
        if i[1] > 1:
            t = i[0]*(i[1]//2)
            temp1 = temp1 + t
    else:
        t = i[0]*(i[1]//2)
        temp1 = temp1 + t

result = temp1 + temp2 + ''.join(reversed(temp1))

if num > 1:
    print("I'm Sorry Hansoo")
else:
    print(result)
