#REVERSE OF A NUMBER AND ADD ALL IT'S DIGITS

n=int(input("Enter The Number : "))
s=str(n)
sum=0
print("Reverse of", s, "is", s[::-1])
for i in range(0, len(s)):
    sum=sum+n%10
    n = ((n-(n%10))/10)
print("Sum of all the digits of", s, "is", int(sum))
