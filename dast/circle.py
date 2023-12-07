from cmath import pi

class Circle():
    def __init__(self , r=0):
        self.r = r

    def getArea(self):
        return pi*((self.r)*(self.r))

    def getPerimeter(self):
        return pi*2*(self.r)