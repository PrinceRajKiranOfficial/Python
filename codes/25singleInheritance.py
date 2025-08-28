# single_inheritance.py
"""
This script demonstrates Single Inheritance in Python.
A Child class inherits from a single Parent class.
"""

# Parent class
class Parent:
    def parentHouse(self):
        print("This is parent property")


# Child class inheriting Parent
class Child(Parent):
    def childHouse(self):
        print("This is child property")


# Object creation and method calls
if __name__ == "__main__":
    c1 = Child()
    c1.parentHouse()   # Inherited method
    c1.childHouse()    # Child's own method
