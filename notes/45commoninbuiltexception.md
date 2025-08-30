# Common Built-in Exceptions in Python

Python provides several built-in exceptions that are raised when errors occur during program execution.  
Here are some of the most commonly encountered exceptions:

| **Exception**       | **Description**                                      |
|----------------------|------------------------------------------------------|
| `ZeroDivisionError` | Raised when dividing a number by zero.                |
| `ValueError`        | Raised when an invalid value is used (e.g., converting a string `"abc"` to `int`). |
| `TypeError`         | Raised when an operation or function is applied to an object of inappropriate type. |
| `IndexError`        | Raised when a list (or other sequence) index is out of range. |
| `KeyError`          | Raised when accessing a dictionary with a non-existing key. |
| `FileNotFoundError` | Raised when trying to open a file that does not exist. |
| `AttributeError`    | Raised when an invalid attribute reference is made (e.g., calling a non-existent method). |

---

✅ These exceptions can be handled using **try-except-finally** blocks to make your program more robust.
