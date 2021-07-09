import numpy as np

n = int(input())
a = np.array([input().split() for i in range(n)], dtype=int)
b = np.array([input().split() for i in range(n)], dtype=int)
print(a.dot(b))
