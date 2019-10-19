#Program to add 2 Matrices
m1=int(input("Enter the no.s of row in 1st Matrice"))
n1=int(input("Enter the no.s of columns in 1st Matrice"))
m2=int(input("Enter the no.s of row in 2nd Matrice"))
n2=int(input("Enter the no.s of columns in 2nd Matrice"))
if(m1!=m2)or(n1!=n2):
    print("Matrices are Incompatible")
    exit

else:
    mat1=[]
    mat2=[]
    mat3=[]
    for i in range(0,m1):
        mat1.append([])
        mat2.append([])
        mat3.append([])
    for i in range(0,m1):
        for j in range(0,n1):
            mat1[i].append([j])
            mat2[i].append([j])
            mat3[i].append([j])

    print("enter the elements of 1st matrix")
    for i in range(0,m1):
        for j in range(0,n1):
            print("Enter value for", i+1, "*", j+1)
            mat1[i][j]=int(input())

    print("enter the elements of 2nd matrix")
    for i in range(0,m2):
        for j in range(0,n2):
            print("Enter value for", i+1, "*", j+1)
            mat2[i][j]=int(input())

    print("The sum of both the matrices is")
    for i in range(0,m1):
        for j in range(0,m2):
            print("Sum Of", i+1, "*", j+1, "element is")
            mat3[i][j]=mat1[i][j]+mat2[i][j]
            print(mat3[i][j])
