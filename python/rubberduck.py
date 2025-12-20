# while True:
#     s = input()
#     if s == 'stop':
#         break
#     print(ord(s))





# maxw = 0
# maxs = ''
# temp = []

# for i in range(4):
#     s = input()
#     w = 0
#     for ch in s:
#         w += ord(ch)
#     temp += [w, s]
#     if w > maxw:
#         maxw = w
#         maxs = s

# print(maxs)



s = input()
s1 = s
sum1 = 0
sum2 = 0

for char in s:
    sum1 += ord(char)
sal1 = sum1 * 3

eng = 'eyopaxcETOPAHXCBM'
rus = 'еуорахсЕТОРАНХСВМ'

for i in range(len(s1)):
    for j in range(len(eng)):
        if s1[i] == eng[j]:
            s1 = s1[:i] + rus[j] + s1[i+1:]

for ch in s1:
    sum2 += ord(ch)
sal2 = sum2 * 3



print(
    f"Старая стоимость: {sal1}🐝",
    f"Новая стоимость: {sal2}🐝",
    sep='\n'
)
