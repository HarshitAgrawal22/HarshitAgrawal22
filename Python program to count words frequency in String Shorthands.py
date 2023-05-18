st=input("enter the string: ")
res={key:st.count(key) for key in st.split()}
print(res)

dic={}
li=st.split()
for i in li:
    x=li.count(i)
    dic[i]=x
print(dic)