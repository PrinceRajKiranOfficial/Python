# file_operations.py
"""
File Handling in Python

This script demonstrates different file handling operations such as:
- Reading from a file
- Writing to a file
- Appending to a file
- Creating a new file
- Checking if a file exists
- Removing and renaming files
- Using the `with` statement for safe file handling
"""

import os

def read_file():
    """Reads and prints content from an existing file."""
    with open("35prince35.txt", "r") as file:
        content = file.read()
        print(content)


def write_file():
    """Writes text into a file (overwrites if file already exists)."""
    with open("35prince35.txt", "w") as file:
        file.write("Hello, this is going to be fun!")


def append_file():
    """Appends text at the end of the file."""
    with open("35prince35.txt", "a") as file:
        file.write("\nDid you have enough fun?\n")


def create_file():
    """Creates a new file. Fails if file already exists."""
    with open("37hii.txt", "x") as file:
        pass


def check_file_exists():
    """Checks if a file exists."""
    return os.path.exists("37hii.txt")


def remove_file():
    """Deletes a file if it exists."""
    if os.path.exists("37hii.txt"):
        os.remove("37hii.txt")
        print("File removed successfully!")
    else:
        print("File does not exist.")


def rename_file():
    """Renames a file if it exists."""
    if os.path.exists("37hii.txt"):
        os.rename("37hii.txt", "37hello.txt")
        print("File renamed successfully!")
    else:
        print("File does not exist.")


if __name__ == "__main__":
    # Example flow:
    write_file()        # Write data
    append_file()       # Append data
    read_file()         # Read data
    print("File exists?", check_file_exists())
    # remove_file()     # Uncomment to delete file
    # rename_file()     # Uncomment to rename file
