# using_else_block.py
"""
Using Else Block in Exception Handling

In Python, the `else` block in a try-except statement executes 
only if no exception occurs in the try block.
"""

def divide_example():
    """Demonstrates the use of an else block with exception handling."""
    try:
        x = 10 / 2  # No exception here
    except ZeroDivisionError:
        print("❌ Error! Division by zero.")
    else:
        print(f"✅ Success! Result: {x}")


if __name__ == "__main__":
    divide_example()
