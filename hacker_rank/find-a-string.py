def count_substring(string, sub_string):
    nl = len(string)
    sl = len(sub_string)
    c = 0

    for i in range(nl - sl + 1):
        if (string[i:(i + sl)] == sub_string):
            c = c + 1

    return c  # string.find(sub_string)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
