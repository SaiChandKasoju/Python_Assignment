#to print n terms of fibonacci series in a list.
#to find the sum of n terns of fibonacci series.

def fib_series(n):
    first_value=0
    second_value=1
    li=[]
    for i in range(0,n+1):
        li.append(first_value)
        next_value=first_value+second_value
        first_value=second_value
        second_value=next_value
    print("List of fibonacci series: ", li)

def sum_of_fib(n):
    first_value=0
    second_value=1
    sum=0
    for i in range(0,n+1):
        sum=sum+first_value
        next_value=first_value+second_value
        first_value=second_value
        second_value=next_value
    print("Sum of n terms of fibonacci series = ", sum_of_fib(n))
def main():
    n=int(input("Enter a value: "))
    fib_series(n)
    #sum_of_fib(n)
if (__name__== "__main__"):
    main()