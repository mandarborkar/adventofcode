'''
[N]         [C]     [Z]
[Q] [G]     [V]     [S]         [V]
[L] [C]     [M]     [T]     [W] [L]
[S] [H]     [L]     [C] [D] [H] [S]
[C] [V] [F] [D]     [D] [B] [Q] [F]
[Z] [T] [Z] [T] [C] [J] [G] [S] [Q]
[P] [P] [C] [W] [W] [F] [W] [J] [C]
[T] [L] [D] [G] [P] [P] [V] [N] [R]
 1   2   3   4   5   6   7   8   9
'''
boxes = [['T','P','Z','C','S','L','Q','N'],
         ['L','P','T','V','H','C','G'],
         ['D','C','Z','F'],
         ['G','W','T','D','L','M','V','C'],
         ['P','W','C'],
         ['P','F','J','D','C','T','S','Z'],
         ['V','W','G','B','D'],
         ['N','J','S','Q','H','W'],
         ['R','C','Q','F','S','L','V']]
f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent5input.txt", "r")
inputlist = f1.readlines()
mycommand = []
for i in range(0, len(inputlist)):
# for i in range(0, 1):
    mycommand.append(inputlist[i].replace('\n','').split())
    moves = int(mycommand[-1][1])
    source = int(mycommand[-1][3])-1
    target = int(mycommand[-1][5])-1
    print(moves)
    print(source)
    print(target)
    for j in range(0, moves):
        boxes[target].append(boxes[source][-1])
        boxes[source].pop()

print(boxes)

finalbottom = ''

for i in range(0, len(boxes)):
    finalbottom += boxes[i][-1]
print(finalbottom)


