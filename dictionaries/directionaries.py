'''Dictionaries are Python's implementation of a data structure that
 is more generally known as an associative array. A dictionary consists
  of a collection of key-value pairs. Each key-value pair maps the key
   to its associated value'''


BlackShoes = {42: 2, 41: 3, 40: 4, 39: 1, 38: 0}
print(BlackShoes)
while (True):
    purchaseSize = int(input("Which shoe size would you like to buy?\n"))
    if purchaseSize < 0:
        break
    if BlackShoes[purchaseSize] > 0:
        BlackShoes[purchaseSize] -= 1  # BlackShoes[purchaseSize] - 1
    else:
        print("Shoes are no longer in stock")
    print(BlackShoes)
