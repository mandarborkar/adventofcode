from collections import OrderedDict
def duplicates (hand):
    duplicate = []
    for c in "".join(OrderedDict.fromkeys(hand)):
        duplicate.append([hand.count(c),c])
    # print (duplicate)
    duplicate.sort(key=lambda x: x[0])
    return duplicate


f1 = open("advent7testinput.txt", "r")
inputlist = f1.readlines()
cardlist = [c1.split(' ') for c1 in [c.replace('\n', '') for c in inputlist]]
# print (cardlist)
ranking = []
for i in range (0,len(cardlist)):
    score = duplicates(cardlist[i][0])

    if score[-1][0] == 5 : # Five of a kind
        rank = 5
    elif score[-1][0] == 4: # four of a kind
        rank = 4
    elif score[-1][0] == 3 and score[-2][0]==2: # Three of a kind + Pair = Full house
        rank = 3.5
    elif score[-1][0] == 3 and score[-2][0]==1: # Three of a kind + individual
        rank = 3
    elif score[-1][0] == 2 and score[-2][0]==2: # Two pair
        rank = 2.5
    elif score[-1][0] == 2 and score[-2][0]==1: # One pair
        rank = 2
    else:
        rank = 1 #highest card

    ranking.append([cardlist[i][1],rank,score,cardlist[i][0]])

ranking.sort(key=lambda x: x[1])
for i in ranking:
    print (i)

