f1 = open("/Users/mborkar/PycharmProjects/hello-world/avent14input.txt", "r")
dockinstructions = f1.readlines()

for i in range (0,len(dockinstructions)):
    dockinstructions[i] = dockinstructions[i].replace ('\n','')


print (dockinstructions)