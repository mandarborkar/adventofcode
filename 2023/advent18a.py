mydictionary = {}

f1 = open("advent18testinput.txt", "r")
inputlist = f1.readlines()

trenchinstructions = [c1.split(' ') for c1 in [c.replace('\n', '') for c in inputlist]]
print (trenchinstructions)

for c in trenchinstructions:
    if c[0].__eq__('R'):
        print ('Right ', c[1])
    elif c[0].__eq__('L'):
        print('Left ', c[1])
    elif c[0].__eq__('U'):
        print('Up ', c[1])
    elif c[0].__eq__('D'):
        print('Down ', c[1])

exit (0)