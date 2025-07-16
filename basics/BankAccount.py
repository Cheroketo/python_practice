class BankAccount:
    def __init__(self, name_owner, balance=0):
        self.name_owner = name_owner
        self.balance = balance

    def deposit(self, amount):
        self.balance -= amount

    def withdraw(self, amount):
        if self.balance < amount:
            print('Недостаточно средств')
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance