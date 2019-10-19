a=[]
n=int(input("Enter the number of values to be inserted"))
for i in range(0,n):
    a.append([])

print("Enter the Elements:")
for i in range(0,n):
    print("Enter the value for", i+1, "th element", end=" ")
    a[i]=int(input(" - "))

for j in range(0,n):
    small=a[j]
    index=j
    for i in range(j+1, n):
        if a[i]<small
        small=a[i]
        index=i
a[index]=a[j]
a[j]=small
