class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Your new balance with deposit: {self.balance}")
        else:
            print("Error")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawals may not exceed the available balance, because account cannot be overdrawn.")
        else:
            self.balance -= amount
            print(f"Your new balance with withdraw: {self.balance}")


account1 = Account("Kami", 500000)

account1.deposit(2000)
account1.withdraw(1900)

