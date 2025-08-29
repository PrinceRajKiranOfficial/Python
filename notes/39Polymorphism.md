# Polymorphism in Python

**Polymorphism** allows different classes to define methods with the **same name** but with **different behavior**.

👉 In simple words: *same method name, but changing the behavior depending on the class/object*.

---

## Key Points

* Improves **code reusability** and **code reduction**.
* Same function or method name can work differently depending on the context.
* Makes programs more flexible and extensible.

---

## Example 1: Polymorphism with Functions

```python
def add(x, y, z=0):
    return x + y + z

print(add(2, 3))       # Output: 5
print(add(2, 3, 4))    # Output: 9
```

Here, the function `add()` behaves differently based on the number of arguments passed.

---

## Example 2: Polymorphism with Classes

```python
class Circle:
    def area(self, radius):
        return 3.14 * radius * radius

class Square:
    def area(self, side):
        return side * side

# Objects
c = Circle()
s = Square()

print("Circle area:", c.area(5))   # Output: 78.5
print("Square area:", s.area(4))   # Output: 16
```

Here, both classes have an `area()` method but their behavior is different.

---

## Example 3: Polymorphism with Inheritance

```python
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Polymorphism in action
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()
```

Output:

```
Bark
Meow
```

Each object responds differently to the same `sound()` method call.

---

✅ **Summary:** Polymorphism enables the same method name to be used across different classes with varying implementations. It helps in **code reduction, flexibility, and scalability** of programs.
