import csv
from tkinter import *
import time
topa=False
signupwindow=Tk()
signupwindow.title("signup Window")
signupwindow.geometry("600x600")
signupwindow.config(bg="black")

signupwindow.iconphoto(True,PhotoImage(file="loginpic (1).png") )
signupimage = PhotoImage(file="loginpic (2).png")
header = Label(signupwindow, text="sign up  \U0001F92B".title(), font=("Ariel", 19, "bold")
                   , fg="white", bg="grey", image=signupimage
                   , compound="left", width=450)
header.pack(anchor=N)
tag1 = Label(signupwindow, fg="white", bg="black", font=("Ariel", 19, "bold"), text="enter username:".title()).place(x=10, y=100)
username = Entry(tag1, fg="white", font=("Arial", 19, "italic"), bg="grey")
username.place(x=250, y=100)


tag2 = Label(signupwindow, fg="white", bg="black", font=("Ariel", 19, "bold"), text="enter password:".title()).place(x=10, y=150)
password = Entry(tag2,  fg="white", font=("Arial", 19, "italic"), bg="grey")
password.place(x=250, y=150)

signuplabel = Label(signupwindow, fg="white", bg="black", font=("Ariel", 12, "bold"),
                        text="create account:".title())
signuplabel.place(x=160, y=300)


def checker():
    if len(username.get())==0 or len(password.get())==0:
        alreadylabel = Label(signupwindow, text="you are required to fill all entries".title(), fg="red", bg="black",
                             font=("Ariel", 15, "bold"))
        alreadylabel.place(x=100, y=400)
    else:
        signinwriter()

def signinwriter():
    idlist=[]
    mainfile= open("signin.csv")
    file=csv.reader(mainfile)
    for i in file:
        idlist.append(i)
    if [username.get(),password.get()] not in idlist:
        with open("signin.csv","a",newline="\n") as file:

            file_writer=csv.writer(file)
            file_writer.writerow([username.get(),password.get()])
        alreadylabel = Label(signupwindow, text="account created succesfully \U0001F603".title(), fg="green", bg="black",
                             font=("Ariel", 15, "bold"))
        alreadylabel.place(x=100, y=400)
        time.sleep(2)
        signupwindow.destroy()
        global topa
        topa=True


    else:
        alreadylabel=Label(signupwindow, text="Sorry but account already exists!!\U0001F605".title(), fg="red", bg="black", font=("Ariel", 15, "bold"))
        alreadylabel.place(x=100,y=400)



signupbutton = Button(text="Sign Up", fg="blue", bg="black", activeforeground="red"
                          , command=checker, activebackground="black", font=("Ariel", 8, "bold"), padx=0, pady=0)
signupbutton.place(x=300, y=300)

signupwindow.mainloop()
if topa:
    import login