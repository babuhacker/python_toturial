import numpy as np

l = list(map(float, input().split()))
x = int(input())
arr = np.array(l)
print(np.polyval(arr, x))
