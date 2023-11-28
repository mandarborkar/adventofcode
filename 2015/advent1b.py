calorieslist = [0]

f1 = open("advent1input.txt", "r")
inputlist = f1.readlines()

print(len(inputlist[0]))
i = 0
for j in range(0, len(inputlist[0])):
    # print (inputlist[0][j])
    if inputlist[0][j] == '(':
        i += 1
    elif inputlist[0][j] == ')':
        i -= 1
    if i == -1:
        break

print (j+1)
