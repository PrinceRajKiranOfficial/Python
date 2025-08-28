# `__init__` Method in Python

In Python, `__init__` is a **constructor method** in classes.

## Key Points
- It is automatically called when an object is created from a class.
- It allows the class to initialize its attributes.
- Used to set up the initial state of an object.
- With `__init__`, we can initialize the **`self` attributes** (instance variables).

## Example
```python
class Person:
    def __init__(self, name, age):
        # initializing attributes using self
        self.name = name      
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Creating an object automatically calls __init__
p1 = Person("Alice", 25)
p1.introduce()
```

**Output:**
```
Hi, my name is Alice and I am 25 years old.
```

---
✅ **Summary**: `__init__` is a special constructor method that runs automatically when an object is created. It initializes the object's attributes using `self`.
