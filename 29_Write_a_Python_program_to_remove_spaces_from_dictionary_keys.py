di={"ayush singh":"name","22 09 2003":"birthday"}
d2={}
for key,value in di.items():
    d2.update({key.replace(" ",""):value})
print(d2)