
while True:
    def completer(a, o, rang,start):
        if a == "v":
            if o == "f":
                for i in range(start, rang):
                    print(i)
            elif o == "r":
                for i in range(rang, start, -1):
                    print(i)
            else:
                print("try again option are f and r only")
                inputer()
        elif a == "h":
            if o == "f":
                for i in range(start, rang):
                    print(i, end=" ")
            elif o == "r":
                for i in range(rang, start, -1):
                    print(i, end=" ")
            else:
                print("try again option are f and r only")
                inputer()

        else:
            print("options are v and h only ")
            inputer()
    def powerrangers(start,rang):
        for i in range(start,rang,-1):
            print(i)

    def inputer():

        a = input("enter here from {v}or {h}\U0001F601:")
        o = input("enter the way you want to print it{f} or {r}\U0001F604:")
        start=input("enter the starting point\U0001F606")
        rang = input("enter the ending point\U0001F607")
        checker(a, o, rang,start)


    def checker(a, o, rang,start):
        if (a.isdigit() or o.isdigit() or rang.isalpha() or start.isalpha()):
            print("sorry but invalid input\n try again".title())
            inputer()
        else:
            rang,start= int(rang),int(start)
            if start>rang:
                print(("hmm,playing games\U0001F605"))
                powerrangers(start,rang)

            completer(a, o, rang,start)


    inputer()



