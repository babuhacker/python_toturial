# we have created a function named main
def main():
    # we have assign sum_total as one thousand
    sum_total = 1000
    # we have created a for loop in the range of sum_total
    for c in range(sum_total):
        # we have created a for loop in the range of c
        for b in range(c):
            # we have created a for loop in the range of b
            for a in range(b):
                # we are checking if a + b + c is equal to sum_total
                if a + b + c == sum_total:
                    # we are checking if is_triplet(a,b,c)
                    if is_triplet(a, b, c):
                        # we are printing (a,b,c)
                        print(a, b, c)
                        # we are printing(a multiply by b multiply by c)
                        print(a * b * c)


# we have created a function  named is_triplet(a,b,c)
def is_triplet(a, b, c):
    # we are checking if a square + b square is equal to c square
    if (a ** 2 + b ** 2) == c ** 2:
        # then printing a,b,c
        print('returning true', a, b, c)
        # we are returning true
        return True
    # we have created else
    else:
        # then returning false
        return False


# we have called main() function
main()
