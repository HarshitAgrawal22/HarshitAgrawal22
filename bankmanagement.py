"""========================================importing modules===================================================================================="""
import pandas as pd
import time
from colorama import Fore,Back,Style
import random
"""==================================================function creation===================================================================================="""
file=pd.read_csv("database.csv")
file.to_numpy()

namelist=list(file.loc[:,"Name"])
agelist=list(file.loc[:,"Age"])
codelist=list(file.loc[:,"Code"])
passwordlist=list(file.loc[:,"Password"])
phonelist=list(file.loc[:,"Phone"])
accountlist=list(file.loc[:,"Accounttype"])
balancelist=list(file.loc[:,"Balance"])



def filewriter():
    dict = {"Name": namelist, "Age": agelist,"Code":codelist,"Password":passwordlist,"Phone":phonelist,"Accounttype":accountlist,"Balance":balancelist}
    var = pd.DataFrame(dict)
    var.to_csv("database.csv")
def reseter():
    print(Style.RESET_ALL)


def checker():
    details=input(Fore.CYAN+"\n\nenter your code below\n->".title())
    reseter()
    if details in codelist:
        x=codelist.index(details)
        delay()
        print(file.loc[x,:],"\nso here are your details")
        editer(x)
    else:
        choice1=input("sorry but either you dont have an account or your entered code is wrong\nwould you like to try again(y/n)".title()).lower()
        if choice1=="y":
            checker()



def editer(x):
    choice2 = input("\n\ndo you want to edit any data (y/n)".title()).lower()
    if choice2=="y":
        a=file.loc[x,:]
        delay()
        print(a)
        correction=input("\n\nwhats the detail you want to change in your details \n 1.name\n2.age\n3.password\n4.phone number"
        "\nnote:1.we cant allow yo to have your own predefined code\n2.account type cant be changed, we would suggest you to close this account of yours and have a new one ".title())

        if correction=="1":
            newname=input(Fore.CYAN+"enter the new name you want to use".title()).title()
            reseter()
            namelist[x]=newname
            filewriter()
        elif correction=="2":
            newage=input(Fore.CYAN+"enter the age after correction".title())
            reseter()
            agelist[x]=newage
            filewriter()
        elif correction=="3":
            newpassword(x)
        elif correction =="4":
            phonelist[x]=int(input(Fore.CYAN+"enter the new mobile nuumber ".title()))
            reseter()


def newpassword(x):
    oldpassword = input("\n\nenter the old password just for safety purpose:".title())
    if passwordlist[x] == oldpassword:
        passwordlist[x] = input(Fore.CYAN+"enter the new password".title())
    else:
        print("sorry but we cant give access to this account".title())
        otherway=int(input(Fore.CYAN+"well you can login by your mobile number\nenter here->".title()))
        if otherway in phonelist:
            passwordlist[x]=input(Fore.CYAN+"enter the new password".title())

def getinfo(age):
    agelist.append(age)

    code=0
    while code in codelist:
        code =str(random.randint(0, 10000000))
    codelist.append(code)
    print(Fore.MAGENTA+"this is your code ->".title(),code)
    password = (input(Fore.MAGENTA+"enter your password but remember it".title()))
    passwordlist.append(password)
    phone=int(input(Fore.MAGENTA+"enter you phone number: "))
    phonelist.append(phone)
    balance=input(Fore.MAGENTA+"how much money would you like to credit in your account".title())
    balancelist.append(balance)
    delay()
    print(Fore.GREEN+"your account has been sucessfully created ".title())

    filewriter()

def currentaccount(name):
    print("\n\nyou can have this account but you will not get any kind of interest on this account and perform as many transactions as many you want".title())

    sure = input("want to continue (y/n)".title()).lower()

    if sure in "y":
        account="current"
        accountlist.append(account)
        namelist.append(name)
        agechecker()
    else:
        print("well you didnt want to continue so good bye \n have a nice day".title())


def agechecker():
    age = int(input("enter the age".title()))


    if (age < 18):
        print("sorry but you are not eligible to hold a account".title())
    else:
        getinfo(age)

def delay():
    print("\n\nLoading",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".",end="")
    time.sleep(1)
    print(".")
    time.sleep(2)



