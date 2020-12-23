f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent8input.txt", "r")
instructionset = f1.readlines()
# print (len(instructionset))
instructiondetails = []

for i in range (0,len(instructionset)):
    instructionset[i]=instructionset[i].replace('\n','')
    instructiondetails.append ( instructionset[i].split(" ") )
    instructiondetails[i].append ("N")
    # print (instructiondetails)
    # print ("instruction is = " + str(i) + " " + str(instructionset[i]) + "\ninstruction visited = " + str(instructiondetails[i][2]) + " instruction = " + str(instructiondetails[i][0]) + " operation = " + str(instructiondetails[i][1]))

# instructiondetails[601][0] = "nop"
#print (instructiondetails[601])
maxindex = len(instructionset)-1
#print (maxindex)

def evaluatetermination (instructiondetails):

    index = 0
    accumulate = 0
    maxindex = len(instructiondetails)

    while instructiondetails[index][2] == "N" or index == maxindex:
        instructiondetails[index][2] = "Y"
        # print ("instruction being executed : " + str(instructiondetails[index]) + " index at " + str(index) + " accumulated = " + str(accumulate))
        if instructiondetails[index][0] == "jmp" :
            index = index + int(instructiondetails[index][1])
        elif instructiondetails[index][0] == "nop" :
            index += 1
        elif instructiondetails[index][0] == "acc" :
            accumulate = accumulate + int(instructiondetails[index][1])
            index+=1
    if index == maxindex-1:
        print ("max accumulated = " + str(accumulate) + " index at "+ str(index))
        return accumulate
    else:
        print ("infinite loop")
        return 0

for i in range (0,len(instructiondetails)):
    accx=0
    if instructiondetails[i][0] == "nop":
        instructiondetails[i][0] = "jmp"
        accx = evaluatetermination(instructiondetails)
        instructiondetails[i][0] = "nop"
        print("found nop/jmp " + str(accx) + " index = " + str(i))
    elif instructiondetails[i][0] == "jmp":
        instructiondetails[i][0] = "nop"
        accx = evaluatetermination(instructiondetails)
        instructiondetails[i][0] = "jmp"
        print("found nop/jmp " + str(accx) + " index = " + str(i))
    if accx > 0 :
        print ("found change")
        break