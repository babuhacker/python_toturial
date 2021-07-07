from collections import Counter

n = int(input())

stock = list(map(int, input().split(' ')))

# print(stock)
dic = Counter(stock)

x = int(input())

p = 0
for i in range(x):
    size, prise = map(int, input().split(' '))
    if dic[size]:
        dic[size] = -1
        p = p + prise
print(p)
