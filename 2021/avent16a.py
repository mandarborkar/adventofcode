
filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent23testinput.txt'

message = "D2FE28"

messagecode = {}

for readline in open(filename):
    first, second = readline.strip().replace('\n','').split('=')
    print (first+second)
    messagecode.update({first.strip(): second.strip()})
    if first in ["F"]:
        break

print (message)
messagebin = ''
for i in range (0,len(message)):
    messagebin += messagecode.get(message[i])

print (int(messagebin[0:3],2))