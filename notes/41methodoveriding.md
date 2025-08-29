#methodoveriding.md
# Method Overriding in Python

**Method Overriding** occurs when a **child class** provides a specific implementation of a method that is already defined in its **parent class**.  
This enables **runtime polymorphism** (dynamic method resolution).

---

## Key Concept

- The **same method name** is defined in both parent and child classes.
- The child class method **overrides** the parent class method.
- The method called is determined at **runtime** based on the object type.

---

## Example: Method Overriding

```python
class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def sound(self):   # Overriding the parent method
        print("Dog barks")

class Cat(Animal):
    def sound(self):   # Overriding the parent method
        print("Cat meows")


# Runtime polymorphism
animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()  # Output: Animals make sounds
dog.sound()     # Output: Dog barks
cat.sound()     # Output: Cat meows
