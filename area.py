print("calculate the area of square,rectangle,circle,triangle")
import math
print("calculate area")
print("enter 1 for square")
print("enter 2 for rectangle")
print("enter 3 for circle")
print("enter 4 for triangle")
choice=int(input("enter choice"))
if choice==1:
    s=int(input("enter side"))
    print("area = ",s*s)
elif choice==2:
    a=int(input("enter length"))
    b=int(input("enter breath"))
    print("area= ",a*b)
elif choice==3:
          r=int(input("enter radius"))
          a=math.pi*r*r
          print("area= ",a)
elif choice==4:
    a=int(input("enter the side 1 of triangle"))
    b=int(input("enter side 2 of triangle"))
    c=int(input("enter the side 3 of triangle"))
    s=(a+b+c)/2
    A=math.sqrt((s-a)*(s-b)*(s-c))
    print("area= ",math.sqrt((s-a)*(s-b)*(s-c)))
else:
    print("choice is invalid")
