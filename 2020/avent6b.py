f1 = open("/Users/mborkar/PycharmProjects/hello-world/avent6input.txt", "r")
questionsstring = f1.read()
#print (questionsstring)
questions = questionsstring.split("\n\n")
for i in range (0,len(questions)):
    questions[i]=questions[i].replace('\n',' ')
# print (questions)
#print (len(questions))

# print (questions[0])
numberofquestions=0
for i in range (0,1):
    print (questions[0])
    answerperperson = questions[i].split(" ")
    print (answerperperson)

    for j in range (0,len(answerperperson)):
        foundinall = True
        print ("processing question " + answerperperson[j])
        while answerperperson[j]:
            for k in range(j+1,len(answerperperson)):
                print("looking for " + answerperperson[j][0] + " in " + answerperperson[k])
                if answerperperson[j][0] not in answerperperson[k]:
                    foundinall = False
                    break
            if not foundinall :
                break
            else:
                numberofquestions += 1
                print(answerperperson[j][0] + " found in all, count = " + str(numberofquestions))
                answerperperson[j] = answerperperson[j].replace(answerperperson[j][0], '')
                print (answerperperson[j])
        if not foundinall :
            break

    ''' 
    while questions[i] :
        # print (questions[0][0])
        questions[i] = questions[i].replace(questions[i][0],'')
        numberofquestions += 1
        # print(numberofquestions)
        # print (questions[0])
    '''
print ("Total questions answered yes : " + str(numberofquestions))