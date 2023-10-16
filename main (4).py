class Bank_Account:
    def __init__(self, account_number, account_name, account_balance):  
      self.__account_number = account_number
      self.__account_name = account_name
      self.__account_balance = account_balance
    def deposit (self,amount):
      if  amount > 0 :
        self.__account_balance += amount
        print(f"deposited:₹{amount}. current balance:₹{self.__account_balance}")
      else:
        print("Invaial deposit amount")
    def withdraw (self,amount):
      if amount > 0 and amount<=self.__account_balance :
        self.__account_balance -= amount
        print(f"withdraw:₹{amount}. current balance:₹{self.__account_balance}")
      else:
        print("Invalid withdraw amount")
        
    def display (self):
     print( f'account_balance of { self.__account_name }Rs.{ self.__account_balance}')
account=Bank_Account(123456,"Ramya",500)
account.deposit(1000)
account.withdraw(300)
account.display()