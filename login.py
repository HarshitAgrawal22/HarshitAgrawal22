import csv
import random
from tkinter import *

loginwindow = Tk()


def reader():
    with open("signin.csv") as file:
        data = csv.reader(file)
        if [entry1.get(), entry2.get()] in data:
            loginwindow.destroy()
            import filecontroler

        else:

            Label(loginwindow, fg="red", bg="black", font=("Ariel", 15, "bold"),
                  text="you dont hold a account please signup \U0001F61E".title()).place(x=60, y=300)



loginwindow.title("Login Window")
loginwindow.geometry("600x600")
loginwindow.config(bg="black")
loginicon = PhotoImage(file="loginpic (1).png")
loginwindow.iconphoto(True, loginicon)
loginimage = PhotoImage(file="loginpic (2).png")
header = Label(loginwindow, text="sign in  \U0001F92B".title(), font=("Ariel", 19, "bold")
               , fg="white", bg="grey", image=loginimage
               , compound="left", width=450)
header.pack(anchor=N)
tag1 = Label(loginwindow, fg="white", bg="black", font=("Ariel", 19, "bold"), text="enter username:".title()).place(
    x=10, y=100)
entry1 = Entry(tag1, fg="white", font=("Arial", 19, "italic"), bg="grey")
entry1.place(x=250, y=100)
tag2 = Label(loginwindow, fg="white", bg="black", font=("Ariel", 19, "bold"), text="enter password:".title()).place(
    x=10, y=150)
entry2 = Entry(tag2, fg="white", font=("Arial", 19, "italic"), bg="grey")

loginbutton = Button(text="Sign in", fg="green", bg="black", activeforeground="red", command=reader,
                     activebackground="black", font=("Ariel", 12, "bold"), width=45).place(x=45, y=210)
entry2.place(x=250, y=150)
signuplabel = Label(loginwindow, fg="white", bg="black", font=("Ariel", 10, "bold"),
                    text="doesn't have a account?:".title())
signuplabel.place(x=150, y=400)

loginwindow.mainloop()