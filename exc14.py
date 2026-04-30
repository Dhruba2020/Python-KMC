class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []   

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
            print("Deposit successful")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print("Withdrawal successful")
        else:
            print("Insufficient balance or invalid amount")

    def display(self):
        print("\n--- Account Details ---")
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Transactions:", self.transactions)


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)   # constructor chaining
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        self.transactions.append(f"Interest added: {interest}")
        print("Interest added successfully")


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, reward_points):
        super().__init__(account_number, balance, interest_rate)
        self.reward_points = reward_points
        self.minimum_balance = 500   

    def redeem_points(self):
        if self.reward_points > 0:
            print(f"Redeemed {self.reward_points} points")
            self.transactions.append(f"Redeemed points: {self.reward_points}")
            self.reward_points = 0
        else:
            print("No points to redeem")

   
    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("Cannot withdraw: Minimum balance must be maintained")
        elif amount > 0:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print("Withdrawal successful (Premium Account)")
        else:
            print("Invalid amount")

    def display(self):
        super().display()
        print("Reward Points:", self.reward_points)