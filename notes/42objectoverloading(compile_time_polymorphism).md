# Operator Overloading in Python (Compile-Time Polymorphism)

Operator overloading allows us to redefine the behavior of built-in operators (such as `+`, `-`, `*`, etc.) for user-defined classes. This enables intuitive usage of custom objects with operators.

## Example: Adding Two Points

In this example, we define a `Point` class and overload the `+` operator so that two `Point` objects can be added directly.

```python
class Point:
    def __init__(self, x, y):   # Constructor
        self.x = x
        self.y = y

    def __add__(self, other):   # Overloading the '+' operator
        return Point(self.x + other.x, self.y + other.y)


# Creating two Point objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Adding points using overloaded '+'
p3 = p1 + p2

print(p3.x, p3.y)  # Output: 4 6
