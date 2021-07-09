# method 1



# from itertools import product
#
# K, M = list(map(int, input().split()))
# N = []
# for i in range(K):
#     N.append(list(map(int, input().split()))[1:])
# result = map(lambda x: sum(i ** 2 for i in x) % M, product(*N))
# print(max(result))

# method 2

from itertools import product

KM = list(map(int, input().split()))
K, M = KM[0], KM[1]
N = []
for i in range(K):
    N.append(list(map(int, input().split()))[1:])

N = list(product(*N))
ans = []
for i in N:
    s = 0
    for j in i:
        s += j ** 2
    ans.append(s % M)
print(max(ans))
