num=int(input("enter the number: "))
li=[]
sum=0
for i in range(1,num):
    if num%i==0:
        li.append(i)
for i in li:
    sum+=i
if sum==num
    print("perfect number")
else:
    print("not a perfect number")
