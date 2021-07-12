l = []
e = int(input())
english = set(map(int, input().split()))
f = int(input())
french = set(map(int, input().split()))

inter = english.intersection(french)
print(len(inter))
