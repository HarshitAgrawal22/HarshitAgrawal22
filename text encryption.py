
from random import shuffle
import string
import time
a=input("enter text to be encrypted")

l=" "+string.punctuation+string.digits+string.ascii_letters
ol=list(l)
shuffle(ol)

with open("encrpyt.txt","w") as file:
    file.write(str(ol))
final=""
for i in a:
    
    final+=str(ol[l.index(i)])
print("encrypted line:  ",final)
fil=""
for i in final:
    
    fil+=str(l[ol.index(i)])
print("encrypted line:  ",fil)

time.sleep(5)