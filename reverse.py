row = input("Name: ")
length = len(row)

for i in range(length-1 , -1, -1):
    print(row[i], end=' ')
