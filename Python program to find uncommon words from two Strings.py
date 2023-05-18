input_string=input("enter the string: ")
input_string1=input("enter 2nd string: ")
li=input_string.split()
li1=input_string1.split()
li2=[]
for i in li:
    if i not in li1:
        li2.append(i)
for i in li1:
    if i not in li:
        li2.append(i)
print("uncommon words from two given strings are: ",li2)
