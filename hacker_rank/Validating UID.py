T = int(input())
for i in range(T):
    a = str(input())
    c = 0
    for i in a:
        if (i.isupper()):
            c += 1
    if (c > 1):
        d = 0
        for j in a:
            if (j.isnumeric()):
                d += 1
        if (d > 2):
            if (a.isalnum()):
                if (len(a) == 10):
                    t = 0
                    for k in a:
                        for h in a:
                            if (k == h):
                                t += 1
                    if (t == 10):
                        print("Valid")
                    else:
                        print("Invalid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")
