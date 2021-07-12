l = []
e = int(input())
english = list(map(int, input().rstrip().split()))
f = int(input())
french = list(map(int, input().rstrip().split()))
for i in english:
    l.append(i)
for i in french:
    l.append(i)

s = set(l)
print(len(s))
