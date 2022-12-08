# Code to remove duplicate elements in a string.

x=input("Enter a string: ")
n=1
for i in range(0,len(x)):
    for j in range(n,len(x)):
        if x[i]==x[j]:
            y=x.split()
    #print(n)
    n=n+1
print(y)
print(len(x))