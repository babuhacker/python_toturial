import numpy

n = input().split()
arr = numpy.array(n, dtype=int)
print(arr.reshape(3, 3))
