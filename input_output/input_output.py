# input and output

# var = input("message to the user")

# name = input("please enter your name: ")
# print(name)

# age = int(input("please enter your age: "))
# print(age+1)

scores = []

for i in range(5):
    currentscore = int(input("please enter the score " + str(i + 1) + ": "))
    scores.append(currentscore)
    print("the score you entered was:\n",currentscore)

print(scores)
