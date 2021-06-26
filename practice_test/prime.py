'''
1.find greatest number  in a list [4,5,6,7,8,9,32,65]
2. find smallest
3. find second greatest
4. find second smallest

5. write a function to check if a number is prime or not 97-true 10-false

6. tell if a numbet is odd or even

7. write a program to generate fibonacci series till a given number.

'''


# we defined a function named greatest which takes one list as argument
def greatest(input_list):
    # we have defined greatest_number which is assign to 0
    greatest_number = 0
    # we are looping through input list
    for input_l in input_list:
        # checking if current number is greater than current greatest
        if input_l > greatest_number:
            # assigning current number as greatest now
            greatest_number = input_l

    # after the loop is complete we have found the greatest number and we return it
    return greatest_number


# we defined a function named smallestnumber which takes one list as argument
def smallestnumber(numbers):
    # here we defined smallest_num which is assign to 0
    smallest_num = numbers[0]
    # we are looping through numbers
    for num in numbers:
        # we are checking if the number is smaller than the previous number
        if num < smallest_num:
            smallest_num = num
    # the function of smallestnumber is returning
    return smallest_num


# we defined a function named second which takes one list as argument
def second(numbers):
    # here we defined second_num which is assign to 0
    second_num = numbers[0]
    # we are looping through numbers
    for num in numbers:
        # this function is checking  if num is greater than second_num
        if num > - second_num:
            second_num = num
    # the function of num is returning
    return second_num


# we defined a function named secondsmall which takes one list as argument
def secondsmall(numbers):
    # we have defined smallest which is assign to 0
    smallest = numbers[0]
    # we have defined second_smallest which is assign to 1
    second_smallest = numbers[1]
    # we are looping through numbers
    for num in numbers:
        # this function is checkig if num is smaller than smallest
        if num < smallest:
            second_smallest = smallest
            smallest = num

    # the function of num is returning
    return second_smallest


# we have defined greatest_smallest which takes one list as argument
def greatest_smallest(num_list):
    # we have defined greatest_number which is assign to 0
    greatest_number = 0
    # we have defined smallest_number which is assign to first element in the list
    smallest_number = num_list[0]
    # we have defined second_smallest which is assign to first element in the list
    second_smallest = num_list[0]
    # we have defined second_greatest which is assign to 0
    second_greatest = 0
    # we are looping through num_list
    for number in num_list:
        # print(input_l)
        # cheking if the number is greater than the current gretest number
        if number > greatest_number:
            # greateat_number is equal to number
            greatest_number = number
        # cheking if the number is smaller than the current greater number and number greater than the second greatest
        if number < greatest_number and number > second_greatest:
            # second_greatest is equal to number
            second_greatest = number
        # cheking if the number is smaller than the current smaller number
        if number < smallest_number:
            # second_smallesst is equal to smallest_number
            second_smallest = smallest_number
            # smallest_number is equal to number
            smallest_number = number
    # we are printing greatest_number
    print("greatest number =", greatest_number)
    # we are printing second_greatest
    print("second greatest number", second_greatest)
    # we are printing smallest_number
    print("smallest number =", smallest_number)
    # we are printing second_smallest
    print("second smallest number =", second_smallest)


a = [6, 5, 3, 9, 7, 8, 105, 32, 65]
# we are printing greatest_smalleat(a)
print(greatest_smallest(a))
# print(smallest(a))


# a = [6, 5, 3, 7, 8, 105, 9, 32, 65]
# print("greatest numer is", greatest(a))
# print("smallest number is", smallestnumber(a))
# print("second greatest numder is",second(a))
# print("second smalest number is",secondsmall(a))
