#PATTERN TO PRINT DOLLAR PATTERN

n=int(input("Enter the value of n- "))
for i in range(2,n):
    print("$", end ="")

for i in range(0,n-1):
    print("$$")

for i in range(0,n):
    print("$", end="" )
