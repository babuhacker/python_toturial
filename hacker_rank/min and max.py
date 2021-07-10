import numpy

n, m = list(map(int, (input().split())))
a = numpy.array([list(map(int, (input().split()))) for i in range(int(n))])
print(numpy.max(numpy.min(a, axis=1), axis=None))
