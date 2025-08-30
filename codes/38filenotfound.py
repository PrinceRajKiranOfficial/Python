# file_exception_handling.py
"""
File I/O with Exception Handling in Python

This script demonstrates how to safely handle file operations
with exceptions such as:
- FileNotFoundError: when the file does not exist
- IOError: when an input/output error occurs while reading
"""

def read_file(filename):
    """Attempts to read a file and handle exceptions gracefully."""
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(content)

    except FileNotFoundError:
        print("❌ File not found. Please check the filename and try again.")

    except IOError:
        print("⚠️ I/O Error occurred while reading the file.")


if __name__ == "__main__":
    read_file("37hello.txt")
