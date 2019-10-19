#CHECKING IF A NUMBER IS PRIME

n=int(input("Enter a number :"))
s=n
mult=0

for i in range(0,n):
    check=n%(s)
    s=s-1
    if check==0:
         mult= mult + 1

if mult==2:
    print(n, "is a prime number. ")

else:
    print(n, "is not a prime number.")
