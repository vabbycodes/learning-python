a=[]
n=int(input("Enter the number of values to be inserted - "))
for i in range(0,n):
    a.append([])

print("Enter the Elements:")
for i in range(0,n):
    print("Enter the value for", i+1, "th element", end=" ")
    a[i]=int(input(" - "))
print("")

print("Your Input Values are - ", end="")
for i in range(0,n):
    print(a[i], end=" ")
print("")
print("\nSorting Values:")

for j in range(0,n):
    small=a[j]
    index=j
    for i in range(j+1, n):
        if a[i]<small:
            small=a[i]
            index=i
    print("Exchanged", a[j], "=>", a[index], ", Now", end=" ")
    a[index]=a[j]
    a[j]=small
    print("Values After Exchange are", end=" ")
    for i in range(0,n):
        print(a[i], end=" ")
    print()
print("")

print("Your Values After Selection Sort are : ")
for i in range(0,n):
    print(a[i], end=" ")
