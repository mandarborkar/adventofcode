f1 = open("advent1input.txt", "r")
inputlist = f1.readlines()

digitarr = [c.replace('\n', '') for c in inputlist]

total = 0

for i in range(0, len(digitarr)):
    translateTable = digitarr[i].maketrans("abcdefghijklmnopqrstuvwxyz", "                          ")
    output = digitarr[i].translate(translateTable)
    output1 = output.replace (' ', '')
    total += int(output1[0])*10+int(output1[-1])

print(total )