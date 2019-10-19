n=int(input("enter no of terms"))
sum=1
for i in range(2,n+1):
      f=1
      for j in range(i,i+1):
          f=f*j
      sum=sum+i/f
print("sum of series",sum)
