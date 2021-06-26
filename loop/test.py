def prime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return n
    return "prime"
    # check for prime number in this function
    # return n or return "prime"


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # elif i % 3 == 0:
    #     print("Fizz")
    #
    # elif i % 5 == 0:
    #     print("Buzz")

    else:
        print(prime(i))
