a = input()
b = list(a)
c = [0] * len(b)

available = False
for i in range(len(b)):
    if b[i] == '<':
        available = True

    if available == True:
        c[i] = 1

    if b[i] == '>':
        available = False

temp = []
for i in range(len(c)):
    if c[i] == 1:
        if len(temp) != 0:
            print(''.join(list(reversed(temp))), end='')
            temp = []
        print(b[i], end='')
    else:
        if b[i] == ' ':
            if len(temp) != 0:
                print(''.join(list(reversed(temp))), end=' ')
                temp = []
        else:
            temp.append(b[i])

if len(temp) != 0:
    print(''.join(list(reversed(temp))), end='')
