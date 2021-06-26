
family_list = {}


'''
{"name":aditya, "age":15,"father":rajesh,"future":software engineer}
'''


while True:
    option = input("enter your option eg., add, remove, exit")
    if option == "add":
        name = input("please enter name")
        age = int(input("please enter age"))
        father = input("please enter father")
        future = input("please enter future")

        temp = {}
        temp['name'] = name
        temp['age'] = age
        temp['father'] = father
        temp['future'] = future
        family_list[name] = temp
    elif option == "remove":
        name = input("please enter the name you want to remove")
        try:
            del family_list[name]
        except Exception:
            print(f"sorry the name:{name} is not avaliable")
    elif option == "exit":
        break

    print(family_list)
