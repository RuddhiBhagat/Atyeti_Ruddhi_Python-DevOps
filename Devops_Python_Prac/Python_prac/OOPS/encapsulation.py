#Variables which are made inside constructor are called as instance variable e.g self.pin self.balance.
#It is called as instance variable because its value changes as instance changes--object changes.
#When we do Ruddhi.pin -- it is accessible.So it won't happen it should be hidden right ? otherwise everyone will able to access it.
#Use self.__balance self.__pin --- check for objname.pin it will show error now
#If we set any value as self.__balance = "asdrfnjnj" -- it wont show you error it will execute. but it cant affect the code as all methods will use _Atm__balance

class Atm:
    # Constructor
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.menu()

    def set_pin(pin):
        self.pin = pin
        print("Pin changed")
    def get_pin():
        return self.pin
        

    def menu(self):
        user_input = 0
        while(user_input != "5"):
            user_input = input("""
                            Hello,how would you like to proceed?
                            1. Enter 1 to create pin
                            2. Enter 2 to deposit
                            3. Enter 3 to withdraw
                            4. Enter 4 to check balance
                            5. Enter 5 to exit
                        """)
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_bal()
            else:
                print("Thank you for using Atm")

    def create_pin(self):
        self.__pin = input("Enter new pin: ")
        print("Your pin set successfully")
        print("Please don't share your pin with anyone")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            new_amt = int(input("Enter Amount to be deposited"))
            self.__balance = self.__balance + new_amt
            print("Amount deposited successfully.")
        else:
            print("Invalid pin")
            
    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            with_amt = int(input("Enter Amount to be withdrawed: "))
            if with_amt <= self.__balance:
                self.__balance = self.__balance - with_amt
            else:
                print("Oops ! Insufficient balance...")
        else:
            print("Invalid pin")
    
    def check_bal(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            print(f"Total balance in your account is RS.{self.__balance}.")
        else:
            print("Invalid pin")

Ruddhi = Atm()
