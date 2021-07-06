# First code

def print_rangoli(size):
    for i in range(n):
        s = "-".join(chr(ord('a') + n - j - 1) for j in range(i + 1))
        print((s + s[::-1][1:]).center(n * 4 - 3, '-'))

    for i in range(n - 1):
        s = "-".join(chr(ord('a') + n - j - 1) for j in range(n - i - 1))
        print((s + s[::-1][1:]).center(n * 4 - 3, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# Second Code

def print_rangoli(size):
    n = size
    l1 = list(map(chr, range(97, 123)))
    x = l1[n - 1::-1] + l1[1:n]
    m = len('-'.join(x))

    for i in range(1, n):
        print('-'.join(l1[n - 1:n - i:-1] + l1[n - i:n]).center(m, '-'))

    for i in range(n, 0, -1):
        print('-'.join(l1[n - 1:n - i:-1] + l1[n - i:n]).center(m, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
