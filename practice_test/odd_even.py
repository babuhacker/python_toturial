def is_odd_or_even(number):
    if number % 2 == 0:
        return "even"
    return "odd"


for i in range(1, 101):
    print(i, is_odd_or_even(i))
