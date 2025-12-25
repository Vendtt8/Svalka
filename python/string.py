s = input()
sf = s

for i in range(1, len(s) + 1):
    if s[i - 1:i + 1] == '[u':
        temp = int(s[i + 2:i + 6])
        sf = sf.replace(s[i - 1:i + 7], chr(temp))
print(sf)
