""""
name=input("Your name")
age=input("Your age")
a=int(input("Marks in subject 1 out of 100"))
b=int(input("Marks in subject 2 out of 100"))
c=int(input("Marks in subject 3 out of 100"))
total=a+b+c
avg =(total)/3
if avg>=90:
    q="grade A+"
elif avg>=80:
    q="Grade A"
elif avg>=70:
    q="Grade B"
elif avg>=60:
    q="Grade C"
elif avg>=50:
    q="Grade D"
else:
    q="Grade E"
print("Name:", name,
      "Age:",age,
      "Total:",total,
      "Average:",avg,
      "Grade:",q)

for i in range(1,8,2):
    for j in range(1,i+2,2):
        print(j,end="")
    print()
"""
"""
import math
print("Enter coefficients")
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
if a==0:
    print("Value",a, "is 0")
    print("Aborting")
else:
    d=b*b-(4*a*c)
    if d>0:
        r1=(-b+ math.sqrt(d))/2*a
        r2=(-b- math.sqrt(d))/2*a
        print("Roots are real and unequal")
        print("Root 1 ",r1,"Root 2",r2)
    elif d==0:
        r1=-b/2*a
        print("Roots are real and equal")
        print("Root 1",r1,"Root 2",r1)
    else:
        print("Roots are complex and imaginary")
"""
"""
a=int(input("Enter number of fibonacci numbers"))
first=0
second=1
print(first)
print(second)
for i in range(1,a-1):
    third=first+second
    print(third)
    first=second
    second=third
"""

b=1
n=int(input("ENTER NTH POWER"))
x=int(input("Enter a integer"))
s=x
for i in range(2,n+1):
    b=b*i
    a=(x**n)/b
    s=s+a
print("SUM",s+1)
print('hello')
