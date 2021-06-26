def prime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


print(prime(97))
print(prime(10))
print(prime(37))
print(prime(48))
print(prime(39))
print(prime(77))
print(prime(84))
print(prime(99))
print(prime(23))
