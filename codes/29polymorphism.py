# 29polymorphism.py
"""
Demonstration of Polymorphism in Python.
Here, both Bird and Cat classes define the same method `sound()`,
but with different behaviors. The function `make_sound()` accepts
any object and calls its `sound()` method, showcasing polymorphism.
"""

class Bird:
    def sound(self):
        print("Chirp")
    
class Cat:
    def sound(self):
        print("Meow")

# Polymorphic function
def make_sound(animal):
    animal.sound()

# Object creation
b = Bird()
c = Cat()

# Temporary reference through `animal` parameter
make_sound(b)  # Output: Chirp
make_sound(c)  # Output: Meow

# Here we are temporarily storing the Bird and Cat objects
# in the 'animal' reference parameter to achieve polymorphism.
