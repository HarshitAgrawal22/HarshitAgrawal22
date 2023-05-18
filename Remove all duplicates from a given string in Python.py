input_string=input("enter the string: ")
li=list(input_string)
li1=[]
for i in li:
    if i not in li1:
        li1.append(i)
print("".join(li1))