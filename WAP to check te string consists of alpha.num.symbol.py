str_input=input("enter a string: ")
x=str_input.isalpha()
y=str_input.isdigit()
z=str_input.isascii()
if(x==True):
    print("string only consists alphabets ")
elif(y==True):
    print("string only consists digits ")
else:
    print("string constists symbol")
