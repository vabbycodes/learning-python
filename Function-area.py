#PROGRAM TO CREATE A FUNCTION THAT CALCULATES AREA

class Rectangle(object):
    def __init__(self,w,h):
        self.width=w
        self.height=h

    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return 2*(self.width+self.height)
    
    def getwidth(self):
        return self.width

    def getheight (self):
        return self.height

    def issquare(self):
        if self.width==self.height:
            return True
        
        else:
            return False


w=int(input("Enter Width"))
h=int(input("Enter Height"))

R1=Rectangle(w,h)
print("Width is:", R1.getwidth())
print("Height is:", R1.getheight())
print("Area is:", R1.area())
print("Perimeter is:", R1.perimeter())
print("Is it a Sqaure ?", R1.issquare())
