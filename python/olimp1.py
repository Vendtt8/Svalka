n = int(input())
x = int(input())

period = 3 * x
pairs = n // period
days = pairs * 2
sold = pairs * period
rem = n - sold

if rem > 0:
    if rem <= x:
        days += 1
    else:
        days += 2

print(days)
