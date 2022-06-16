class calc:

    def __init__(self):
        self.total=0
        self.menu()

    def menu(self):
        user_input = input(""" 
            enter 1 to add
            enter 2 to sub
            enter 3 to mult
            enter 4 to dividee
""" )

        if user_input == "1":
            self.__add__()
        elif user_input=="2":
            self.__sub__()
        elif user_input=="3":
            self.__mult__()
        elif user_input=="4":
            self.__divide__()
        else:
            print("exit from calculater, Bye!!")

    def __add__(self):
        add=int (input("enter a no. to add : "))
        b=int (input("enter a 2nd no. : "))
        c=add+b
        print("addition is : "+ str(c))

    def __sub__(self):
        sub=int(input("enter a no. to sub : "))
        b=int(input("enter a 2nd no. : "))
        c=sub-b
        print("addition is : "+ str(c))
        

    def __mult__(self):
        mult=int(input("enter a no. to mult : "))
        b=int(input("enter a 2nd no. : "))
        c=mult*b
        print("addition is : "+ str(c))
        

    def __divide__(self):
        div=int(input("enter a no. to div : "))
        b=int(input("enter a 2nd no. : "))
        c=div/b
        print("addition is : "+ str(c))
        


