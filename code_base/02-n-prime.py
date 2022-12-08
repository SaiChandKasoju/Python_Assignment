# This program helps us to find first n prime numbers.
# If we give 3 as input it should give first 3 prime numbers i.e., 2, 3, 5.

def n_prime(n):
    c=0
    for i in range(2,n*10):
        y=0
        for j in range(2,i):
            x=i%j
            if x==0:
                y=y+1
        if y<1:
            print(i,end=" ")
            c=c+1
        if c==n:
            break
def main():
    n=int(input("Enter a number= "))
    n_prime(n)
if (__name__=="__main__"):
    main()