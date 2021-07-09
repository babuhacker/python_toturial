# #
# # Student ID → ___1_____2_____3_____4_____5__
# # Subject 1   |  89    90    78    93    80
# # Subject 2   |  90    91    85    88    86
# # Subject 3   |  91    92    83    89    90.5
# #             |______________________________
# # Average        90    91    82    90    85.5
#


n = list(map(int, input().split()))
n, x = n[0], n[1]
z = []
for i in range(x):
    z.append(list(map(float, input().split())))

zipvar = zip(*z)

for i in zipvar:
    print(sum(i) / x)
