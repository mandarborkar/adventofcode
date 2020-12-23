f1 = open("/Users/mborkar/PycharmProjects/hello-world/avent13input.txt", "r")
schedule = f1.readlines()

for i in range (0,len(schedule)):
    schedule[i] = schedule[i].replace ('\n','')


print (schedule)
schedule[1] = schedule[1].replace ('x,','')
print(schedule[1])
busnumbers = schedule[i].split (",")

waitingtime = []
minimumwait = 0
earliestbus = -1
for i in range (0,len(busnumbers)):
    x = int(int(schedule[0])/int(busnumbers[i]))
    waitingmins = (int(busnumbers[i])*(x+1))-int(schedule[0])
    #print (x)
    #print (waitingmins)
    waitingtime.append (waitingmins)
    #print (waitingtime)
    if minimumwait > waitingmins or minimumwait == 0 :
        minimumwait = waitingmins
        earliestbus = i
print (waitingtime)
print (earliestbus)
print (minimumwait)
print (str(int(busnumbers[earliestbus]) * int(minimumwait)))