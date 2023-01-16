#=============================================================================================================importing modules and libraries===================================================================================
import time
import csv
from colorama import Fore,Back,Style
#=============================================================================================================file handling========================================================================================================
list=[]
with open ('words.csv') as file:
    words=csv.reader(file)
    for word in words:
        list.append(word)
time.sleep(5)
#============================================================================================================functions creation==========================================================================================================

def para(paragraph):
    if (paragraph.endswith(".")):
            sen = (paragraph.replace(".", " .")).split(".")
            sen.remove('')

            for line in sen:
                line = line.split()
                for word in line:
                    print(Fore.CYAN + word, end=" ")
                print("\n")
                checker(line)
    else:
            print(Fore.RED + "heyy it looks like you forgot to put full stop at the end \U0001F631".title())


def finalle():

    print(Fore.CYAN + "\nthis is a basic code perform sentimental analysis ,so me and my group is working on it to make it better. ".title())
    print("\nwe are thankful for you using our code we wish to better it by the coming months\n have a great day sir".title())


def checker(sen):
    n=p=0
    for value in list:
        for j in sen:
            if (value[2] == j):
                p += 1
            elif (value[1] == j):
                n += 1
    if (n > 0):
        print(Fore.RED + "your entered sentence seems to be negative\t\U0001F622".title())
        print(Style.RESET_ALL)
    elif (p > 0):
        print(Fore.GREEN + "your entered sentence seems to be positive\t\U0001F604".title())
        print(Style.RESET_ALL)
    else:
        print(Fore.BLUE + "your sentence seems too be neutral\t\U0001F9D0".title())
        print(Style.RESET_ALL)
#============================================================================================================main program==========================================================================================================
c=0
print("good morning sir \nwelcome to our group project:\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tcreated by->Harshit Agrawal\n".title(),"\t\t\t\t\t\t\t\t\t\U0001F642<-sentimental analysis->\U0001F643".upper())
print("\t\t\t\t\t\t\t\t\t____________________________")

while(True):
        print(Fore.MAGENTA + "\nhow would you like to enter the data".title())
        choice = input("1.paragraph\n2.line\nenter here:")

        if(choice=="1"):
            c+=1
            if (c == 1):
                paragraph = input(Fore.YELLOW + "\n\nenter the paragraph here:".title()).lower()
                para(paragraph)


            else:
                paragraph = input(Fore.YELLOW + "\n\nif you want to exit then press '!' else \nyou can enter the paragraph here:".title()).lower()
                if (paragraph == "!"):
                    finalle()
                    break
                else:
                    para(paragraph)







        elif(choice=="2"):
            c+=1
            print(Fore.MAGENTA + "\t\n<please remember to put a full stop(.) at end of the sentence>\n".title())
            if(c==1):

                sentence = input(Fore.YELLOW+"Enter your sentence here:".title()).lower()
                print(Style.RESET_ALL)

            else:

                sentence = input(Fore.YELLOW+"\n\nif you want to continue then\nenter the sentence below \nelse enter '!' -> ".title()).lower()
                print(Style.RESET_ALL)
                if(sentence=="!"):
                    finalle()
                    break



            sentence=sentence.replace("."," .")
            with open("database.txt", 'a') as file2:
                file2.writelines(sentence)

            if(sentence.endswith(".")):
                sen=sentence.split()
                checker(sen)
            else:
                print(
                    Fore.RED + "sorry but it looks like you forget to put fool stop at the end of your sentence.".title())
                print(Style.RESET_ALL)
