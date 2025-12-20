sums = {}
for a in range(1, int(100000**(1/3)) + 1):
    for b in range(a, int(100000**(1/3)) + 1):
        s = a**3 + b**3
        if s > 100000:
            break
        sums.setdefault(s, []).append((a, b))
print({s: pairs for s, pairs in sums.items() if len(pairs) > 1})

