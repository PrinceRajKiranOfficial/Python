# Exception Handling in Python

## 📌 What is an Exception?
- An **exception** is an event that disrupts the normal flow of a program's execution.  
- It typically occurs when the program encounters an error during runtime.  
- Exceptions are **unexpected events**. We cannot stop them completely, but we can provide **alternative ways** to handle them.  

### ⚠️ Example (Unhandled Exception)
```python
x = 10
y = 0
print(x / y)  # ZeroDivisionError
```
If not handled, exceptions cause the program to **crash**.

---

## 📌 Exception Handling in Python
Python provides the `try-except-finally` blocks to handle exceptions gracefully.

### ✅ Syntax
```python
try:
    # Code that may raise an exception
    risky_code()
except SomeException:
    # Code that runs if an exception occurs
    handle_error()
finally:
    # Code that always runs (optional)
    cleanup_code()
```

---

## 📌 Example 1: Division by Zero
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")
```

**Output (if input is 0):**
```
Error: Division by zero is not allowed.
Execution completed.
```

---

## 📌 Example 2: Handling Multiple Exceptions
```python
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numbers only.")
finally:
    print("Program finished.")
```

---

## 📌 The `finally` Block
- The `finally` block **always executes**, whether an exception occurs or not.  
- It is often used to **release resources** like closing files, database connections, or cleaning up memory.  

### Example
```python
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Closing file (if opened).")
```

---

## 🎯 Summary
- **Exception:** Unexpected event during program execution.  
- **Handling:** Done using `try-except-finally` blocks.  
- **finally block:** Always runs, useful for cleanup operations.  

👉 Exception handling makes programs **more robust and error-tolerant**.