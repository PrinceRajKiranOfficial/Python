
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


def main():
    """Main function to run the bank account simulation."""
    print("\n🏦 Welcome to Prince's Bank 🏦")

    # --- Get Initial Balance ---
    try:
        init_balance = float(input("Enter initial balance to deposit: "))
        if init_balance < 0:
            print("Initial balance cannot be negative. Starting with $0.")
            init_balance = 0.0
        accn = BankAccount(init_balance)
    except ValueError:
        print("Invalid input. Starting with a default balance of $0.")
        accn = BankAccount(0.0)

    # --- Process Withdrawal ---
    try:
        wih_balance = float(input("Enter amount to withdraw: "))
        accn.withdraw(wih_balance)
    except ValueError:
        print("Invalid amount. Please enter a number.")

    # --- Display Final Balance ---
    print(f"💵 Final Balance: ${accn.get_balance():.2f}")
    print("🙏 Thank You for banking with us!")


if __name__ == "__main__":
    # The loop allows the user to perform multiple transactions without restarting the script.
    while True:
        main()
        
        # Ask user if they want to perform another transaction
        another_transaction = input("\nDo you want to perform another transaction? (yes/no): ").lower()
        if another_transaction != 'yes':
            break
