def checkvaladity(number):
    T = number.split("-")
    P = "".join(T)

    if number[0] in '456':
        if len(number) == 16 or len(number) == 19:
            d = "1234567890-"
            for j in number:
                if j not in d:
                    return False
            if len(number) == 19:
                d2 = "1234567890"
                for x in T:
                    if len(x) != 4:
                        return False
            for x in range(len(P) - 4):
                if P[x:x + 4] == P[x] * 4:
                    return False
            return True
    return False


n = int(input())
for x in range(n):
    if (checkvaladity(input())):
        print("Valid")
    else:
        print("Invalid")
 