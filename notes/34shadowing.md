# Variable Shadowing in Python

In Python, **shadowing** occurs when a local variable in a function or method has the **same name** as a global variable. In such cases, the **local variable takes priority** within its scope.

## Key Point
- If a **global** and **local** variable share the same name, the **local variable is used** inside the function.
- This can sometimes cause confusion or bugs if not handled carefully.

## Example
```python
x = 10  # Global variable

def my_function():
    x = 5  # Local variable (shadows the global one)
    print("Inside function, x =", x)

my_function()
print("Outside function, x =", x)
```

**Output:**
```
Inside function, x = 5
Outside function, x = 10
```

Here, the local variable `x = 5` **shadows** the global variable `x = 10` inside the function.

---

## Accessing Global Variable Explicitly
If you still want to access or modify the global variable, use the **`global` keyword**.

```python
x = 10  # Global variable

def my_function():
    global x
    x = 5  # Modifies the global variable
    print("Inside function, x =", x)

my_function()
print("Outside function, x =", x)
```

**Output:**
```
Inside function, x = 5
Outside function, x = 5
```

---
✅ **Summary**: When local and global variables have the same name, the **local variable shadows the global one** within the function's scope. Use the `global` keyword to explicitly work with the global variable.
