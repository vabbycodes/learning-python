#Program to create a 2-D Matrice
c=int(input("enter the no. of columns in the matrix"))
r=int(input("enter the no. of rows in the matrix"))
m=[]
for i in range(0,c):
    m.append([])

for i in range(0,c):
    for j in range(0,r):
        m[i].append([j])

print("Enter the elements of matrix")
for i in range(0,c):
    for j in range(0,r):
        print("enter the value for", i+1, "*", j+1, "element")
        m[i][j]=int(input())

print("Values in your matrix are")
for i in range(0,c):
    for j in range(0,r):
        print("Value in", i+1, "*", j+1, "is")
        print(m[i][j])
