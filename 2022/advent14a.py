
f = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent14testinput.txt", "r")
underground = f.readlines()
print(underground)
underground2 = [[y.split(',') for y in x] for x in [x.replace('\n','').replace(' ','').split ('->') for x in underground]]
print (underground2)

