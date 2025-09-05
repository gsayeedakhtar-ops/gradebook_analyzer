class Transaction:
    def __init__(self, amount, category, t_type):
        self.amount = amount
        self.category = category
        self.t_type = t_type
    def __str__(self):
        return f"{self.t_type.capitalize()}: {self.amount} ({self.category})"

class ExpenseTracker:
    def __init__(self, owner):
        self.owner = owner
        self.transactions = []

    def add_transaction(self, amount, category, t_type):
        if amount <= 0:
            print("Amount must be positive.")
            return
        if t_type not in ["income", "expense"]:
            print("Transaction type must be 'income' or 'expense'.")
            return
        new_t = Transaction(amount, category, t_type)
        self.transactions.append(new_t)

    def show_summary(self):
        income = sum(t.amount for t in self.transactions if t.t_type == "income")
        expense = sum(t.amount for t in self.transactions if t.t_type == "expense")
        balance = income - expense
        return income, expense, balance
    def show_history(self):
        if not self.transactions:
            print(" No transactions yet.")
        else:
           print("\n--- Transaction History ---")
           for i, t in enumerate(self.transactions, start=1):
               print(f"{i}. {t}")
    def show_category_summary(self):
        categories = {}
        for t in self.transactions:
            categories[t.category] = categories.get(t.category, 0) + t.amount
        print("\n---category summary---")
        for cat, total in categories.items():
            print(f"{cat}: {total}")
            
    
tracker = ExpenseTracker("Sayeed")
tracker.add_transaction(30000, "Salary", "income")
tracker.add_transaction(7500, "Rent", "expense")
tracker.add_transaction(3500, "Food", "expense")
tracker.add_transaction(1780, "Travel", "expense")
tracker.add_transaction(1200, "Electricity", "expense")


income, expense, balance = tracker.show_summary()
print("\n---summary---")
print("Income:", income)
print("Expense:", expense)
print("Balance:", balance)
tracker.show_history()
tracker.show_category_summary()

        
