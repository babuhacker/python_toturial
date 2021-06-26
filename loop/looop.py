'''n python, while loop is used to execute a block of statements
 repeatedly until a given a condition is satisfied. And when the
  condition becomes false, the line immediately after the loop in
   program is executed.'''

# loops

Note = "Hello"

List = []

for w in Note:
    print(w)
    if w == "H":
        print("Whata funny letter")

    List.append(w)

print(List)

for l in List:
    print(l)

Numbers = [1, 2, 3, 4, 5]

for l in Numbers:
    if l % 2 == 1:
        print(l)

# range(Starting,Stoping,Steps)

Numbers = []
for num in range(1, 12, 2):
    Numbers.append(num)
    print(num)

print(Numbers)
