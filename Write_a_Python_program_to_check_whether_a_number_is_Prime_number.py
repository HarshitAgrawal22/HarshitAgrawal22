num=int(input("enter the number: "))
li=[]
x=2
for i in range(1,num+1):
    if num%i==0:
        li.append(i)
if len(li)==x:
    print("given number is prime")
else:
    print("number is not prime")