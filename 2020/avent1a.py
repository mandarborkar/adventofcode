f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent1input.txt", "r")
mylist = f1.readlines()
for i in range(0, len(mylist)-1):
    for j in range(i+1, len(mylist)):
        stx = mylist[i]
        x = int(stx[0:len(stx)-1])
        stx = mylist[j]
        y = int(stx[0:len(stx)-1])
        if x + y == 2020:
            print ('x=' + str(x) + ' y=' + str(y) +' product xy=' + str(x * y))
# Nop