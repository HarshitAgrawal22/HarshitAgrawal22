num=int(input("enter the range : "))
r=0
for num in range(1,num+1):
    n=num
    x=len(str(num))
    sum=0
    while(num):
        r=num%10
        sum+=r**x
        num//=10

    if n==sum:
        print(n,end=" ")

