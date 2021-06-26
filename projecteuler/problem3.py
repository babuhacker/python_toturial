import logging
import math

logging.basicConfig(level=logging.DEBUG)


def getfactors(number):
    factors = []
    for num in range(1, int(math.sqrt(number)) + 1):
        if number % num == 0:
            factors.append(num)
    return factors


logging.debug(getfactors(17))


def isprime(number):
    return len(getfactors(number)) == 2


allfactors = getfactors(600851475143)

# finding the highest number

largestprimefactor = 0
for factor in allfactors:
    if isprime(factor) and factor > largestprimefactor:
        largestprimefactor = factor

print(largestprimefactor)
