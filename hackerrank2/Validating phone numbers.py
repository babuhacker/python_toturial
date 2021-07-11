# n = int(input())
# for i in range(n):
#     s = str(input())
#     if s[0] == "7" or s[0] == "8" or s[0] == "9":
#         if len(s) == 10:
#             print("YES")
#     else:
#         print("NO")

import re


def checker(contact):
    pattern = r"[789]\d{9}$"
    if re.match(pattern, contact):
        return "YES"
    else:
        return "NO"


n = int(input())
for i in range(n):
    print(checker(input()))
