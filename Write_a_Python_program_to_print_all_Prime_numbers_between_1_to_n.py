n=int(input("enter the range: "))
y=0
x=1
for i in range(1,n+1):
   
    if x%i==0:
        y+=1
   
    if y==2:
        print(i)
    x+=1
   
