# raising_exception.py
"""
Raising Exceptions Manually in Python

This script demonstrates how to raise exceptions explicitly using `raise`.
Here, we check a user's age and raise a ValueError if the age is 18 or below.
"""

def check_age():
    """Prompts user for age and raises an exception if invalid."""
    age = int(input("Enter your age: "))

    if age <= 18:
        raise ValueError("❌ Access Denied: Age must be above 18.")
    else:
        print("✅ Access Granted.")


if __name__ == "__main__":
    try:
        check_age()
    except ValueError as e:
        print(e)
