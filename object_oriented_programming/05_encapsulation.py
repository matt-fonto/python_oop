class Account:
    def __init__(self, balance):
        self._balance = balance

    @property # get
    def balance(self):
        return self._balance

    # every time we call self.balace = <value>, we will be using the setter internally
    @balance.setter # set
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def deposit(self, amount):
        self.balance += amount # use setter
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount # setter
        return self.balance

account = Account(100)

# account._balance = 150 # it won't work
print(account.deposit(50)) # 100 + 50 = 150
print(account.withdraw(120)) # 150 - 120 = 30