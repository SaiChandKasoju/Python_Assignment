n=int(input("enter a value: "))
n=n+1
for i in range(1,n):
    if i<=(n//2):
        print(i,end=" ")
    else:
        print(n-i,end=" ")