st=input("enter a string: ")
sub_string=input("enter the substring: ")
ans=st.find(sub_string)

if ans>=0:
    print(f"the sub string is persent in the string and is present at index {ans+1}")
else:
    print("substring is not present in the string")