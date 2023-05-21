with open("image path","rb")as image:
    i=image.read()
    fize=len(i)
    
with open("video path","rb") as movie:
    a=movie.read()

with open(r"size.txt","w")as file:
    file.write(str(fize))

with open(r"image.png","ab")as final:
    final.write(i)
    final.write(a)