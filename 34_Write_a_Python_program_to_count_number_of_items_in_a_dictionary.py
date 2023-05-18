di={1:"ayush",2:"leo",3:[1,2,3,4],5:()}
count=0
for keys,val in di.items():
    if type(val)==list:
        count+=1
print(count)