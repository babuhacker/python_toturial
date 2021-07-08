from collections import Counter

n = int(input())
l = list()

for _ in range(n):
    l.append(input())
# It will give total aucarences of input
x = Counter(l)
# len() is finding the length of the given value like x
print(len(x))
# * is a pack operator
print(*x.values())
