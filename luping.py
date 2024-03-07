for i in range(1, 8):
    for j in range(8 - i):
        print("&", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

for l in range(7):
    print("&"*(7-l), end="")
    for m in range (l+1):
        print(m+1, end="")
    print()