f1 = open("/Users/mborkar/PycharmProjects/hello-world/avent9input.txt", "r")
transmit = f1.readlines()
print (len(transmit))
for i in range (0, len(transmit)):
    transmit[i] = transmit[i].replace('\n', '')
print (transmit)
