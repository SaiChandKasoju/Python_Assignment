n=int(input("Enter a number= "))
c=0
for i in range(2,1000):
    y=0
    for j in range(2,i):
        x=i%j
        if x==0:
            y=y+1
        if y<1:
            print(i,end="")
            c=c+1
    if c==n:
        break