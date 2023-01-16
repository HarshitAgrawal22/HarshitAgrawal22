tender=[]
container=[]
subcontainer=[]
a=int(input("enter the number of customers:".title()))
whines="whine"
for i in range(a):
    try:
        b= int(input(f"\n\n{i}th guy\n\nenter the number of whine this guy drinks:".title()))
        for j in range (b):
             if(whines!="!"):
                whines=input("enter the name of the drink else enter ! to get out of the loop:".title()).lower()
             else:
                break
             subcontainer.append(whines)
        container.append(subcontainer)
    except:
        print("looks like you enetered character the place of integer\U0001F604")


for i in container:
    for j in i:
        if(j not in tender):
            tender.append(j)
print("the drinks bartender is supposed to bring are ->",tender)