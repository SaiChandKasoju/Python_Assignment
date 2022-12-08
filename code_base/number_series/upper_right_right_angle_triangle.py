n=int(input("enter a value: "))
x=0
for i in range(0,n):
    for j in range(1,n-i+1):
        print(j,end=" ")
    x=x+2
    print("\n",end = " "*x)