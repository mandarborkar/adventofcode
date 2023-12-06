seedlist=[79, 14, 55, 13]
soillist = []
stflist = []
ftwlist = []
wtllist = []
lttlist = []
tthlist = []
htllist = []

sts = [[0,0,50],[50,98,2],[52,50,48]]
stf = [[0,15,37],[37,52,2],[39,0,15]]

# f1 = open("advent5testinput.txt", "r")

def transformlist (s, t):
    result = []
    for i in s:
        for j in t:
            if j[0] < i and i < j[0] + j[2]:
                currsoil = i + (j[0]-j[1])
                print (i,currsoil, j[1], i, j[0], j[2])
                result.append(currsoil)
    return result


soillist = transformlist(seedlist,sts)

stflist = transformlist(soillist,stf)


print (soillist)
print (stflist)
