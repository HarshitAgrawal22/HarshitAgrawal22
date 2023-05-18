num=int(input("enter the number: "))
r=0
n=num
x=len(str(num))
i=1
sum=0
while(num):
    r=num%10
    sum+=r**x
    num//=10
print(sum)
if n==sum:
    print("the number is armstrong")
else:
    print("the number is not armstrong")