num=int(input("enter the number: "))
li=[]
for i in range(1,num+1):
    if num%i==0:
        li.append(i)
print(f"factors of {num} are ",li)
