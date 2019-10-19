a=[]
n=int(input("enter the number of values to be inserted"))
for i in range(0,n):
    a.append([])

print("Enter the Elements:")
for i in range(0,n):
    print("Enter the value for", i+1, "th", "element", end=" ")
    a[i]=int(input(" - "))

target=int(input("Enter The Value to be Searched"))

found=0
i=0
com=0

for i in range(0,n):
    com=com+1
    if target==a[i]:
        print("Value print at", i+1, "position")
        print("Value compared", com, "times")
        found=1

if found==0:
    print("Value Not Found")
