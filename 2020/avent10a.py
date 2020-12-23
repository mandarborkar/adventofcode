
f1 = open("/Users/mborkar/PycharmProjects/hello-world/avent10input.txt", "r")
adapter = f1.readlines()
print (len(adapter))
adapterint = [0]
for i in range (0, len(adapter)):
    adapterint.append(int(adapter[i].replace('\n','')))

adapterint.sort()
adapterint.append(int(adapterint[len(adapterint)-1])+3)
print (adapterint)

adapterdiff = []
for i in range (0, len(adapterint)-1):
    adapterdiff.append(adapterint[i+1]-adapterint[i])
print (adapterdiff)

count1 = adapterdiff.count(1)
print (count1)
count3 = adapterdiff.count(3)
print (count3)
print (str(count1 + count3))
print (str(count1 * count3))