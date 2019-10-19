a=[]
n=int(input("Enter the number of values to be inserted - "))
for i in range(0,n):
    a.append([])

print("Enter the Elements:")
for i in range(0,n):
    print("Enter the value for", i+1, "th element", end=" ")
    a[i]=int(input(" - "))
print("")
shift=0

for i in range(1,n): 
  
        currentv = a[i] 
  
        pos = i-1
        while pos >=0 and currentv < a[pos] :
            a[pos+1] = a[pos]
            pos -= 1
        a[pos+1] = currentv
        shift=shift+1
        print("Value after", shift, "shift - ", end=" " )
        for m in range(0,n):
            print(a[m], end=" ")
        print()

print("Sorted List is ")
for i in range(0,n):
    print(a[i], end=" ")
