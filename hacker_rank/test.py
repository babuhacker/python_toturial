
L = input().split(",")

print(L)

big = L[0]

second_big = L[0]

for i in range(1, len(L)):

    if L[i] > big:

        second_big = big

        big = L[i]

    elif L[i] > second_big:

        second_big = L[i]

print(second_big)
