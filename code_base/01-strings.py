# Concatination of First 2 and last 2 elements of a string.

n=input("Enter a string: ")
x=n[0:2]
y=n[len(n)-2:]
n=x+y
print(n)