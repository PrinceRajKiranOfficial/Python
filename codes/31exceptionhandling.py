# exceptionhandling.py
"""
Exception Handling Example in Python

This script demonstrates how to handle runtime errors in Python using 
try-except-finally blocks. Specifically, it shows how to handle a 
ZeroDivisionError.
"""

def divide_numbers():
    """Performs a division operation with exception handling."""
    try:
        # Attempt division by zero (will raise ZeroDivisionError)
        x = 10 / 0
        print(f"Result: {x}")
    except ZeroDivisionError as e:
        print("Error: Division by zero is not allowed.")
        # Uncomment below to see the actual exception message
        # print(f"Exception details: {e}")
    finally:
        print("Thank you for using the platform!")


if __name__ == "__main__":
    divide_numbers()
