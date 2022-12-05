
def fullycontained(fcs1, fce1, fcs2, fce2):
    if ((fcs1 <= fcs2) and (fce1 >= fce2)) or \
            ((fcs2 <= fcs1) and (fce2 >= fce1)) or \
            ((fcs1 >= fcs2) and (fcs1 <= fce2)) or \
            ((fce1 >= fcs2) and (fce1 <= fce2)):
        print('overlap')
        return 1
    return 0


f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent4input.txt", "r")
inputlist = f1.readlines()
totalcontained = 0
for i in range(0, len(inputlist)):
    print(inputlist[i].replace('\n', ''))
    cs1 = int(inputlist[i].replace('\n', '').split(",")[0].split("-")[0])
    ce1 = int(inputlist[i].replace('\n', '').split(",")[0].split("-")[1])
    cs2 = int(inputlist[i].replace('\n', '').split(",")[1].split("-")[0])
    ce2 = int(inputlist[i].replace('\n', '').split(",")[1].split("-")[1])

    totalcontained += fullycontained(cs1, ce1, cs2, ce2)

print(totalcontained)
