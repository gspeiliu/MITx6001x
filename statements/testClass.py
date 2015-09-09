class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y
X = 7
Y = 8
w1 = Weird(X, Y)
print w1.getX()