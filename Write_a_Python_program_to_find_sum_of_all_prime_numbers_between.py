n=int(input("enter the range: "))

li2=[]
for i in range(1,n+1):
    li=[]
    for j in range(1,n+1):
        if i%j==0:
            li.append(i)
    x=len(li)
    if x==2:
        li2.append(i)
sum=0
for i in li2:
    sum+=i
print(f"sum of prime numbers is {sum}")
