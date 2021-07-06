def swap_case(word):
    word1 = ''
    for i in word:
        if (i.isupper()) == True:
            word1 += (i.lower())
        elif (i.islower()) == True:
            word1 += (i.upper())
        else:
            word1 += i

    return word1


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
