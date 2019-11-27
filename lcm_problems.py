a=int(input("Enter the first number - "))
b=int(input("Enter the second number - "))
ma=a
mb=b
ma=[]
mb=[]
for i in range(0,a+1):
    ma.append([])
for i in range(0,b+1):
    mb.append([])
x=0
ma[0]=0
for i in range(0,a):
    x=x+1
    if a%x==0:
        ma[x]=x
    else:
        ma[x]=0
y=0
mb[0]=0
for i in range(0,b):
    y=y+1
    if b%y==0:
        mb[y]=y
    else:
        mb[y]=0
l1=[]
ma[a-1]=a
mb[b-1]=b
print("\nCommon Multiples of", a, "and", b, "are", end=" ")
for i in range(0,a):
    for j in range(0,b):
        if ma[i]==mb[j] and ma[i]!=0:
            l1.append(ma[i])
            print(ma[i], end=" ")
print("\n")
print("The L.C.M of", a, "and", b, "is - ", end=" ")
lcm=(a*b)/max(l1)
print(int(lcm))


    
