f1 = open("advent1input.txt", "r")
inputlist = f1.readlines()

digitarr = [c.replace('\n', '') for c in inputlist]

total = 0

for i in range(0, len(digitarr)):
    print (digitarr[i])
    stopForwardmove=False
    stopBackwardmove=False
    x1=x2= 0
    for j in range (0, len(digitarr[i])):
        print(digitarr[i][j:j+5], digitarr[i][len(digitarr[i])-j-1])
        if digitarr[i][j].isdigit() and not (stopForwardmove) :
            x1=digitarr[i][j]
            stopForwardmove = True
        else:
            if digitarr[i][j:j+3].__eq__('one')  and not (stopForwardmove):
                x1 = 1
                stopForwardmove = True
            elif digitarr[i][j:j+3].__eq__('two')  and not (stopForwardmove):
                x1 = 2
                stopForwardmove = True
            elif digitarr[i][j:j+5].__eq__('three')  and not (stopForwardmove):
                x1 = 3
                stopForwardmove = True
            elif digitarr[i][j:j+4].__eq__('four')  and not (stopForwardmove):
                x1 = 4
                stopForwardmove = True
            elif digitarr[i][j:j+4].__eq__('five')  and not (stopForwardmove):
                x1 = 5
                stopForwardmove = True
            elif digitarr[i][j:j + 3].__eq__('six') and not (stopForwardmove):
                x1 = 6
                stopForwardmove = True
            elif digitarr[i][j:j+5].__eq__('seven')  and not (stopForwardmove):
                x1 = 7
                stopForwardmove = True
            elif digitarr[i][j:j+5].__eq__('eight')  and not (stopForwardmove):
                x1 = 8
                stopForwardmove = True
            elif digitarr[i][j:j+4].__eq__('nine')  and not (stopForwardmove):
                x1 = 9
                stopForwardmove = True
            elif digitarr[i][j:j+4].__eq__('zero')  and not (stopForwardmove):
                x1 = 0
                stopForwardmove = True
            #rint (x1)
        if digitarr[i][len(digitarr[i])-j-1].isdigit() and not (stopBackwardmove):
            x2 = digitarr[i][len(digitarr[i])-j-1]
            stopBackwardmove = True
        else:
            #print (digitarr[i][len(digitarr[i])-j-4:len(digitarr[i])-j])
            if digitarr[i][len(digitarr[i])-j-3:len(digitarr[i])-j].__eq__('one')  and not (stopBackwardmove):
                x2 = 1
                stopBackwardmove = True
            elif digitarr[i][len(digitarr[i])-j-3:len(digitarr[i])-j].__eq__('two')  and not (stopBackwardmove):
                x2 = 2
                stopBackwardmove = True
            elif digitarr[i][len(digitarr[i])-j-5:len(digitarr[i])-j].__eq__('three')  and not (stopBackwardmove):
                x2 = 3
                stopBackwardmove = True
            elif digitarr[i][len(digitarr[i])-j-4:len(digitarr[i])-j].__eq__('four')  and not (stopBackwardmove):
                x2 = 4
                stopBackwardmove = True
            elif digitarr[i][len(digitarr[i])-j-4:len(digitarr[i])-j].__eq__('five')  and not (stopBackwardmove):
                x2 = 5
                stopBackwardmove = True
            elif digitarr[i][len(digitarr[i])-j-3:len(digitarr[i])-j].__eq__('six')  and not (stopBackwardmove):
                x2 = 6
                stopBackwardmove = True
            elif digitarr[i][len(digitarr[i])-j-5:len(digitarr[i])-j].__eq__('seven')  and not (stopBackwardmove):
                x2 = 7
                stopBackwardmove = True
            elif digitarr[i][len(digitarr[i])-j-5:len(digitarr[i])-j].__eq__('eight')  and not (stopBackwardmove):
                x2 = 8
                stopBackwardmove = True
            elif digitarr[i][len(digitarr[i])-j-4:len(digitarr[i])-j].__eq__('nine') and not (stopBackwardmove):
                x2 = 9
                stopBackwardmove = True
            elif digitarr[i][len(digitarr[i])-j-4:len(digitarr[i])-j].__eq__('zero') and not (stopBackwardmove):
                x2 = 0
                stopBackwardmove = True
            #print(x2)
        if stopForwardmove and stopBackwardmove :
            print (x1, x2)
            break

    total += int(x1)*10+int(x2)

print(total)