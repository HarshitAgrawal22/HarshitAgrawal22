string1=input("enter the string: ")
str2=string1[::-1]
x=len(string1)
if string1==str2:
    print("string is palindrome")
else:
    print("not palindrome")
    
if(x%2==0):
    str1=string1[0:(len(string1)//2)]
    str3=string1[(len(string1)//2):len(string1)]
    if str1==str3:
        print("string is symmetrical")
    else:
        print("not symmetrical")
