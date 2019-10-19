#PROGRAM TO ENTER AND SEARCH VALUES IN AN ARRAY USING FOR LOOP
n=int(input("enter the number of temrs"))
a=[]
for i in range(0,n):
    a.append([])

for i in range(0,n):
    a[i]=int(input("enter value"))

val=int(input("Enter the value you want to search"))
found=0
for i in range(0,n):
    if a[i]==val:
        found=1
        break

if found==1:
    print(val,"Value found at index", i+1)

else:
    print("value not find")
