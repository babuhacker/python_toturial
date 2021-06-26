# import is used to import any code that is already written in python
import logging
import math

logging.basicConfig(level=logging.DEBUG)


# def is a function named getfactors which stored number
def getfactors(number):
    # we have defined factors
    factors = []
    # a for loop is running in the range of 1 to the number and including the number
    for num in range(1, int(math.sqrt(number)) + 1):
        # an if statementis checking if the number modules to num is equal to zero
        if number % num == 0:
            # factor is appending num
            factors.append(num)
            factors.append(number // num)
    # we are returnin through factors
    return factors


logging.debug(getfactors(17))


# def is a function named isprime which stored number
def isprime(number):
    # we are returning through getfactors(number) which is equal to 2
    return len(getfactors(number)) == 2


# we have defined allfactors
allfactors = getfactors(600851475143)

# finding the highest number
# largestprimefactor is assign to zero
largestprimefactor = 0
# a for loop is running in allfactors
for factor in allfactors:
    # we are checking if isprime(factor) and factor is greater than largestprimefactor
    if isprime(factor) and factor > largestprimefactor:
        # largestprimefactor is assign to factor
        largestprimefactor = factor
# we are printing largestprimefactor
print(largestprimefactor)
