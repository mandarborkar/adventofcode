calorieslist = [0]

f1 = open("/2022/advent2input.txt", "r")
inputlist = f1.readlines()

j = 0
for i in range(0, len(inputlist)):
    if inputlist[i] == '\n':
        j += 1
        calorieslist.append(0)
    else:
        calorieslist[j] += int(inputlist[i].replace('\n', ''))
    print(calorieslist[j])

print("Elf no. " + str(calorieslist.index(max(calorieslist))) + " has max calories " + str(max(calorieslist)))
