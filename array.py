#Program to make an array then insert and print the values
n=int(input("enter the number of terms"))
a=[]
for i in range(0,n):
    a.append([])

for i in range(0,n):
    a[i]=int(input("enter value"))
for i in range(0,n):
    print("value inserted in","a [",i,"] = ", a[i])
