num=int(input("enter the number: "))
li=[]
i=2
while i<=num:
    if num%i==0:
        li.append(i)
        num//=i
        
    else:
        i+=1
print(li)
