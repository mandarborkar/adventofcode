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

f1 = open("advent18input.txt", "r")
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