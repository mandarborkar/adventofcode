f1 = open("advent1input.txt", "r")
inputlist = f1.readlines()

digitarr = [c.replace('\n', '') for c in inputlist]

total = 0

for i in range(0, len(digitarr)):
    translateTable = digitarr[i].maketrans("abcdefghijklmnopqrstuvwxyz", "                          ")
    output = digitarr[i].translate(translateTable)
    output1 = output.replace (' ', '')
    total += int(output1[0])*10+int(output1[-1])

<<<<<<< HEAD
print(total )
=======
print(total)
print ('Hello world')
>>>>>>> eeaf5eaf714a0cd51a4c4794e85230e52e2a4ec4
