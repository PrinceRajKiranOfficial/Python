"""
Encapsulation Example in Python
-------------------------------
This script demonstrates encapsulation by hiding the balance attribute
using a private variable and exposing controlled access through methods.
"""

# Class definition
class BankAccount:
    def __init__(self, balance):
        # private attribute
        self.__balance = balance

    def deposit(self, amount):
        # method to add amount to balance
        self.__balance += amount

    def get_balance(self):
        # getter method to access private balance
        return self.__balance


# Object creation
acct = BankAccount(1000)

# Using methods to interact with private data
acct.deposit(500)
print(acct.get_balance())  # Output: 1500
"""
Encapsulation Example in Python
-------------------------------
This script demonstrates encapsulation by hiding the balance attribute
using a private variable and exposing controlled access through methods.
"""

# Class definition
class BankAccount:
    def __init__(self, balance):
        # private attribute
        self.__balance = balance

    def deposit(self, amount):
        # method to add amount to balance
        self.__balance += amount

    def get_balance(self):
        # getter method to access private balance
        return self.__balance


# Object creation
acct = BankAccount(1000)

# Using methods to interact with private data
acct.deposit(500)
print(acct.get_balance())  # Output: 1500
