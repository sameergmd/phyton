class InsufficientFunds(Exception):
    pass

class Account:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance          # encapsulation

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amount
        print(f"Deposited {amount}. Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientFunds("Insufficient balance.")
        self.__balance -= amount
        print(f"Withdrew {amount}. Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

    def __del__(self):
        pass  # destructor

class SavingsAccount(Account):           # inheritance
    def __init__(self, acc_no, name, balance=0, rate=0.04):
        super().__init__(acc_no, name, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.get_balance() * self.rate
        self.deposit(interest)

acc = SavingsAccount(1001, "Asha", 5000)
try:
    acc.deposit(2000)
    acc.withdraw(1500)
    acc.add_interest()
    acc.withdraw(100000)
except (InsufficientFunds, ValueError) as e:
    print("Error:", e)
print("Final balance:", acc.get_balance())
