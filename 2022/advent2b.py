# Scoring
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

# A for Rock, B for Paper, and C for Scissors
# X for lose, Y for draw, and Z for win
# Win Rock (X) defeats Scissors (C), Scissors (Z) defeats Paper (B), and Paper (Y) defeats Rock (A).

def calculatescore(play1, play2):
    score = 0
    if play2 == 'X':
        score = 0
    elif play2 == 'Y':
        score = 3
    elif play2 == 'Z':
        score = 6

    # X=0 -> A=3;B=1;C=2
    # Y=3 -> A=1;B=2;C=3
    # Z=6 -> A=2;B=3;C=1

    if (play1 == 'B' and play2 == 'X') or (play1 == 'A' and play2 == 'Y') or (play1 == 'C' and play2 == 'Z'):
        return score+1
    elif (play1 == 'C' and play2 == 'X') or (play1 == 'B' and play2 == 'Y') or (play1 == 'A' and play2 == 'Z'):
        return score+2
    elif (play1 == 'A' and play2 == 'X') or (play1 == 'C' and play2 == 'Y') or (play1 == 'B' and play2 == 'Z'):
        return score+3


f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent2input.txt", "r")

inputlist = f1.readlines()
myTotalScore = 0

for i in range(0, len(inputlist)):
    myTotalScore += calculatescore(inputlist[i][0], inputlist[i][2])
    print('play = ' + inputlist[i] + ' current score = ' + str(myTotalScore))
