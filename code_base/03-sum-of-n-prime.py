#Code to execute sum of first n prime numers.
# if the input is 3 the the output should be 2+3+5=10.

def sum_of_n_prime(num):
    c=0
    sum=0
    for i in range(2,num*10):
        y=0
        if c==num:
            break
        for j in range(2,i):
            x=i%j
            if x==0:
                y=y+1
        if y<1:
            print(i,end=" ")
            c=c+1
            sum=sum+i
    print("\nSum of first n prime numbers=",sum)
def main():
    num=int(input("enter a value: "))
    sum_of_n_prime(num)
if (__name__=="__main__"):
    main()