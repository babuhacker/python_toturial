def Operations():
    global output
    ol = input().split()
    operations = ol[0]
    updaterset = set(map(int, input().split()))
    if operations == "intersection_update":
        a.intersection_update(updaterset)
    elif operations == "update":
        a.update(updaterset)
    elif operations == "symmetric_difference_update":
        a.symmetric_difference_update(updaterset)
    elif operations == "difference_update":
        a.difference_update(updaterset)
    output = sum(a)
    return output


input()
a = set(map(int, input().split()))
n = int(input())
for i in range(n):
    Operations()
print(output)
