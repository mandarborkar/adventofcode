f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent6input.txt", "r")
questionsstring = f1.read()
#print (questionsstring)
questions = questionsstring.split("\n\n")
for i in range (0,len(questions)):
    questions[i]=questions[i].replace('\n','')
#print (questions)
#print (len(questions))

# print (questions[0])
numberofquestions=0
for i in range (0,len(questions)):
    while questions[i] :
        # print (questions[0][0])
        questions[i] = questions[i].replace(questions[i][0],'')
        numberofquestions += 1
        # print(numberofquestions)
        # print (questions[0])
print ("Total questions answered yes : " + str(numberofquestions))