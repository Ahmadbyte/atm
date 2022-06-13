class Atm:

    def __init__(self):
        #print("Hello")
        self.pin=""
        self.balance=0

        self.menu()

    def menu(self):
        user_input = input("""
            enetr 1 to enter pin
            enter 2 to deposit
            enter 3 to wdr
            enter 4 to check balance
            enter 5 to exit
""")

        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.wdr()
        elif user_input=="4":
            self.check_bal()
        elif user_input=="5":
            self.exit()
            #print("bye")    

    def create_pin(self):
        self.pin =input("Enter pin : ")
        print("Pin set succesful")

    def deposit(self):
        temp = input("enter your pin : ")
        if temp == self.pin:
            amount=int(input("eneter the amount to depost : "))
            self.balance = self.balance+amount
            print("account bal is : "+ str(self.balance))
        else:
            print("Invalid pin")

    def wdr(self):
        temp =input("enter your pin : ")
        if temp == self.pin:
            amount=int(input("eneter the amount to withdraw : "))
            if amount <= self.balance:
                self.balance = self.balance-amount
                print("remaining amount is : "+ str(self.balance))
            else:
                print("insufficient amount")
        else:
            print("Invalid pin")

    def check_bal(self):
        pin = input("enter the pin to check balance : ")
        if self.pin == pin:
            print("your account balance is : "+ str(self.balance))
        else:
            print("Wrong pin")

    def exit(self):
        self.exit=input("Enter 5 to exit : ")
        print("bye tc, have a good day!!")


        

