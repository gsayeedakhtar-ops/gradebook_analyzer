class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{self.owner} deposited {amount}. New balance = {self.balance}"
        return "Deposit must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"{self.owner} withdrew {amount}. New balance = {self.balance}"

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"


# Inheritance Example
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.03):
        super().__init__(owner, balance)   # inherit from BankAccount
        self.interest_rate = interest_rate

    # Polymorphism: redefine withdraw (limit per transaction)
    def withdraw(self, amount):
        if amount > 1000:
            return "Withdrawal limit exceeded! (Max 1000)"
        return super().withdraw(amount)

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied at {self.interest_rate*100}%. New balance = {self.balance:.2f}"


class CreditAccount(BankAccount):
    def __init__(self, owner, balance=0, credit_limit=500):
        super().__init__(owner, balance)
        self.credit_limit = credit_limit

    # Polymorphism: allow overdraft (negative balance up to limit)
    def withdraw(self, amount):
        if amount > self.balance + self.credit_limit:
            return "Credit limit exceeded!"
        self.balance -= amount
        return f"{self.owner} withdrew {amount}. New balance = {self.balance}"


# --- Testing ---
acc1 = SavingsAccount("Sayeed", 2000)
acc2 = CreditAccount("Faizan", 500)

print(acc1)
print(acc1.deposit(300))
print(acc1.withdraw(1200))   # should hit limit
print(acc1.withdraw(800))    # valid
print(acc1.apply_interest())
print(acc1, "\n")

print(acc2)
print(acc2.deposit(200))
print(acc2.withdraw(1000))   # allowed (credit used)
print(acc2.withdraw(2000))   # exceeds limit
print(acc2)
