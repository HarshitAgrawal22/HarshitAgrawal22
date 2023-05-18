st=input("enter a string: ")
li=[]
s1=''
l=list(st)
for i in st:
    if i in li:
        li.append(st.replace("i","$"))
print(li)