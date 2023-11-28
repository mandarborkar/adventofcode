f1 = open("advent2input", "r")
inputlist = f1.readlines()
print(inputlist)

total = 0
for i in range(0, len(inputlist)):
    numbers = inputlist[i].replace("\n", "").split("x")
    # print("nums " + numbers[i])
    print(numbers)
    print(numbers[0])
    print(numbers[1])
    print(numbers[2])

    total += 2 * ((int(numbers[0])*int(numbers[1])) + (int(numbers[0])*int(numbers[2])) + (int(numbers[2])*int(numbers[1]))) +  min((int(numbers[0])*int(numbers[1])) , (int(numbers[0])*int(numbers[2])) , (int(numbers[2])*int(numbers[1])))
    print(total)
