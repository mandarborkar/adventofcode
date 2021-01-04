f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent18input.txt", "r")
schedule = f1.readlines()

for i in range (0,len(schedule)):
    schedule[i] = schedule[i].replace ('\n','')


print ("schedule = ")
print (schedule)