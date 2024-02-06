
# 1
# 121
# 12321
# 1234321
# 123454321
# 12345654321
# 1234567654321


for i in range(1, 8):
    for m in range(7 - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for k in range(i - 1, 0, -1):
        print(k, end="")
    print()
