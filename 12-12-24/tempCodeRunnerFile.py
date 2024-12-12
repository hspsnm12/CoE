class Bank:
    acbal = 10000
    transaction = 0

    def validation(self, user_pin):
        pin = 1234
        return user_pin == pin

    def viewOptions(self):
        print("1. Deposit\n2. Withdraw\n3. Bal Enquiry\n0. EXIT\nChoose an option:")

    def performAction(self, inp):
        if inp == 1:
            depo = int(input("Enter amount to be deposited: "))
            self.deposit(depo)
        elif inp == 2:
            withdraw = int(input("Enter the amount to be withdrawn: "))
            self.amt_withdraw(withdraw)
        elif inp == 3:
            print("Account balance:", self.acbal)
        elif inp == 0:
            print("EXIT")
        else:
            print("Invalid option.")

    def deposit(self, depo):
        if depo % 100 == 0 and depo <= 50000:
            self.acbal += depo
            print("Transaction successful.\nAccount balance:", self.acbal)
        else:
            print("Transaction failed.")
            if depo % 100 != 0:
                print("Amount should be a multiple of 100")
            if depo > 50000:
                print("Max deposit amount is 50K")

    def amt_withdraw(self, withdraw):
        if (
            withdraw >= 100
            and withdraw % 100 == 0
            and withdraw < self.acbal
            and self.acbal - withdraw > 500
            and withdraw <= 20000
            and self.transaction <= 3
        ):
            self.acbal -= withdraw
            print("Transaction successful.\nAccount balance:", self.acbal)
            self.transaction += 1
        else:
            print("Transaction Failed.")
            if withdraw % 100 != 0:
                print("Amount should be a multiple of 100")
            if withdraw > self.acbal:
                print("Withdraw amount should be less than the account balance.")
            if self.acbal - withdraw < 500:
                print("Minimum balance should be 500")
            if withdraw > 20000:
                print("Per transaction max amount is 20K.")
            if self.transaction > 3:
                print("Only 3 transactions per day are allowed.")

obj = Bank()
print("Welcome to ABC bank")

count = 0
for count in range(3):
    user_pin = int(input("Enter the pin: "))
    if obj.validation(user_pin):
        while True:
            obj.viewOptions()
            inp = int(input("Enter the option: "))
            if inp == 0:
                obj.performAction(inp)
                break
            obj.performAction(inp)
        break
    else:
        count += 1
        if count < 3:
            print("Incorrect pin, try again.")
        else:
            print("Incorrect pin. You have reached the attempts limit.")
