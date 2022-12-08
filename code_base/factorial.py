# Code to find the factorial of a number
#if n=5 then fact(n)=5*4*3*2*1==120

def factorial(n):
    fact=1
    i=1
    while i<=n:
        fact=fact*i
        i=i+1
    print("Factoral of the number n= ", fact)
def main():
    n=int(input("Enter a number = "))
    factorial(n)
if (__name__=="__main__"):
    main()