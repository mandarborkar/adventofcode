from IPython.display import Image
Image('images/network.PNG')

filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent12testinput.txt'

h1 = [x for x in open (filename).read().strip().split('-') ]
totalses = 0

for x in h1:
    print (x)