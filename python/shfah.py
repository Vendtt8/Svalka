s = 'А232МК_23'
flag = 0
exa = 'АВЕКМНОРСТУХ'


if s[0] in exa:
    flag += 1


if s[1:4].isdigit():
    flag += 1


temp = 0
for i in range(4, 6):
    if s[i] in exa:
        temp += 1
if temp == 2:
    flag += 1


if s[6] == '_':
    if len(s) == 9:
        if s[7:].isdigit():
            flag += 1
    elif len(s) == 10:
        if s[7:].isdigit():
            flag += 1


if flag == 4:
    print('YES')
else:
    print('NO')


### My solution ###


