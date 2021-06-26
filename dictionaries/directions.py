

# Sets = {"Element1","Element2","Element1","Element4"}
# print(Sets)
# if "Element1" in Sets:
#     print("Yes")


CountryList =[]
for i in range(1):
    Country = input("Please Enter Your Country:")
    CountryList.append(Country)

CountrySet = set(CountryList)

print(CountryList)
print(CountrySet)
#
# if "USA" in CountrySet:
#     print("ATTENDED.")
#
# if "India" in CountrySet:
#     print("ATTENDED.")
#
# if "Pakistan" in CountrySet:
#     print("Not Allowed.")

# Dictionary = {"Key":"Value","Key2":"Value2","Key3","Value3"}

CountryDictionary = {}
for Country in CountryList:
    if Country in CountryDictionary:#List[0}
        CountryDictionary[Country] += 1

    else:
        CountryDictionary[Country] = 1

print(CountryDictionary)





