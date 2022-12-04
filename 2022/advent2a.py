# Scoring
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# Win Rock (X) defeats Scissors (C), Scissors (Z) defeats Paper (B), and Paper (Y) defeats Rock (A).

def calculatescore (play1, play2):
    score=0
    if play2=='X':
        score=1
    elif play2=='Y':
        score=2
    elif play2=='Z':
        score=3

    if ((play1=='C' and play2=='X') or (play1=='B' and play2=='Z') or (play1=='A' and play2=='Y')):
        return score+6
    elif (play1=='B' and play2=='Y') or (play1=='C' and play2=='Z') or (play1=='A' and play2=='X'):
        return score+3
    else:
        return score+0

f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent2input.txt", "r")
inputlist = f1.readlines()

myTotalScore=0

for i in range (0,len(inputlist)):
    myTotalScore += calculatescore(inputlist[i][0], inputlist[i][2])
    print ('play = ' + inputlist[i] + ' current score = ' + str(myTotalScore))
