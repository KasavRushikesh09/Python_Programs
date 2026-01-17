class Account:
    def __init__(self,account_number,balanace):
        self.account_number = account_number
        self.balance = balanace

    def deposit(self,amount):
        self.balance +=amount
        print(f"Deposited ${amount}.New Balance: ${self.balance}")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"withdrawn ${amount}.Balance: ${self.balance}")
        else:
            print("Insufficient balance")
class SavingAccount(Account):
    def __init__(self,account_number,balance,min_balance = 1000):
        super().__init__(account_number,balance)
        self.min_balance = min_balance

    def withdraw(self,amount):
        if self.balance - amount >= -self.min_balance:
            self.balance -= amount
            print(f"withdrawn ${amount}.Balance:${self.balance}")
        else:
            print("withdrawal denied: Minimum balance required")
class CurrentAccount(Account):
    def __init__(self,account_number,balance,overdraft_limit=5000):
        super().__init__(account_number,balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self,amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance += amount

            print(f"withdrawn $P{amount}.Balance:${self.balance}")
        else:
            print("withdrawal denied: Overdraft limit exceeded")
accounts = [
    SavingAccount("SA829",50000),
    CurrentAccount("CK926",30000)
]
for acc in accounts:
    acc.withdraw(3000)