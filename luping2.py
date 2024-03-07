
# 1
# 121
# 12321
# 1234321
# 123454321
# 12345654321
# 1234567654321


for i in range(1, 5):
    for m in range(7 - i):
        print(" ", end="")
    for j in range(i *2-1):
        print('*', end="")
    print()

for i in range(3, 0, -1):
    for m in range(7 - i):
        print(" ", end="")
    for j in range(i * 2 - 1):
        print('*', end="")
    print()

