def Bsearch(a,n,target):
    found=0
    low=0
    high=n
    com=0

    while(low<=high) and not found:
        mid = int((low + high)/2)
        com=com+1
        if target < a[0]:
            print("Search Value Is Not Valid")
        elif target > a[n-1]:
            print("Search Value Is Not Valid")
        elif target < a[mid]:
            high = mid -1

        elif target >a[mid]:
            low = mid+1

        else:
            found=1

    if found:
        print("Value Present At", mid+1, "Position")
        print("Compared", com, "time(s)")

    else:
        print("Value Not Present")
        print("Compared", com, "time(s)")

n=int(input("Enter the number of elements"))


a=[]
for i in range(0,n):
    a.append([])
print("Enter the element")

for i in range(0,n):
    a[i]=int(input(":"))

target=int(input("Enter The Search Value"))

Bsearch(a,n,target)

    
