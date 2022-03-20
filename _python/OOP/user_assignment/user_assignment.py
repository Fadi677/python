class User:
    def __init__(self, name, account_balance):
        self.name=name
        self.account_balance = account_balance
    
    def make_deposit(self,amount):
        self.account_balance+=amount
    def make_withdrawal(self,amount):
        self.account_balance-=amount
    def display_user_balance(self):
        print("User: "+self.name+" "+"Account Balance: "+str(self.account_balance))
    def transfer_money(self,user,amount):
        self.account_balance-=amount
        user.account_balance+=amount

mark=User("Mark",400)
mark.display_user_balance()
joe=User("joe",200)
joe.display_user_balance()
jane=User("jane",300)
jane.display_user_balance()

#Have the first user make 3 deposits and 1 withdrawal and then display their balance
mark.make_deposit(100)
mark.make_deposit(80)
mark.make_deposit(60)
mark.make_withdrawal(200)
mark.display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
joe.make_deposit(200)
joe.make_deposit(100)
joe.make_withdrawal(50)
joe.make_withdrawal(300)
joe.display_user_balance()

#Have the third user make 1 deposits and 3 withdrawals and then display their balance
jane.make_deposit(300)
jane.make_withdrawal(100)
jane.make_withdrawal(50)
jane.make_withdrawal(120)
jane.display_user_balance()

#Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
mark.transfer_money(jane,200)
mark.display_user_balance()
jane.display_user_balance()