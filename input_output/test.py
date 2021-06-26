import os

file = []
while True:
    option = input("what you want to do?\n")
    if option == 'file':
        user = input("now you want to\n""1.read.\n"  "2.delete.\n"  "3.append.\n")

        if user == 'read':
            name = input("tell me the file name")
            outputfile = open(name, "r")
            file_content = outputfile.read()
            print(file_content)

        if user == "delete":
            os.remove('file.abc')

        if user == "append":
            name1 = input("tell me the file name")
            outputfile = open(name1,"a")
            outputfile.write(input("what you want to write. "))
            outputfile.close()
