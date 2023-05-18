inp=input("enter a string: ")
li=inp.split()
for i in li:
    x=len(i)
    if x%2==0:
        print("even length words in the given string are: ",i)