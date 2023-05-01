print("process started")
import os
try:
    for i in os.listdir(r"D:\devil name cry baby"):
        with open(f"D:\\devil name cry baby\\{i}","rb") as shitt:
            s=shitt.read()
        with open(f"C:\\Users\\Harshit Agrawal\\Downloads\\{i}","wb") as no :
            no.write(s)
except:
    print("no success")
else:
    print("did it")