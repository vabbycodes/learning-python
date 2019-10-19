#CHECKING IF A NUMBER IS PRIME
n=0

for i in range(0,1000):
    s=n
    mult=0

    for i in range(0,n):
        check=n%(s)
        s=s-1
        if check==0:
             mult= mult + 1

    if mult==2:
        print(n, " - prime ")

    else:
        print(n, "*")
    n=n+1
