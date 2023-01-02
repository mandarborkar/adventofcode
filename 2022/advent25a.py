
f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent25input.txt", "r")
inputlist = f1.readlines()
snafulist = [[*s2] for s2 in [s1[0] for s1 in [s.split() for s in inputlist]]]
print(snafulist)
fueltotal = 0
for snafu in snafulist:
    fuel = 0
    length_s = len(snafu)
    for j in range(0,length_s):
        i = length_s - j - 1
        if snafu[j]=='=':
            fuel += -2 * (5**i)
            # print(snafu,snafu[j], j, i, fuel)
        elif snafu[j]=='-':
            fuel += -1 * (5**i)
            # print(snafu, snafu[j],j, i, fuel)
        else:
            fuel += int(snafu[j]) * (5 ** i)
    # print (snafu,snafu[j],j,i, fuel, fueltotal)
    fueltotal += fuel

print(fueltotal)
# 183488001053
fivex = [5**x for x in range(0,int(fueltotal/(183488001053))) if 5**x < fueltotal]
print(fivex[::-1])
sanfuend= []
sanfuend1= []
x = fueltotal
for i in range (len(fivex),0,-1):
    div = int(x/fivex[i-1])
    sanfuend.append(div)
    sanfuend1.append(x)
    x -= div * fivex[i-1]
print (sanfuend)

