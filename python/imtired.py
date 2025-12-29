def del_uneven_i(num: int) -> None:
    ls = list()

    for i in range(num):
        ls.append(int(input()))

    del ls[1::2]

    return print(ls)


def k_string(num: int) -> None:
    ls = list()
    res = ""

    for i in range(num):
        ls.append(input())

    k = int(input())

    for i in ls:
        if k > len(i):
            continue
        res += i[k - 1]

    return print(res)


def allsym(num: int):
    ls = list()
    for i in range(num):
        ls.extend(input())
    return ls


def func1(num: int) -> None:
    ls = []

    for i in range(num):
        ls.append(int(input()))

    for i in ls:
        print(i)

    print()

    for x in ls:
        print(x**2 + 2 * x + 1)


def remove_outliers(num: int) -> None:
    ls = []

    for i in range(num):
        ls.append(int(input()))

    ls.remove(max(ls))
    ls.remove(min(ls))

    return print(*ls, sep="\n")


def no_dublicats(num: int) -> None:
    ls = []
    res = []

    for i in range(num):
        ls.append(input())

    for i in ls:
        if i not in res:
            res.append(i)
    return print("\n", *res, sep="\n")


def google(num: int) -> None:
    lines = []
    for _ in range(num):
        line = input()
        lines.append(line)

    search_string = input()

    for line in lines:
        if search_string.lower() in line.lower():
            print(line)


def negnullpos(n):
    ls = []
    res = []
    for i in range(n):
        ls.append(int(input()))

    for i in ls:
        if i < 0:
            res.append(i)

    for i in ls:
        if i == 0:
            res.append(i)

    for i in ls:
        if i > 0:
            res.append(i)

    return print(res, sep="\n")


def pairs(str1: str):
    ls = str1.split()
    count = 0

    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            if ls[i] == ls[j]:
                count += 1

    return count


def change_min_max(str1: str):
    ls = list(map(int, str1.split()))

    maxind, max1 = ls.index(max(ls)), max(ls)
    minind, min1 = ls.index(min(ls)), min(ls)

    ls[maxind] = min1
    ls[minind] = max1
    return print(*ls, sep=" ")


def cleancomments(num: str):
    num = num.replace("#", "")
    sad = list()

    for i in range(int(num)):
        s = input()
        if "#" in s:
            ind = s.index("#")
            s = s[:ind]
        sad.append(s.rstrip())

    return print(*sad, sep="\n")


def playlist(num: int):
    ls = [input() for _ in range(num)]
    ls.sort()
    return print(*ls, sep="\n")


def dunno():
    return print(
        *[
            c**2
            for c in [k for k in list(map(int, input().split())) if k % 2 == 0]
            if (c**2) % 10 != 4
        ]
    )


def print_perm_time_call(msc_time):  # 07:30
    msc_time = list(map(int, msc_time.split(":")))  # [7, 30]
    prm_time = msc_time
    if msc_time[0] < 8:
        prm_time[0] = prm_time[0] + 2  # [9, 30]
        print(f"Созвон будет в {'0' + str(prm_time[0])}:{prm_time[1]}")
    else:
        print(f"Созвон будет в {prm_time[0]}:{prm_time[1]}")


def print_symbol_counts(s):
    ls = []
    ls.extend(sorted(s.lower()))
    ls_sym = []
    for i in ls:
        if i not in ls_sym:
            ls_sym.append(i)
    for i in ls_sym:
        print(f"{i}: {ls.count(i)}")


def convert_to_miles(km):
    return km * 0.6214


def code_format(s):
    return f"<code>{s}</code>"


def get_days(month: int):
    return {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }[month]


def round_to_int(num: float):
    if num - int(num) < 0.5:
        return int(num)
    else:
        return int(num) + 1


def get_factors(num: int):
    return [i for i in range(1, num + 1) if num % i == 0]


def get_factors_count(num: int):
    return len([i for i in range(1, num + 1) if num % i == 0])


def get_unique(num: list):
    result = []
    for i in num:
        if i not in result:
            result.append(i)

    return result


def get_last_index(data: list, value: int):
    if value in data:
        return len(data) - data[::-1].index(value)
    else:
        return "ERROR!"


def find_all(target: str, symbol: str):
    return [i for i in range(len(target)) if target[i] == symbol]


print(find_all("hello world", "l"))
