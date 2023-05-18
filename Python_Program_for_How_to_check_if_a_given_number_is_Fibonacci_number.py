num=int(input("enter a number: "))
li=[]
a=0
b=1
c=0
for i in range(2,num+1):
    c=a+b
    a=b
    b=c
    li.append(c)
if num not in li:
    print("given number is not a fibonacci number")
else:
    print("entered number is a fibonacci number")
