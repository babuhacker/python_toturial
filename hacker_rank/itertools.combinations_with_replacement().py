from itertools import combinations_with_replacement

s, n = input().split(' ')
list = list(combinations_with_replacement(sorted(s), int(n)))

for i in list:
    print(''.join(i))
# input is HACK 2
