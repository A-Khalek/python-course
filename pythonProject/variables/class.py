class BankAccount:
    def __init__(self,account_name,balance = 0):
        self.account_name = account_name
        self.balance = balance


    def deposit(self,balance):
        self.balance += balance

    def withdraw(self,amount):
        if amount > self.balance:
            self.balance -= amount
        else:
            print('Insufficient funds')

    def display(self):
        print(self.account_name, self.balance)


bankAccount = BankAccount('Md.Abdul Khalek',1000)
bankAccount.deposit(10)
# bankAccount.display()
bankAccount.withdraw(90000)