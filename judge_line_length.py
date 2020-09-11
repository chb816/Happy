import math

class Point2D :
    def __init__(self, x=0, y=0) :
        self.x = x
        self.y = y

p = [Point2D(), Point2D(), Point2D(), Point2D()]

for i in p :
    i.x, i.y = map(int, input().split())

def linelength(x, y) :
    length = 0.0
    length = math.sqrt(math.pow((y.x - x.x),2) + math.pow((y.y - x.y),2))
    return length

length_def = 0.0
length_def = linelength(p[0], p[1]) + linelength(p[2], p[1]) + linelength(p[3], p[2])
print(length_def)

