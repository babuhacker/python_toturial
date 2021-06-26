participantnumber = 5
participantdata = []
registeredparticipant = 0
outputfile = open("participantdata.txt","w")


while(registeredparticipant < participantnumber):
    tempartdata = []#name, country of origin, age
    name = input("please enter your name: ")
    tempartdata.append(name)
    country = input("please enter your country of origin: ")
    tempartdata.append(country)
    age = int(input("please enter your age: "))
    tempartdata.append(age)#[name, country, age]
    print(tempartdata)
    participantdata.append(tempartdata)
    print(participantdata)
    #[temppartdata} = [name, country, age]

    registeredparticipant += 1# = registeredparticipant + 1


for participant in participantdata:
    for data in participant:
        outputfile.write(str(data))#str(25) -> "25"
        outputfile.write(" ")

    outputfile.write("\n")

outputfile.close()

inputfile = open("participantdata.txt", "r")

inputlist = []

for line in inputfile:
    temparticipant = line.strip("\n").split()
    # print(temparticipant)
    inputlist.append(temparticipant)
    # print(inputlist)

age = {}
print(inputlist)
for part in inputlist:
    tempage = int(part[-1])
    if tempage in age:
        age[tempage] += 1

    else:
        age[tempage] = 1

print(age)

countries = {}
for part in inputlist:
    tempcountry = (part[1])
    if tempcountry in countries:
        countries[tempcountry] += 1
    else:
        countries[tempcountry] = 1

print("countries that attended",countries)

oldest = 0
youngest = 100
mostoccuringage = 0
counter = 0

for tempage in age:
    if tempage > oldest:
        oldest = tempage
    if tempage < youngest:
        youngest = tempage
    if age[tempage] > counter:
        counter = age[tempage]
        mostoccuringage = tempage
print(oldest)
print(youngest)
print("most occuring age is:",mostoccuringage,"with",counter,"participants")

inputfile.close()
