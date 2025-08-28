# Class and Object in OOP

Understanding **Class** and **Object** is fundamental in Object-Oriented Programming (OOP).

## Class
- A **class** is a blueprint, prototype, or template for creating objects.
- It defines attributes (data) and behaviors (methods).
- A class itself does not occupy memory until objects are created from it.

**Example:**
```python
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, my name is {self.name}.")
```

## Object
- An **object** is a real-world entity created from a class.
- It is an instance of a class and **does occupy memory**.
- Every object has two parts:
  1. **Has** → Properties (variables)
  2. **Does** → Behaviors (functions/methods)

**Example:**
```python
prince = Person("Prince")
prince.introduce()  # Output: Hi, my name is Prince.
```

### Breaking down the example:
- **Has (properties/variables):** `name`
- **Does (behaviors/methods):** `introduce()`

Real-world analogy:
- **Prince has name** → "Prince"
- **Prince does dishwashing** → an action (behavior)

---
✅ **Key Difference**: A class defines what an object will have and do, while an object is the actual implementation of those definitions in memory.
