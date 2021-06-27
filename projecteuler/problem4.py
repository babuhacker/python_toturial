# first you have to creat a function clled main
def main():
    # and then you have to creat a list
    list_of_palindromes = []
    # a for loop is running in the range from 100 to 1000
    for x in range(100, 1000):
        # a for loop is running in the range from 100 to 1000
        for y in range(100, 1000):
            # we are checking if string x*y is equal to string x*y
            if str(x * y) == str(x * y)[::-1]:
                # we are appending list_of_palindormes into integer x*y
                list_of_palindromes.append(int(x * y))
    # we are printing the maximum number in list_of_palindromes
    print(max(list_of_palindromes))


# we are calling main function
main()
