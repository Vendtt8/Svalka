t, n = map(int, input().split())
powers = set(map(int, input().split(',')))

all_paws = set(range(n))

result = sorted(all_paws - powers)

print(' '.join(map(str, result)))

