num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
print(f"before swaping num1 is {num1} and num2 is {num2}")
num1=num1^num2
num2=num1^num2
num1=num1^num2
print(f"after swaping num1 is {num1} and num2 is {num2}")