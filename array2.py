#Program to make two arrays then multiply their values
n=int(input("enter the number of terms"))
a=[]
b=[]
for i in range(0,n):
    a.append([])
    b.append([])

for i in range(0,n):
    a[i]=int(input("enter value for a"))
    b[i]=int(input("enter value for b"))
for i in range(0,n):
    print("value for",a[i],"*", b[i],"is", a[i]*b[i])
