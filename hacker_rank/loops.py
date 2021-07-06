# # for i in range(5):
# #     print(i * i)
#
#
# # for i in range(1,4):
# #     print(i)
#
# num = int(input("Please enter number: "))
# for i in range(1, num+1):
#      print(i,end='')
#
#
# n = int(input())
# d = int(input())
# c = int(input())
# b = int(input())
# a = int(input())
#
# scores = [n, d, c, b, a]
# print(scores[-2])



data = int(input())

arr = map(int, input().split())


def find_second_maximum(list):
    first_max = max(list[0], list[1])
    second_max = min(list[0, list[1]])

    for i in range(2, len(list)):
        if list[i] > first_max:
            second_max = first_max
            first_max = list[i]

        elif list[i] > second_max:
            second_max = list[i]

    return second_max


print(find_second_maximum(arr))



