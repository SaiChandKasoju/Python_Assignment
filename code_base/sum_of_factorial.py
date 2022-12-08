
def sum_of_factorial(num):
    sum=0
    for i in range(1,num+1):
        fact=1
        for j in range(1,i+1):
            fact=fact*j
        sum=sum+fact
    print("Sum of series of factorials = %d" %sum)
def main():
    num=int(input("enter a value=  "))
    sum_of_factorial(num)
if (__name__=="__main__"):
    main()