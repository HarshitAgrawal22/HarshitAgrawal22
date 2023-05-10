import time
print("started")
movie=open(r"D:\anime movies\5 Centimetres Per Second [2007] [720p] [Dual] @Anime_Gallery.mkv","rb")
data=movie.read()
movie.close()
print("movie read")



textfile=open(r"C:\Users\Harshit Agrawal\Downloads\new.txt","w")
textfile.write(str(data))
textfile.close()
print("movie is texted")

encrypt=open(r"C:\Users\Harshit Agrawal\Downloads\new.txt","r")
data=eval(encrypt.read())
encrypt.read()
encrypt.close()
print("text is read")

final=open(r"C:\Users\Harshit Agrawal\Downloads\final.mp4","wb")
final.write(data)
final.close()
print("movie created again")


print((time.ctime(time.perf_counter)))