c = 0
e = int(input())
english = set(map(int, input().rstrip().split()))
f = int(input())
french = set(map(int, input().rstrip().split()))
l = english.difference(french)
print(len(l))
