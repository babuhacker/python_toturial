# file = open("filename","r")#"r","w","a","r+" -> read and write
# file.close()

vacationspots = ["london", "paris", "new york", "utha", "ice land"]

vacationfile = open("vacationplaces", "w")

for spots in vacationspots:
    vacationfile.write(spots + "\n")

vacationfile.close()

vacationfile = open("vacationplaces", "r")

firstline = vacationfile.readline()
print(firstline)
secondline = vacationfile.readline()
print(secondline)
for line in vacationfile:
    print(line, end="")

# thewholefile =vacationfile.read()
#
# print(thewholefile)

vacationfile.close()

finalspot = "thailand\n"

vacationfile = open("vacationplaces", "a")
vacationfile.write(finalspot)
vacationfile.close()

vacationfile = open("vacationplaces", "r")
for line in vacationfile:
    print(line, end="")
vacationfile.close()

for i in range(5):
    with open("vacationplaces" + str(i), "r") as vacationfile:
        for line in vacationfile:
            print(line)

vacationfile.read()
