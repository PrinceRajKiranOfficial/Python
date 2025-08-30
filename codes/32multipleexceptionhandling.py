# handling_multiple_exceptions.py
"""
Handling Multiple Exceptions in Python

This script demonstrates how to handle multiple exceptions using
try-except-finally blocks. It handles:
- ValueError: when a non-numeric input is entered
- ZeroDivisionError: when attempting to divide by zero
"""

def divide_numbers():
    """Prompts user for numerator and denominator, then divides with exception handling."""
    try:
        print("Welcome to the program!")
        num = float(input("Enter Numerator: "))
        denom = float(input("Enter Denominator: "))
        result = num / denom
        print(f"Result: {result}")

    except ValueError:
        print("❌ Invalid Input! Please enter numeric values only.")

    except ZeroDivisionError:
        print("❌ Error! Denominator cannot be zero.")

    finally:
        print("✅ Thank you for using the program!")


if __name__ == "__main__":
    divide_numbers()
