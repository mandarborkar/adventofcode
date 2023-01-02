
f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent25input.txt", "r")
inputlist = f1.read().strip().split()
print (inputlist)
revsnafulist = [x[::-1] for x in inputlist]
print(revsnafulist)

fueltotal = 0
t = {
    "0": 0,
    "1": 1,
    "2": 2,
    "-": -1,
    "=": -2
}


tx = {d:s for s,d in t.items()}
for x in revsnafulist:
    power = 1
    for y in x :
        fueltotal += (power * int(t[y]))
        power *= 5
print (fueltotal)

x = fueltotal
ans = ""
while x > 0 :
    y = ((x + 2) % 5) - 2
    ans += str(tx[y])
    x -= y
    x //= 5

print(ans[::-1])
