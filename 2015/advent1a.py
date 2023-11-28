calorieslist = [0]

f1 = open("advent1input.txt", "r")
inputlist = f1.readlines()

print(inputlist)
j = 0

# for i in range(0, len(inputlist)):
for k in range(0, len(inputlist[0])):
    print (inputlist[0][k])
    if inputlist[0][k] == '(':
        j += 1
    elif inputlist[0][k] == ')':
        j -= 1

print (j)

'''
j = 0
for i in range(0, len(inputlist)):
    if inputlist[i] == '\n':
        j += 1
        calorieslist.append(0)
    else:
        calorieslist[j] += int(inputlist[i].replace('\n', ''))
    print(calorieslist[j])

print("Elf no. " + str(calorieslist.index(max(calorieslist))) + " has max calories " + str(max(calorieslist)))
'''