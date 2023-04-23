from tkinter import *
import os
from tkinter import filedialog
import psutil





def main():
    window = Tk()
    folderimage=PhotoImage(file="folder.png")
    icon = PhotoImage(file="fileicon.png")
    createicon = PhotoImage(file="create.png")
    moveicon = PhotoImage(file="move.png")
    copyicon = PhotoImage(file="copy.png")
    deleteicon = PhotoImage(file="delete.png")
    openicon = icon
    searchicon = PhotoImage(file="search.png")
    sendicon = PhotoImage(file="send.png")
    ideaicon = PhotoImage(file="idea.png")

    def Path(entry):
        global path
        path = (entry.get()+"://")


    def filedial():
        filepath=filedialog.askopenfilename(title="open file".title(),filetypes=(("all files","*.*"),("txt files","*.txt")))
        print(filepath)


    class worker:
        def __init__(self, title, windowname, command, icon):
            self.window = Toplevel()
            self.window.title(windowname.title())
            self.window.geometry("500x600")
            self.window.config(bg="black")

            self.label = Label(self.window, text=title.title(), image=icon, compound="right",
                               font=("Ariel", 20, "bold"), width=450, fg="white", bg="grey")
            self.label.pack()

            self.label2 = Label(self.window, text="enter file name here:".title(), bg="black", fg="white",
                                font=("Ariel", 15, "bold"))
            self.label2.place(x=10, y=100)



            self.entry1 = Entry(self.window, fg="black", font=("Arial", 15, "italic"))
            self.entry1.place(x=230, y=100)



            self.label3=Label(self.window,text="Enter the drive here:".title(),bg="black",fg="white",font=("Ariel",15,"bold"))
            self.label3.place(x=10,y=200)



            self.entry2=Entry(self.window,fg="black",font=("Ariel",15,"italic"))
            self.entry2.place(x=230,y=200)

            Label(self.window,text="{case sensetive}".title(),font=("ariel",10,"bold"),bg="black",fg="white").place(x=245,y=170)



            Button(self.window,bg="black",fg="purple",font=("Ariel",12,"bold"),text="choose manually".title(),command=filedial ,activebackground="black").place(x=100,y=250)

            Button(self.window, fg="purple", bg="black", text="submit entries".title(), activeforeground="purple",
                            activebackground="black", command=lambda:command(self.entry1,self.entry2,self.window), font=("Ariel", 12, "bold")).place(x=300,y=250)





    def theone(name,directory):
        print(os.path.join(directory,name,))


    class fileentry:
        def __init__(self, entry, directory, windowname,path):


            for file in directory:
                if entry.get().casefold() == file.casefold():

                    label2 = Label(windowname, text="found your searched item             ".title(), bg="black", fg="grey",
                                   font=("Ariel", 10, "bold"))
                    label2.place(x=150, y=150)


                    Button(windowname, text="hallelujah bro use me".title(), font=("Ariel", 12, "italic"),
                           activeforeground="red",
                           activebackground="black", command=lambda:theone(file,path)).place(x=200, y=450)

                    break


                elif file.casefold().startswith(entry.get().casefold()) or entry.get() in file.casefold():
                    label2 = Label(windowname, text=f"are you looking for {file}            ".title(), bg="black", fg="grey",
                                   font=("Ariel", 10, "bold"))
                    label2.place(x=150, y=150)

                    Button(windowname,text="if yes then use me".title(),font=("Ariel",12,"italic"),activeforeground="red",
                            activebackground="black", command=lambda:theone(file,path)).place(x=200, y=450)

                    break


            else:

                    label2 = Label(windowname, text="item not present here           ".title(), bg="black", fg="grey",
                                   font=("Ariel", 10, "bold"))
                    label2.place(x=150, y=150)







    def windower(entry,entry2,window):
        Path(entry2)

        winder=fileentry(entry,os.listdir(path),window,path)



    def writer(entry,window):
        with open("review.txt", "a") as file:

            file.write(entry + "\n")
        Label(window, text="thankyou for your review".title(), bg="#494d08", fg="green",
              font=("Ariel", 15, "bold")).place(x=175, y=550)





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







    def assigner(task):
        if task.get() == "0":  # delete
            deleter=worker("choose the file to delete","delete window", windower,deleteicon)




        elif task.get() == "1":  # saerch

            search = worker("enter the name", "search window", windower, searchicon)


        elif task.get() == "2":  # move

            movewindow = worker("choose the file to move", "move window", windower, moveicon)
        elif task.get() == "3":  # copy

            copywindow = worker("choose the file to copy", "copy window", windower, copyicon)
        elif task.get() == "4":  # send

            sendwindow = worker("select the file to send", "send window", windower, sendicon)
        elif task.get() == "5":  # open
            openwindow = worker("select the file to open", "idea window", windower, openicon)






        elif task.get() == "6":  # new idea

            reviewwindow = Toplevel()
            Label(reviewwindow, compound="left", text="thankyou for your review".title(),
                  fg="white", bg="grey", image=ideaicon, width=450,
                  font=("Ariel", 19, "bold",)).pack()
            reviewwindow.geometry("600x600")
            reviewwindow.config(bg="#494d08")
            Label(reviewwindow, text="enter here:".title(), font=("Ariel", 15, "bold"), bg="#494d08").place(x=20, y=100)


            entry = Text(reviewwindow,bg="light yellow",font=("Ariel","15","italic"),width=30,height=17)
            entry.place(x=140, y=100)


            button = Button(reviewwindow, fg="green", bg="black", text="submit", activeforeground="red",
                            activebackground="black", command=lambda: writer(entry.get("1.0",END),reviewwindow), font=("Ariel", 12, "bold"))

            button.place(x=40, y=200)




        elif task.get() == "7":  # create

            creater = worker("enter the name", "creater window", windower, createicon)



#______________________________________________________________________________________________________________________________________________________________________________________________________________




    cpu_count=os.cpu_count()

    memorystats=psutil.virtual_memory()

    Label(window,text=f"your pc have {cpu_count} threads \nand \n{((memorystats[1]//1024)//1024)} MB available ram\n\n\n\n\n i would recommend you\n to run maximum \n {cpu_count//2}"
                      f" tasks at a time \n this code is for learning\n purpose please dont \ntorture it  ".title(),
          font=("Ariel", 10, "bold",),fg="red", bg="black").place(x=250,y=100)

    window.title("File Handler")
    window.iconphoto(True, icon)

    window.config(bg="black")


    imagelist = [deleteicon, searchicon, moveicon, copyicon, sendicon, openicon, ideaicon, createicon]


    namelist = ["DeleteFile", "SearchFile", "MoveFile", "CopyFile", "SendFile", "OpenFile", "A new idea", "createfile"]

    task = StringVar()
    Label(window,text="Welcome SIR \U0001F60E", font=("Ariel", 19, "bold",), fg="white", bg="grey", image=icon,
                  compound="left", width=450).pack()

    for i in namelist:
        commandlist = Radiobutton(window, bg="grey", font=("constantia", 15), height=56,
                                  width=200, text=i, variable=task, command=lambda: assigner(task)
                                  , value=namelist.index(i), indicatoron=False,
                                  fg="white", image=imagelist[namelist.index(i)], compound="left")
        commandlist.pack(anchor=W)


    window.mainloop()



main()





