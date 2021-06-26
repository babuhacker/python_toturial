# Breaking And Continiting

participants = ["Mark", "Jeff", "Jill", "Jack", "Narin"]

position = 1
#

# Breaking

# for name in Participants:
#     if name == "Jill":
#         print("About to break")
#         break
#     print("About to increment")
#     position = position + 1
#
# print(position)
#
# for currentIndex in range (len(participants)):
#     print(currentIndex)
#     if participants[currentIndex] == "Jack":
#         print("Have Breaked")
#         break
#     print("Not Breaked")
#
# print(currentIndex + 1)

# continuting

for number in range(10):
    if number % 3 == 0:
        print(number)
        print("Divisible By 3")
        continue
    print(number)
    print("Not Divisible By 3")
