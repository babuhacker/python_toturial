from collections import deque

t = int(input())
while t > 0:
    n = int(input())  # q value
    A = list(map(int, input().split()))  # list of q value
    lst = deque(A)  # pass this list to the deque
    rm = lst.pop()  # The right most element
    lm = lst.popleft()  # The left most element
    csv = lm if lm > rm else rm  # The current element value
    lp = -1  # The latest peaked value
    flag = False
    while (len(lst) > 0):
        # Main Logic
        if (lm >= rm and lm <= csv):
            csv = lm
            lm = lst.popleft()
            latest = lm
        elif (rm > lm and rm <= csv):
            csv = rm
            rm = lst.pop()
            latest = rm
        else:
            flag = True
            break
    if flag or latest > csv:
        print("No")
    else:
        print("Yes")
    t -= 1
