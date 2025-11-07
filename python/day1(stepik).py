# minutes = 150
# def minhour():
#     hours = minutes // 60
#     xminutes = minutes % 60
#     print(f"{minutes} мин - это {hours} час {xminutes} минут.")
# minhour()


# x = 34
# print((x // 4) + 1)



# num = int(input())
# a = num % 10
# print(a)
# b = (num % 100) // 10
# c = num // 100
# print(c, b ,a, sep='\n')

## Formulas for fiding digit
# n // 10 ** (n - i)) % 10
# num % 10 ** (n + 1 - i) // (10 ** (n - i))

# num = 53
# ldigit = num % 10
# fdigit = num // 10
# print(fdigit, ldigit, sep='\n')

# num = 824
# digit1 = num % 10
# digit2 = (num % 100) // 10
# digit3 = num // 100
# print(digit3, digit2, digit1, sep='\n')

# hui = 123
# a = hui // 100
# b = (hui // 10) % 10
# c = hui % 10
# print('Сумма цифр = ', a + b + c, 'Произведение цифр = ', a * b * c)
###################################
#                                 #
#  d1 = (number // 10 ** 2) % 10  #
#  d2 = (number // 10 ** 1) % 10  #
#  d3 = (number // 10 ** 0) % 10  #
#                                 #
###################################

# num = 3192
# d1 = (num // 10 ** 0) % 10
# d2 = (num // 10 ** 1) % 10
# d3 = (num // 10 ** 2) % 10
# d4 = (num // 10 ** 3) % 10
# print(
#     'Цифра в позиции тысяч равна', d1,
#     'Цифра в позиции сотен равна', d2,
#     'Цифра в позиции десятков равна', d3,
#     'Цифра в позиции единиц равна', d4,
#     sep='\n'
# )

# n = 12345
# a = n // 10000
# b = (n // 1000) % 10
# c = (n // 100) % 10
# d = (n // 10) % 10
# e = n % 10
# print(a, b, c, d, e, sep='\n')
















# num = 123
# a = num // 100
# b = (num // 10) % 10
# c = num % 10
# print(
#     a * 100 + b * 10 + c * 1,
#     a * 100 + c * 10 + b * 1,
#     b * 100 + a * 10 + c * 1,
#     b * 100 + c * 10 + a * 1,
#     c * 100 + a * 10 + b * 1,
#     c * 100 + b * 10 + a * 1,
#     sep='\n'
# )


# a = 17 // (23 % 7)
# b = 34 % a * 5 - 29 % 4 * 3
# print(a * b)
# print(a)
# print(b)



# # print('ж' * 3 + 'ж' * 1)

# from math import sqrt, floor

# print(round(sqrt(260)))

# sqrt((x1 - x2)**2 + (y1 - y2)**2)

x = 5

y = 3

a = x + y ** 2

b = y ** 2 * x

c = x ** y - x

d = x ** (y - 2)

e = x / y + 3

f = x / y * 3

g = x // y

h = x % y

m = x == y or (x - 4) >= 1

k = x != 2 and y <= 5

print(a,b,c,d,round(e, 2),f,g,h,m,k, sep='\n')