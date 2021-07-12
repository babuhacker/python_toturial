import numpy

numpy.set_printoptions(sign=" ")

arr = numpy.array(input().split(), dtype=float)
f = numpy.floor(arr)
c = numpy.ceil(arr)
r = numpy.rint(arr)
print(f)
print(c)
print(r)
