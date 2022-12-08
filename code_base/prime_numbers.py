# code to find out whether a given number is a prime or not.

def is_prime(num):
    y=0
    for i in range(2,num):
        x=num%i
        if x==0:
            y=y+1
    if y>=1:
        print("The given number %d is not a prime number" %num)
    else:
        print("The given number %d is a prime number" %num)
def main():
    num=int(input("Enter a number = "))
    is_prime(num)
if (__name__=="__main__"):
    main()