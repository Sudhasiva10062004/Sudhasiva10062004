class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number  # Private attribute
        self.__account_holder_name = account_holder_name  # Private attribute
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ${self.__balance}"

# Create an instance of the BankAccount class
account = BankAccount("123456789", "John Doe", 1000)

# Test deposit and withdrawal functionality
print(account.deposit(500))  # Deposited $500. New balance: $1500
print(account.withdraw(200))  # Withdrew $200. New balance: $1300
print(account.display_balance())  # Account balance for John Doe: $1300