from collections import Counter

if __name__ == '__main__':
    s = sorted(input())
    a = Counter(s)
    # print(a)
    a = Counter(s).most_common(3)
    # print(a)
    for x in a:
        # * is a unpack operator
        print(*x)

