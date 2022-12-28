'''
mjqjpqmgbljsphdztnvjfqwrcgsmlb
'''

f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent6input.txt", "r")
inputlist = f1.readlines()
foundindex=0
print (inputlist)
for i in range(0, len(inputlist[0])-3):
    print (i)
    processstring = inputlist[0][i:i+4]
    duplicates = [x for x in set(processstring) if processstring.count(x) > 1]
    print(processstring)
    print(duplicates)
    if  len(duplicates) == 0 :
        foundindex=i
        break

print(foundindex+4)


