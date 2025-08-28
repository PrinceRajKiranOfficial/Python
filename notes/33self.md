# `self` Attribute in Python

In Python classes, `self` is a special reference variable that represents the **instance of the class**. It is used to access variables and methods associated with the current object.

## Key Points
- `self` refers to the current object of the class.
- It must be the **first parameter** in instance methods (including `__init__`).
- It allows access to **attributes** and **methods** of the object.
- Without `self`, Python methods would not know which object's attributes to operate on.

## Example
```python
class Car:
    def __init__(self, brand, model):
        # using self to initialize object attributes
        self.brand = brand
        self.model = model

    def display_info(self):
        # using self to access object attributes
        print(f"Car Brand: {self.brand}, Model: {self.model}")

# Creating objects
car1 = Car("Tesla", "Model S")
car2 = Car("BMW", "X5")

car1.display_info()  # Output: Car Brand: Tesla, Model: Model S
car2.display_info()  # Output: Car Brand: BMW, Model: X5
```

## Real-world Analogy
Think of a **class** as a **form template** and an **object** as the filled-out form.
- `self` is like saying *“this particular form”* — it helps the class methods know which object's data they are working with.

---
✅ **Summary**: `self` is a reference to the current instance of the class. It is required to access and modify object attributes and to call methods inside a class.
