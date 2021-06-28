# calculate sumofsquares: (1*1) + (2*2) + ...
sumofsquares = 0
for i in range(1, 101):
    sumofsquares += i * i

# calculate squareofsums: (1+2+...)^ 2
squaresofsums = 0
for i in range(1, 101):
    squaresofsums += i
squaresofsums = squaresofsums * squaresofsums

print(squaresofsums - sumofsquares)
