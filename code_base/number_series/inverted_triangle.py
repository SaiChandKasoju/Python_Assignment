# if input is 3 an inverted triangle is formed as mentioned below
#   1 2 3 
#    1 2
#     1
def inverted_triangle(n):
    for i in range(0,n):
        for j in range(1,n-i+1):
            print(j,end=" ")
        print("\n",end=" "*(i+1))
def main():
    n=int(input("enter a value: "))
    inverted_triangle(n)
if (__name__=="__main__"):
    main()