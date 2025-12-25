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
