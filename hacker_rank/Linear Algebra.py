import numpy as np

n = int(input())
list1 = []
for i in range(n):
    l1 = list(map(float, input().split()))
    list1.append(l1)

arr = np.array(list1)

p = np.linalg.det(arr)
print(round(p, 2))
