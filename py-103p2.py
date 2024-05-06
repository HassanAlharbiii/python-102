import datetime
class BankAccount:
    def __init__(self):
        self.balance=0

    def deposit(self, amount):
        self.balance += amount
        self.print_transaction('Deposit ', amount)
        
    def withdraw(self, amount):
        if(self.balance <=0):
            print("sorry,there is no money in the account")
        else:
            if(self.balance>=0):
                self.balance -=amount
                self.print_transaction('Withdraw', amount)

            else:
                print('sorry, there is not enough money in the balance ')

    def check_balance(self):
        print("current balance :",self.balance)

    def print_transaction(self, function, amount):
        date= datetime.datetime.now().strftime("%Y-%M-%D %H:%M")
        print(f"{function}of {amount} function date at {date}")

user_account1= BankAccount()
user_account1.check_balance()

user_account1.deposit(100)
user_account1.deposit(100)
user_account1.check_balance()






        

