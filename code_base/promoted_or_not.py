# code to find whether a student has promoted or not based on marks of s1, s2, s3.
# a student is promoted only when he got above 35 marks in all the three subjects.

s1=int(input("Marks in S1= "))
s2=int(input("Marks in S2= "))
s3=int(input("Marks in S3= "))
a, b, c=0,0,0
if s1>=35:
    if s2>=35:
        if s3>=35:
            c=1
        else:
            c=0
    else:
        c=0
else:
    c=0

if (c==1):
    print("Promoted")
else:
    print("Not promoted")