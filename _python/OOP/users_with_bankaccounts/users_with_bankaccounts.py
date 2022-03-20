class User:
    def __init__(self, name, account_number):
        self.name=name
        self.account=BankAccount(account_number,int_rate=0.0, balance=0)
    
    def make_deposit(self,amount):
        self.account.balance+=amount
    def make_withdrawal(self,amount):
        self.account.balance-=amount
    def display_user_balance(self):
        print("User: "+self.name)
        print("The is the account info:"),self.account.display_account_info()
    def transfer_money(self,user,amount):
        self.account.balance-=amount
        user.account.balance+=amount

class BankAccount:
    def __init__(self, account_number,int_rate=0.01, balance=0):
        self.account_number=account_number
        self.int_rate= int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        self.balance-=amount
        return self
    def display_account_info(self):
        print("account number: ",self.account_number,"intereset rate: ",self.int_rate,"account balance: ",self.balance)
    def yield_interest(self):
        if self.balance>0:
            self.balance= self.balance + (self.balance*self.int_rate)
        else: 
            self.balance += 0
        return self

mark=User("Mark",222)
mark.account.display_account_info()
mark.display_user_balance()
joe=User("joe",333)
joe.account.display_account_info()
jane=User("jane",444)
jane.account.display_account_info()