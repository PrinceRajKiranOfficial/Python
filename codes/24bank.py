"""
Encapsulation with Withdraw Example
-----------------------------------
This script demonstrates encapsulation by:
1. Using a private attribute (__balance).
2. Allowing controlled access through deposit, withdraw, and getter methods.
3. Handling insufficient funds with validation.
"""

class BankAccount:
    def __init__(self, balance):
        """Initialize the bank account with a private balance."""
        self.__balance = balance  # private attribute

    def withdraw(self, amount):
        """Withdraw money if sufficient balance is available."""
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrawal successful! Amount: {amount}")
        else:
            print(
                """❌ Insufficient funds ❌
Please deposit money to continue withdrawing.
This is not your father's bank. 
Deposit money before withdrawing. 💰"""
            )

    def get_balance(self):
        """Return the current balance."""
        return self.__balance


# Main Program
if __name__ == "__main__":
    while True:
        print("\n🏦 Welcome to Prince's Bank 🏦")
        init_balance = float(input("Enter initial balance: "))
        accn = BankAccount(init_balance)

        wih_balance = float(input("Enter withdraw amount: "))
        accn.withdraw(wih_balance)

        print("💵 Final Balance:", accn.get_balance())
        print("🙏 Thank You, Visit Again!")
