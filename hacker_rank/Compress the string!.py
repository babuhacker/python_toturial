from itertools import groupby

n = groupby(input())

print(*[(len(list(c)), int(k)) for k, c in n])
