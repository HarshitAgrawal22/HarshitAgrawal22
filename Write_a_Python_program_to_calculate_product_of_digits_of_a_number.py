num=int(input("enter the num: "))
num1=list(str(num))
product=1
for i in num1:
    x=int(i)
    product+=x
print("product of the digit of the number is ",product)