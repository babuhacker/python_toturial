import re

n = input()
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
p = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), n, flags=re.IGNORECASE)

if p == []:
    print(-1)
else:
    for i in p:
        print(i)
