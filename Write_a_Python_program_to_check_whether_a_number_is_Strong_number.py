num=int(input("enter the number: "))

n=num
r=0
sum=0
while(num):
    i=1
    fac=1
    r=num%10
    while(i<=r):
        fac*=i
        i+=1
    sum+=fac
    num//=10
print(sum)
if sum==n:
    print("stong number")
else:
    print("not a strong number")