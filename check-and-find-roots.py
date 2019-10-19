#PROGRAM TO CHECK ANF FIND ROOTS OF AN EQUATION

import math
print("Enter Value for ax\u00b2 + bx + c  :")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

d= (b*b) - 4*a*c

if d<0:
    print(a,"x\u00b2","+", b,"x", "+", c, " has no real roots")

elif d==0:
    print(a,"x\u00b2","+", b,"x", "+", c,"The Equation has equal real roots")
    r1= (-b + math.sqrt(d) )/ 2*a
    r2= ( -b - math.sqrt(d) )/ 2*a
    print(r1)
    print(r2)

elif d>0:
    print(a,"x\u00b2","+", b,"x", "+", c,"have two distinct real roots that are :")
    r1= (-b + math.sqrt(d) )/ 2*a
    r2= ( -b - math.sqrt(d) )/ 2*a
    print(r1)
    print(r2)

else:
    print("INVALID VALUES")
 
