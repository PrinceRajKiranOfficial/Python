# Reference Variables and Object Address in Python

In Python, **reference variables** are used to refer to objects created from a class. They act as a way to **host the object** and allow access to its attributes and methods.

## Key Points
- A reference variable stores the **address of the object** in memory.
- Multiple reference variables can point to the same object.
- Reference variables allow interaction with the object’s data and behavior.

## Example: Creating a Reference Variable
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating object with reference variable
s1 = Student("Prince", 20)

print("Reference variable s1 is hosting object:", s1)
```

**Output (example):**
```
Reference variable s1 is hosting object: <__main__.Student object at 0x7f9b1c2e5d90>
```
Here, `s1` is the **reference variable** that stores the memory address (`0x7f9b1c2e5d90`) of the object.

---

## Example: Multiple References to the Same Object
```python
s2 = s1  # Both s1 and s2 refer to the same object
print("s1:", s1)
print("s2:", s2)
```

**Output:**
```
s1: <__main__.Student object at 0x7f9b1c2e5d90>
s2: <__main__.Student object at 0x7f9b1c2e5d90>
```
Both `s1` and `s2` point to the same memory address, meaning they reference the **same object**.

---
✅ **Summary**: A reference variable in Python stores the address of an object and provides access to its attributes and methods. Multiple reference variables can point to the same object.
