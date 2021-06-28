
import math

class Triangle():
    def __init__(self, a, b, c):
        self.sidea = a
        self.sideb = b
        self.sidec = c
    def area(self):
        s=(self.sidea+self.sideb+self.sidec)/2
        area=math.sqrt(s*(s-self.sidea)*(s-self.sideb)*(s-self.sidec))
        return area
    def perimeter(self):
        perimeter = self.sidea + self.sideb + self.sidec
        return perimeter
    def scale(self, scale_factor):
        return Triangle(self.sidea*scale_factor, self.sideb*scale_factor, self.sidec*scale_factor)
    def is_valid(self):
        valid = ((self.sidea+self.sideb)>self.sidec) and ((self.sidea+self.sidec)>self.sideb) and ((self.sideb+self.sidec)>self.sidea)
        return valid
    def is_right(self):
        right = ((self.sidec*self.sidec==self.sidea*self.sidea + self.sideb*self.sideb))
        return right