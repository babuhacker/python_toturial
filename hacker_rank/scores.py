# def greatest_smallest(num_list):
#     second_greatest = 0
#     greatest_number = 0
#     for number in num_list:
#         if number > greatest_number:
#             greatest_number = number
#
#         if number < greatest_number and number > second_greatest:
#             second_greatest = number
#     # print(second_greatest)
#
#
#
# a = [12, 23, 34, 45, 56, 67, 78, 89, 90]
# # a = input().split(",")
# print(greatest_smallest(a))


list1 = [10, 20, 4, 45, 99, 45, 8888]

list1.sort()

print("Second largest element is:", list1[-2])