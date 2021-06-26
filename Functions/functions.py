'''A function is a block of organized, reusable code that is used to perform a single, related action.
  As you already know, Python gives you many built-in functions like print(), etc.
  but you can also create your own functions.'''


# def FunctionName(Input):
#     Action
#     return Output


def addone(Number):
    Output = Number + 1
    return Output


Var = 0
print(Var)
Var2 = addone(Var)
Var3 = addone(Var2)
Var4 = addone(2.1 + 3.4)
print(Var2)
print(Var3)
print(Var4)


def addoneAddTwo(Numberone, NumberTwo):
    Output = Numberone + 1
    # Output = Output + NumberTwo + 2
    Output += NumberTwo + 2
    return Output


Sum = addoneAddTwo(Var2, Var3)

print(Sum)
