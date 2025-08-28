# Encapsulation in Python

**Encapsulation** is one of the core principles of Object-Oriented Programming (OOP). It hides the internal data of an object and exposes only what is necessary, ensuring better security and control.

## Key Points
- Encapsulation hides internal details (data) and shows only the required functionality.
- It prevents direct modification of object data from outside the class.
- Achieved using:
  1. **Private attributes** (by prefixing with `__`)
  2. **Getter and Setter methods** to access and update private attributes safely.

---

## Encapsulation in Java vs Python
- In **Java**, both **setters and getters** are commonly used to achieve encapsulation.
- In **Python**, **getters are essential** to read private attributes, but **setters are optional**. You can directly update attributes or use setters if extra validation is required.

---

## Example: Encapsulation in Python
```python
class BankAccount:
    def __init__(self, balance):
        # private attribute
        self.__balance = balance

    # Getter method (compulsory in Python to access private data)
    def get_balance(self):
        return self.__balance

    # Setter method (optional in Python)
    def set_balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = amount


# Creating an object
account = BankAccount(1000)

# Accessing balance using getter
print("Current Balance:", account.get_balance())

# Updating balance using setter (optional)
account.set_balance(1500)
print("Updated Balance:", account.get_balance())
```

**Output:**
```
Current Balance: 1000
Updated Balance: 1500
```

---
✅ **Summary**: Encapsulation is used to hide internal data. In **Java**, setters and getters are required, while in **Python**, **getters are necessary** to access private data but setters are **optional**.
