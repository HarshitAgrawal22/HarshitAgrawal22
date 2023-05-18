di={"a":1,"b":2,"c":4,"d":5}
print("count key value")
for count,(key,value) in enumerate(di.items(),1):
    print(count,"   ",key,"     ",value)
