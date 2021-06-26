
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
first = 1
second = 2
sum = 2
for i in range(1,4000000):
    third = first+second
    first = second
    second = third
    if third % 2 == 0:
        if third > 4000000:
            break
        sum += third

print(sum)