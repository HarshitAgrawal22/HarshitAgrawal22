num=int(input("enter a number: "))
st=str(num)
x=len(st)
sum=0
n=num
i=0
while(i!=x):
    r=num%10
    sum=sum*10+r
    num=num//10
    i+=1
if n==sum:
    print("number is palindrome")
else:
    print("number is not palindrome")