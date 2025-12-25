### FIRST ###

"""
total = []

for _ in range(4):
    s = input()
    total += [s]

big, low = max(total), min(total)

print((ord(big[-1]) * ord(low[-1])) ** 2)
"""

### SECOND ###

"""
total = []
while True:
    s = input()
    if s == 'КОНЕЦ':
        break
    total += [s]
big, low = max(total), min(total)

print(
    f"Минимальная строка ⬇️: {low}",
    f"Максимальная строка ⬆️: {big}",
    sep='\n'
)
"""

### THIRD ###

"""
sa = input()
sb = input()

saa = ''
sbb = ''

for i in range(len(sa)):
    if sa[i].isalpha():
        saa += sa[i]

for i in range(len(sb)):
    if sb[i].isalpha():
        sbb += sb[i]

if saa.lower() == sbb.lower():
    print('YES')
else:
    print('NO')
"""

### FOURTH ###
"""
total = []
for _ in range(3):
    s = input()
    total += [s]
total.sort()
print(' '.join(total))"""

### FIFTH ###

"""
for _ in range(int(input())):
    s = input()
    if len(s) != 2 or not s[0].isdigit() or ord(s[1]) not in range(1040, 1051):
        print('NO')
    else:
        print('YES')
"""

### FINAL ###

total = []

for _ in range(int(input())):
    s = input()
    total += [s]
