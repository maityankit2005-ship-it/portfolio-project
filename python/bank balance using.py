class Bank_account:
    def _init_(self, account_holder_name, balance):
        self.account_holder_name=account_holder_name
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")

account_1=Bank_account("Ankit Maity", 50000)
account_1.deposit(50)
account_1.withdraw(50000)