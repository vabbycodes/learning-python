print("select 1 for F to C")
print("select 2 for C to F")
choice=int(input("enter choice"))
if choice==1:
    F=int(input("tempreature in farenheit"))
    C=5*(F-32)/9
    print("tempreature in celcius=",C)
if choice==2:
    C=int(input("tempreture in celcius"))
    F=9*C/5+32
    print("tempreature in farenheit=",F)
