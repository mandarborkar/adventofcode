instruct = 'LRLRRRLRRLRRRLRRRLLLLLRRRLRLRRLRLRLRRLRRLRRRLRLRLRRLLRLRRLRRLRRLRRRLLRRRLRRRLRRLRLLLRRLRRRLRLRRLRRRLRRLRLLLRRRLRRLRRLRRRLRRRLRRRLRLRLRLRRRLRRRLLLRRLLRRRLRLRLRRRLRRRLRRLRRRLRLRLLRRRLRLRRLRLRLRRLLLRRRLRRRLRRLRRLRLRRLLRRLRRRLRRRLLRRRLRRLRLLRRLRLRRLLRRRLLLLRRLRRRLRLRRLLRLLRRRLLRRLLRRRLRRRLRRLLRLRLLRRLLRLLLRRRR'
instructtest = 'LR'
mydictionary = {}

def find_lcm(num1, num2):
    if(num1>num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2)/int(gcd))
    return lcm

def find_Z (curr_position, currdictionary):

    newx = []
    steps = 0
    while (1 == 1):
        for i in instruct:
            newx = currdictionary[curr_position]
            if i.__eq__('R'):
                curr_position = newx[1]
            else:
                curr_position = newx[0]
            steps += 1
            # print(i, curr_position)
            if curr_position[-1].__eq__('Z'):
                break
        if curr_position[-1].__eq__('Z'):
            # print(steps)
            break
    return steps

f1 = open("advent8input.txt", "r")
inputlist = f1.readlines()

network = [c1.split(' =') for c1 in [c.replace('\n', '') for c in inputlist]]
network1 = []

for i in range(0, len(network)):
    network1.append(network[i][1].replace(' (','').replace(')','').split(', '))

for i in range(0, len(network)):
    # print (network[i])
    mydictionary[network[i][0]] = network1[i]

print ('Dictionary ', mydictionary)

res = [key for key, val in mydictionary.items() if key.endswith('A')]
print ('Starting point ', res)

steps = []
for curr_position in res:
    steps.append(find_Z (curr_position, mydictionary))
    print ('steps ', steps, ' ', curr_position)

num1 = steps[0]
num2 = steps[1]
lcm = find_lcm(num1, num2)

for i in range(2, len(steps)):
    lcm = find_lcm(lcm, steps[i])

print(lcm)


'''
# exit(0)
steps = 0

while (1==1):
    for i in instruct:
        steps += 1
        if steps > 1000000:
            exit(0)
        newres = []
        for curr_position in res:
            if curr_position[-1].__eq__('Z'):
                # print('Found Z res', steps, res)
                continue
            else:
                newx = mydictionary[curr_position]

                if i.__eq__('R'):
                    newres.append (newx[1])
                else:
                    newres.append (newx[0])

                for a in newres:
                    if a[-1].__eq__('Z'):
                        print('Found Z newres', steps, newres)

            res = []
            res = newres

        # print ('new res', newres)
        # exit(0)
        condition = True
        for a in newres:
            if a[-1].__eq__('Z'):
                print('Found Z ', steps, newres)
                exit(0)
            if not a[-1].__eq__('Z') :
                # print(steps, newres)
                condition = False
                break
            else:
                print('Found Z ', steps, newres)


        if condition:
            #print('False ',steps, newres)
            break
        else:
            #print('True  ',steps, newres)
            res = []
            res = newres

    if condition:
        break
    elif steps > 10000000 :
        print ('Steps > 1000')
        break
'''