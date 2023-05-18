
input_string=input("enter a string: ")
li1=str(input_string)
li=[]
for i in li1:
    x=input_string.count("i")
    li.append(x)
print(min(li))