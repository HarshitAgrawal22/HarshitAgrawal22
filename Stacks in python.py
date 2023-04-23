stack = [i for i in range(10)]
while True:
    print("tasks are->\n 1.get the last item \n 2.add a item \n 3.get the whole stack \n4.delete the stack\n 5.check whether the stack is empty or not \n6.exit\n".title())
    try:
        user=int(input("enter task index here:".title()))
    except:
        print("sorry but invalid input brother".title())

    class stacker:

            def poper(harsh):
                try:
                    print(f"{stack.pop()} has been removed from the stack")
                except:
                    print(f"sorry something went wrong".title())
            def adder(harsh):
                try:
                    item = input("enter the item you want to add:".title())
                    stack.append(item)
                except:
                    print("something went wrong")
                else:
                    print(f"{item} was added to stack perfectly".title())

            def shower(harsh):
                print(stack)

            def deleter(harsh):
                try:
                    stack.clear()
                except:
                    print("stack cant be cleared")
                else:
                    print("stack was cleared nicely".title())

            def isempty(harsh):
                print("Yes") if (stack.__len__() == 0) else (print("stack contains some items"))


    stacker=stacker()

    dictator={1:stacker.poper,2:stacker.adder,3:stacker.shower,4:stacker.deleter,5:stacker.isempty}
    try:dictator[user]()
    except:print("invalid input")
