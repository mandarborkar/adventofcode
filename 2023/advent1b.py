calorieslist = [0]
maxvalue = 0

f1 = open("/2022/advent1input.txt", "r")
inputlist = f1.readlines()

j = 0
for i in range(0, len(inputlist)):
    if inputlist[i] == '\n':
        j += 1
        calorieslist.append(0)
    else:
        calorieslist[j] += int(inputlist[i].replace('\n', ''))
    # print(calorieslist[j])

for i in range (0,3):
    maxvalue += max(calorieslist)
    maxindex = calorieslist.index(max(calorieslist))
    print("Elf no. " + str(maxindex) + " has max calories " + str(maxvalue))
    calorieslist[maxindex]=0
