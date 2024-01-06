
f1 = open("advent9testinput.txt", "r")
inputlist = f1.readlines()

oasis = [c1.split(' ') for c1 in [c.replace('\n', '') for c in inputlist]]
print(oasis)

exit