def savingaccount(name):
    print("\n\nyou are most welcome to have a saving account but you cant have more than 3 transactions in a month")
    sure=input("want to continue (y/n)".title()).lower()
    namelist.append(name)
    if sure in"y":
        account = "saving"
        accountlist.append(account)
        agechecker()
    else:
        print("well you didnt want to continue so good bye \n have a nice day".title())




def crediter(user):

    password=input("\n\nenter your password".title())
    if user in codelist:
        x=codelist.index(user)
        if password==passwordlist[x]:
            print(file.loc[x,:],"\nthis is your account details till now".title())
            money=int(input("enter the ammount of money you want to add in your account"))
            balancelist[x]=str(int(balancelist[x])+money)
            delay()
            print(money,"is been credited to your account successfully".title(),balancelist[x],"is the balance of your account".title())
        else:
            choice3=input("the entered password is wrong\n would you like to try again(y/n)".title())
            if choice3 in "Yy":
                crediter(user)
            else:
                print("well you didnt want to continue so good bye \n have a nice day".title())


    else:
        print("the code you entered is either wrong or you are a new user".title())


def debiter(user):
    password = input("\n\nenter your password".title())
    if user in codelist:
        x = codelist.index(user)
        if password == passwordlist[x]:
            print(file.loc[x, :], "\nthis is your account details till now".title())
            money = int(input("enter the ammount of money you want to debit from your account"))
            balancelist[x] = str(int(balancelist[x]) - money)
            delay()
            print(money, "is been debited to your account successfully".title(), balancelist[x],
                  "is the balance of your account".title())
        else:
            choice3 = input("the entered password is wrong\n would you like to try again(y/n)".title())
            if choice3 in "Yy":
                crediter(user)
            else:
                print("well you didnt want to continue so good bye \n have a nice day".title())


    else:
        print("the code you entered is either wrong or you are a new user".title())

def accountdeleter():
    user=int(input(Fore.RED+"\n\nenter the code of your account".title()))
    password = input(Fore.MAGENTA+"enter your password".title())
    if user in codelist:
        x = codelist.index(user)
        if password == passwordlist[x]:
            print(file.loc[x, :], "\nthis is your account details till now".title())
            listoflist=[namelist,agelist,codelist,passwordlist,phonelist,accountlist,balancelist]
            for i in listoflist:
                i.pop(x)
            delay()
            print(Fore.RED+"your account has been successfully deleted".title())
        else:
            choice3 = input("the entered password is wrong\n would you like to try again(y/n)".title())
            if choice3 in "Yy":
                crediter(user)
            else:
                print("well you didnt want to continue so good bye \n have a nice day".title())
    else:
        print("the code you entered is either wrong or you are a new user".title())









"""========================================main program===================================================================================="""
count=0

while(1):
    print(Fore.RED+"Time->"+str(time.asctime(time.localtime(time.time()))))
    count+=1
    if(count==1):
        task=input(Fore.MAGENTA+"what is it you want to do\n    1.create a new account\n    2.check an account info\n    3.credit money\n "
               "   4.debit money\n    5.delete a account\nenter here(index) ->".title()).lower()
        reseter()
    else:
        task = input(Fore.BLUE+
            "\n\n\nwhat you want to do\n    1.create a new account\n    2.check your account info\n    3.credit money\n "
            "   4.debit money\n    5.delete a account\n    6.exit bank\nenter here(index) ->".title()).lower()
        reseter()


    if(task=="1"):
        choice=input(Fore.YELLOW+"\n\nwhat kind of account you want to have\nA.current account\nB.saving account\nC.joint account".title()).upper()
        reseter()


        if(choice=="A"):
            name=input(Fore.BLUE+"enter your name:".title())
            currentaccount(name)


        elif(choice=="B"):
            name = input(Fore.BLUE+"enter your name:".title())
            savingaccount(name)

        elif(choice=="C"):
            person=input(Fore.BLUE+"enter the name of the first person".title())
            person2=input(Fore.BLUE+"enter the name of the second person".title())
            name=person+" and "+person2
            currentaccount(name)

    elif(task=="2"):
        checker()
    elif task=="3":
        user = int(input("\n\nenter the code of the account".title()))
        crediter(user)
    elif task=="4":
        user=int(input(Fore.RED+"\n\nenter the code of your account".title()))
        debiter(user)
    elif task=="5":
        accountdeleter()
    elif task=="6":
        break
        print("\n\nthankyou for using this bank\n have a nice day sir".title())


