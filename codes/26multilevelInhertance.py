# multilevel_inheritance.py
"""
This script demonstrates Multilevel Inheritance in Python.
- Grandparent → Parent → Child
Each class inherits properties from its parent class.
"""

# Grandparent class
class Grandparent:
    def grandparentHouse(self):
        print("This is grandparent property")


# Parent class inheriting Grandparent
class Parent(Grandparent):
    def parentHouse(self):
        print("This is parent property")


# Child class inheriting Parent
class Child(Parent):
    def childHouse(self):
        print("This is child property")


# Object creation and method calls
if __name__ == "__main__":
    c1 = Child()
    c1.grandparentHouse()   # Inherited from Grandparent
    c1.parentHouse()        # Inherited from Parent
    c1.childHouse()         # Child's own method
