#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#*************

#whitespace = 7-i
#(*)*(2xi)-1

for i in range(7):
    for j in range(7):
        print(""*(7-i),"*",""*(7-i), end="")
    print(i-1)