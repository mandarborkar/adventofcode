# Scoring
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# Rock (AX) defeats Scissors (BY), Scissors (CZ) defeats Paper (BY), and Paper (BY) defeats Rock (AX).

f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent2input.txt", "r")
inputlist = f1.readlines()

# A Z - i am defeated so score=0+3

myTotalScore = 0





calorieslist = [0]


j = 0
for i in range(0, len(inputlist)):
    if inputlist[i] == '\n':
        j += 1
        calorieslist.append(0)
    else:
        calorieslist[j] += int(inputlist[i].replace('\n', ''))
    print(calorieslist[j])

print("Elf no. " + str(calorieslist.index(max(calorieslist))) + " has max calories " + str(max(calorieslist)))
