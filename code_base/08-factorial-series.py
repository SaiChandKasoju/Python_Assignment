#2!/1! +3!/2! +4!/3!+ ....+ (n+1)!/n! ?

num=int(input("enter a value=  "))
print(num)
sum=0
for i in range(1,num+1):
    f1=1
    for j in range(1,i+1):
        f1=f1*j
        print(f1)
        f2=1
        for k in range(1,j):
            f2=f2*k
            print(f2)
    x=(f1//f2)
    print(x)
    sum=sum+x
    print(sum)
print(sum-1)